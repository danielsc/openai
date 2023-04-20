import logging
from packaging import version
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.utils import (
    BaseMetadataCallbackHandler,
    flatten_dict,
    hash_string,
    import_pandas,
    import_spacy,
    import_textstat,
)
from langchain.schema import AgentAction, AgentFinish, LLMResult
import mlflow
import tempfile, json, os
from langchain.docstore.document import Document
import json, yaml
import os

module_logger = logging.getLogger(__name__)

def serialize(obj):
    # Handle simple types
    if isinstance(obj, (int, float, str, bool)):
        return obj

    # Handle dicts
    elif isinstance(obj, dict):
        serialized_dict = {}
        for key, value in obj.items():
            if "key" in key.lower():
                serialized_dict[key] = "********"
            else:
                serialized_dict[key] = serialize(value)
        return serialized_dict

    # Handle lists and tuples
    elif isinstance(obj, (list, tuple)):
        serialized_list = []
        for item in obj:
            serialized_list.append(serialize(item))
        if isinstance(obj, tuple):
            return tuple(serialized_list)
        else:
            return serialized_list

    # Handle LangChain Document
    elif isinstance(obj, Document):
        serialized_doc = { 'page_content': obj.page_content, 'metadata': obj.metadata  } 
        return serialized_doc
    
    # handle pydantic models (openai uses pydantic)
    elif hasattr(obj, "dict") and callable(getattr(obj, "dict")):
        return {str(obj.__class__): serialize(obj.dict())}
    
    # Handle other types
    else:
        return str(obj)

def log_json_artifact(json_data, artifact_name):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file in the temporary directory
        with open(os.path.join(temp_dir, artifact_name), "w") as f:
            json.dump(serialize(json_data), f)

        # Log the file as an artifact
        mlflow.log_artifact(os.path.join(temp_dir, artifact_name))

def log_yaml_artifact(yaml_data, artifact_name):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file in the temporary directory
        with open(os.path.join(temp_dir, artifact_name), "w") as f:
            yaml.dump(serialize(yaml_data), f)

        # Log the file as an artifact
        mlflow.log_artifact(os.path.join(temp_dir, artifact_name))


def import_mlflow() -> Any:
    try:
        import mlflow  # noqa: F401
    except ImportError:
        raise ImportError(
            "To use the mlflow callback manager you need to have the `mlflow` python "
            "package installed. Please install it with `pip install mlflow`"
        )
    else:
        if version.parse(mlflow.__version__) < version.parse("2.0.0"):
            raise ImportError(
                f"The current version of the mlflow callback has only been tested on MLflow "
                "versions above 2.0. The currently installed version is {mlflow.__version__}"
            )
    return mlflow

def analyze_text(
    text: str,
    complexity_metrics: bool = True,
    visualize: bool = True,
    nlp: Any = None,
    output_dir: Optional[Union[str, Path]] = None,
    mlflow_client = None,
    run_id = None
) -> dict:
    """Analyze text using textstat and spacy.

    Parameters:
        text (str): The text to analyze.
        complexity_metrics (bool): Whether to compute complexity metrics.
        visualize (bool): Whether to visualize the text.
        nlp (spacy.lang): The spacy language model to use for visualization.
        output_dir (str): The directory to save the visualization files to.

    Returns:
        (dict): A dictionary containing the complexity metrics and visualization
            files serialized in a string.
    """
    resp = {}
    textstat = import_textstat()
    spacy = import_spacy()
    if complexity_metrics:
        text_complexity_metrics = {
            "flesch_reading_ease": textstat.flesch_reading_ease(text),
            "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
            "smog_index": textstat.smog_index(text),
            "coleman_liau_index": textstat.coleman_liau_index(text),
            "automated_readability_index": textstat.automated_readability_index(text),
            "dale_chall_readability_score": textstat.dale_chall_readability_score(text),
            "difficult_words": textstat.difficult_words(text),
            "linsear_write_formula": textstat.linsear_write_formula(text),
            "gunning_fog": textstat.gunning_fog(text),
            "text_standard": textstat.text_standard(text),
            "fernandez_huerta": textstat.fernandez_huerta(text),
            "szigriszt_pazos": textstat.szigriszt_pazos(text),
            "gutierrez_polini": textstat.gutierrez_polini(text),
            "crawford": textstat.crawford(text),
            "gulpease_index": textstat.gulpease_index(text),
            "osman": textstat.osman(text),
        }
        resp.update(text_complexity_metrics)

    if visualize and nlp and output_dir is not None:
        doc = nlp(text)

        dep_out = spacy.displacy.render(  # type: ignore
            doc, style="dep", jupyter=False, page=True
        )
        dep_output_path = Path(output_dir, hash_string(f"dep-{text}") + ".html")
        dep_output_path.open("w", encoding="utf-8").write(dep_out)

        ent_out = spacy.displacy.render(  # type: ignore
            doc, style="ent", jupyter=False, page=True
        )
        ent_output_path = Path(output_dir, hash_string(f"ent-{text}") + ".html")
        ent_output_path.open("w", encoding="utf-8").write(ent_out)

        mlflow_client.log_artifact(run_id, dep_output_path, "dependency_tree")
        mlflow_client.log_artifact(run_id, ent_output_path, "entities")
        text_visualizations = {
            "dependency_tree": str(dep_output_path),
            "entities": str(ent_output_path),
        }
        resp.update(text_visualizations)

    return resp


def construct_html_from_prompt_and_generation(prompt: str, generation: str) -> Any:
    """Returns html document contents from a prompt and a generation.

    Parameters:
        prompt (str): The prompt.
        generation (str): The generation.

    Returns:
        (str): The html content."""
    formatted_prompt = prompt.replace("\n", "<br>")
    formatted_generation = generation.replace("\n", "<br>")

    return f"""
    <p style="color:black;">{formatted_prompt}:</p>
    <blockquote>
      <p style="color:green;">
        {formatted_generation}
      </p>
    </blockquote>
    """


class MLflowCallbackHandler(BaseMetadataCallbackHandler, BaseCallbackHandler):
    """Callback Handler that logs to MLflow.

    Parameters:
        experiment_name (str): The name of the experiment to log to.
        experiment_id (str): The id of the experiment to log to.
        run_id (str): The id of the run to log to.
        tags (dict): A dictionary of tags to log to the run.
        name (str): The display name of the run to log to.
        notes (str): The notes to log to the run.
        nest_actions (bool): Whether to store actions in nested runs.

    This handler will utilize the associated callback method called and formats
    the input of each callback function with metadata regarding the state of LLM run,
    and adds the response to the list of records for both the {method}_records and
    action. It then logs the response using the run.log() method to Weights and Biases.
    """

    def __init__(
        self,
        experiment_name: Optional[str] = None,
        experiment_id: Optional[str] = None,
        run_id: Optional[str] = None,
        tags: Optional[dict[str, str]] = None,
        name: Optional[str] = None,
        notes: Optional[str] = None,
        nest_actions: bool = False,
        visualize: bool = False,
        complexity_metrics: bool = False,
    ) -> None:
        """Initialize callback handler."""

        mlflow = import_mlflow()
        #import_pandas()
        #import_textstat()
        #spacy = import_spacy()

        super().__init__()

        from mlflow.tracking import MlflowClient
        from mlflow import ActiveRun
        self.mlflow_client: MlflowClient = MlflowClient()
        module_logger.info("Saving data to %s", mlflow.get_tracking_uri())

        # Resolve the experiment from configuration
        if experiment_id and experiment_name:
            raise ValueError("Cannot provide both experiment_id and experiment_name")
        elif experiment_name:
            experiment_id = mlflow.create_experiment("experiment1")

        self.experiment_id = experiment_id
        self.tags = tags
        self.notes = notes
        self.name = name

        active_run = mlflow.active_run()
        if not active_run:
            # module_logger.warning("Detected an active MLflow, cleaning")
            # active_run.__exit__(None, None, None)
            self.mlflow_run: ActiveRun = mlflow.start_run(
                run_id=run_id, experiment_id=experiment_id, run_name=name,
                tags=tags, description=notes)

        self.nest_actions = nest_actions
        if self.nest_actions:
            # {
            #   run_id: {
            #       start: {},
            #       end: {}
            #   }
            # }
            self.nested_runs: dict[str, dict[str, Any]] = {}

        self.temp_dir = tempfile.TemporaryDirectory()
        warning = (
            "The mlflow callback is currently in beta and is subject to change "
            "based on updates to `langchain`. Please report any issues to "
            "https://github.com/mlflow/mlflow/issues."
        )
        logging.warning(warning)

        self.visualize = visualize
        self.complexity_metrics = complexity_metrics
        self.callback_columns: list = []
        self.action_records: list = []
        #self.nlp = spacy.load("en_core_web_sm")
        self.nlp = None

    def _init_resp(self) -> Dict:
        return {k: None for k in self.callback_columns}

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts."""
        self.step += 1
        self.llm_starts += 1
        self.starts += 1

        resp = self._init_resp()
        resp.update({"action": "on_llm_start"})
        resp.update(flatten_dict(serialized))
        resp.update(self.get_custom_callback_meta())

        for prompt in prompts:
            prompt_resp = deepcopy(resp)
            prompt_resp["prompts"] = prompt
            self.on_llm_start_records.append(prompt_resp)
            self.action_records.append(prompt_resp)
            module_logger.info("%s", prompt_resp)
            log_yaml_artifact(prompt_resp, f"{self.step}_{resp['action']}.yaml")


    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run when LLM generates a new token."""
        self.step += 1
        self.llm_streams += 1

        resp = self._init_resp()
        resp.update({"action": "on_llm_new_token", "token": token})
        resp.update(self.get_custom_callback_meta())

        self.on_llm_token_records.append(resp)
        self.action_records.append(resp)
        module_logger.info("%s", resp)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        self.step += 1
        self.llm_ends += 1
        self.ends += 1

        resp = self._init_resp()
        resp.update({"action": "on_llm_end"})
        resp.update(flatten_dict(response.llm_output or {}))
        resp.update(self.get_custom_callback_meta())

        for generations in response.generations:
            for generation in generations:
                generation_resp = deepcopy(resp)
                generation_resp.update(flatten_dict(generation.dict()))
                # generation_resp.update(
                #     # TODO: I'm leaking these outputs - save in the same model or separate artifacts?
                #     analyze_text(
                #         generation.text,
                #         complexity_metrics=self.complexity_metrics,
                #         visualize=self.visualize,
                #         nlp=self.nlp,
                #         output_dir=self.temp_dir.name,
                #         mlflow_client=self.mlflow_client,
                #         run_id = self.mlflow_run.info.run_id
                #     )
                # )
                self.on_llm_end_records.append(generation_resp)
                self.action_records.append(generation_resp)
                module_logger.info("%s", generation_resp)
                log_yaml_artifact(generation_resp, f"{self.step}_{resp['action']}.yaml")


    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Run when LLM errors."""
        self.step += 1
        self.errors += 1

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Run when chain starts running."""
        self.step += 1
        self.chain_starts += 1
        self.starts += 1

        resp = self._init_resp()
        resp.update({"action": "on_chain_start"})
        resp.update(flatten_dict(serialized))
        resp.update(self.get_custom_callback_meta())

        chain_input = inputs["input"]

        if isinstance(chain_input, str):
            input_resp = deepcopy(resp)
            input_resp["input"] = chain_input
            self.on_chain_start_records.append(input_resp)
            self.action_records.append(input_resp)
            module_logger.info("%s", input_resp)
        elif isinstance(chain_input, list):
            for inp in chain_input:
                input_resp = deepcopy(resp)
                input_resp.update(inp)
                self.on_chain_start_records.append(input_resp)
                self.action_records.append(input_resp)
                module_logger.info("%s", input_resp)
        else:
            raise ValueError("Unexpected data format provided!")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Run when chain ends running."""
        self.step += 1
        self.chain_ends += 1
        self.ends += 1

        resp = self._init_resp()
        resp.update({"action": "on_chain_end", "outputs": outputs["output"]})
        resp.update(self.get_custom_callback_meta())

        self.on_chain_end_records.append(resp)
        self.action_records.append(resp)
        module_logger.info("%s", resp)

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Run when chain errors."""
        self.step += 1
        self.errors += 1

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> None:
        """Run when tool starts running."""
        self.step += 1
        self.tool_starts += 1
        self.starts += 1

        resp = self._init_resp()
        resp.update({"action": "on_tool_start", "input_str": input_str})
        resp.update(flatten_dict(serialized))
        resp.update(self.get_custom_callback_meta())

        self.on_tool_start_records.append(resp)
        self.action_records.append(resp)
        module_logger.info("%s", resp)

    def on_tool_end(self, output: str, **kwargs: Any) -> None:
        """Run when tool ends running."""
        self.step += 1
        self.tool_ends += 1
        self.ends += 1

        resp = self._init_resp()
        resp.update({"action": "on_tool_end", "output": output})
        resp.update(self.get_custom_callback_meta())

        self.on_tool_end_records.append(resp)
        self.action_records.append(resp)
        module_logger.info("%s", resp)

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Run when tool errors."""
        self.step += 1
        self.errors += 1

    def on_text(self, text: str, **kwargs: Any) -> None:
        """
        Run when agent is ending.
        """
        self.step += 1
        self.text_ctr += 1

        resp = self._init_resp()
        resp.update({"action": "on_text", "text": text})
        resp.update(self.get_custom_callback_meta())

        self.on_text_records.append(resp)
        self.action_records.append(resp)
        module_logger.info("%s", resp)

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> None:
        """Run when agent ends running."""
        self.step += 1
        self.agent_ends += 1
        self.ends += 1

        resp = self._init_resp()
        resp.update(
            {
                "action": "on_agent_finish",
                "output": finish.return_values["output"],
                "log": finish.log,
            }
        )
        resp.update(self.get_custom_callback_meta())

        self.on_agent_finish_records.append(resp)
        self.action_records.append(resp)
        module_logger.info("%s", resp)

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Run on agent action."""
        self.step += 1
        self.tool_starts += 1
        self.starts += 1

        resp = self._init_resp()
        resp.update(
            {
                "action": "on_agent_action",
                "tool": action.tool,
                "tool_input": action.tool_input,
                "log": action.log,
            }
        )
        resp.update(self.get_custom_callback_meta())
        self.on_agent_action_records.append(resp)
        self.action_records.append(resp)
        module_logger.info("%s", resp)

    def _create_session_analysis_df(self) -> Any:
        """Create a dataframe with all the information from the session."""
        pd = import_pandas()
        on_llm_start_records_df = pd.DataFrame(self.on_llm_start_records)
        on_llm_end_records_df = pd.DataFrame(self.on_llm_end_records)

        llm_input_prompts_df = (
            on_llm_start_records_df[["step", "prompts", "name"]]
            .dropna(axis=1)
            .rename({"step": "prompt_step"}, axis=1)
        )
        complexity_metrics_columns = []
        visualizations_columns = []

        if self.complexity_metrics:
            complexity_metrics_columns = [
                "flesch_reading_ease",
                "flesch_kincaid_grade",
                "smog_index",
                "coleman_liau_index",
                "automated_readability_index",
                "dale_chall_readability_score",
                "difficult_words",
                "linsear_write_formula",
                "gunning_fog",
                "text_standard",
                "fernandez_huerta",
                "szigriszt_pazos",
                "gutierrez_polini",
                "crawford",
                "gulpease_index",
                "osman",
            ]

        if self.visualize:
            visualizations_columns = ["dependency_tree", "entities"]

        module_logger.debug("%s", on_llm_end_records_df)
        llm_outputs_df = (
            on_llm_end_records_df[
                [
                    "step",
                    "text",
                    "token_usage_total_tokens",
                    "token_usage_prompt_tokens",
                    "token_usage_completion_tokens",
                ]
                + complexity_metrics_columns
                + visualizations_columns
            ]
            .dropna(axis=1)
            .rename({"step": "output_step", "text": "output"}, axis=1)
        )
        session_analysis_df = pd.concat([llm_input_prompts_df, llm_outputs_df], axis=1)
        module_logger.debug("Session DF: %s", session_analysis_df)
        session_analysis_df["chat_html"] = session_analysis_df[
            ["prompts", "output"]
        ].apply(
            lambda row: construct_html_from_prompt_and_generation(
                row["prompts"], row["output"]
            ),
            axis=1,
        )
        return session_analysis_df

    def flush_tracker(
        self,
        langchain_asset: Any = None,
        reset: bool = True,
        finish: bool = False,
        experiment_name: Optional[str] = None,
        experiment_id: Optional[str] = None,
        run_id: Optional[str] = None,
        tags: Optional[dict[str, str]] = None,
        name: Optional[str] = None,
        notes: Optional[str] = None,
        nest_actions: Optional[bool] = None,
        visualize: Optional[bool] = None,
        complexity_metrics: Optional[bool] = None,
    ) -> None:
        """Flush the tracker and reset the session.

        Args:
            langchain_asset: The langchain asset to save.
            reset: Whether to reset the session.
            finish: Whether to finish the run.
            job_type: The job type.
            project: The project.
            entity: The entity.
            tags: The tags.
            group: The group.
            name: The name.
            notes: The notes.
            visualize: Whether to visualize.
            complexity_metrics: Whether to compute complexity metrics.

            Returns:
                None
        """
        # This is an interesting API - look into having the callback invoked with the assets instead.
        # Also look into more intuitive control flow for the callback, perhaps by having
        # agent.run or chain call()s partition the sessions

        # Treat this more as "ensure import" so we don't lose easy typing?
        _ = import_pandas()

        from pandas import DataFrame

        # Replace these with incoming charts
        action_records_table = DataFrame(self.action_records)
        session_analysis_table: DataFrame = self._create_session_analysis_df()

        from mlflow.models import Model
        from langchain import callbacks as cb
        Model.log(
            "model",
            cb.mlflow_callback,
            langchain_asset=langchain_asset,
            action_records=action_records_table,
            session_analysis=session_analysis_table)

        if finish or reset:
            self.mlflow_run.__exit__(None, None, None)
            self.temp_dir.cleanup()
            self.reset_callback_meta()
        if reset:
            self.__init__(  # type: ignore
                experiment_id=experiment_id if experiment_id else self.experiment_id,
                run_id=run_id if run_id else self.mlflow_run.info.run_id,
                tags=tags if tags else self.tags,
                name=name if name else self.name,
                notes=notes if notes else self.notes,
                visualize=visualize if visualize else self.visualize,
                complexity_metrics=complexity_metrics if complexity_metrics else self.complexity_metrics,
            )