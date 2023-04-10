# set up openai api
import openai, os
openai.api_type = "azure"
openai.api_version = "2022-12-01"
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_key = os.environ["OPENAI_API_KEY"]

cog_search_patched = False

# set up cog search retriever
from langchain.docstore.document import Document
from langchain.schema import BaseRetriever, Document
from typing import List
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import mlflow
import json
import tempfile
import os
from patch import log_json_artifact


class CognitiveSearchRetriever(BaseRetriever):
    def __init__(self, endpoint: str, index_name: str, searchkey: str, top: int = 3, verbose: bool = False):
        self.endpoint = endpoint
        self.index_name = index_name
        self.searchkey = searchkey
        self.top = top
        self.verbose = verbose
        self.client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(searchkey))
    
    def dict(self):
        return {
            "endpoint": self.endpoint,
            "index_name": self.index_name,
            "searchkey": "********",
            "top": self.top,
            "verbose": self.verbose,
        }   

    def get_relevant_documents(self, query: str) -> List[Document]:
        docs = []
        for i in self.client.search(query, top=self.top):
            docs.append(Document(page_content=i['content'], metadata={"sourcefile": i['sourcefile']}))
        if self.verbose:
            print("cog_search_top:", self.top)
            print("cog_search_query:", query)
            print("cog_search_docs:", docs)
            mlflow.log_param("cog_search_top", self.top)
            mlflow.log_param("cog_search_query", query)
            docs_json = [{ 'page_content': doc.page_content, 'metadata': doc.metadata  } for doc in docs]

            # Write the dictionary to a temporary file
            log_json_artifact(docs_json, "cog_search_docs.json")

        return docs

    async def aget_relevant_documents(self, query: str) -> List[Document]:
        pass

from langchain.chains import RetrievalQA
from langchain.chat_models import AzureChatOpenAI
from patch import patch_langchain, log_function_call

def rag(question: str, top: int = 3, chain_type: str = "stuff", meta_prompt: str = None, verbose: bool = False): 
    global cog_search_patched

    if verbose:
        # patch langchain to log function calls
        patch_langchain()
        if not cog_search_patched:
            cog_search_patched = True
            CognitiveSearchRetriever.get_relevant_documents = log_function_call(CognitiveSearchRetriever.get_relevant_documents)
        

    search_endpoint = os.environ["COG_SEARCH_ENDPOINT"]
    index_name = "amldocs"
    searchkey = os.environ["COG_SEARCH_KEY"]
    retriever = CognitiveSearchRetriever(search_endpoint, index_name, searchkey, top=top, verbose=verbose)

    llm = AzureChatOpenAI(
        deployment_name="gpt-35-turbo",
        temperature=0,
        openai_api_version="2023-03-15-preview",
    )

    qa = RetrievalQA.from_chain_type(llm=llm, 
                                    chain_type=chain_type,
                                    retriever=retriever)
    return qa(question)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, default="What is a pipeline?")
    parser.add_argument("--top", type=int, default=3)
    parser.add_argument("--chain_type", type=str, default="stuff")
    parser.add_argument("--meta_prompt", type=str, default=None)
    parser.add_argument("--no-log", action='store_true')
    args = parser.parse_args()

    verbose = not args.no_log

    if verbose:
        # mlflow.start_run()
        mlflow.log_param("question", args.question)
        mlflow.log_param("top", args.top)
        mlflow.log_param("chain_type", args.chain_type)
        mlflow.log_param("meta_prompt", args.meta_prompt)

    result = rag(args.question, top=args.top, chain_type=args.chain_type, meta_prompt=args.meta_prompt, verbose=verbose)
    
    if verbose:
        log_json_artifact(result, "result.json")

    print("Q:", result["query"])
    print("A:", result["result"])