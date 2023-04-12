
#### Define optional inputs in command line
When the input is set as `optional = true`, you need use `$[[]]` to embrace the command line with inputs. For example `$[[--input1 ${{inputs.input1}}]`. The command line at runtime may have different inputs.
- If you are using only specify the required `training_data` and `model_output` parameters, the command line will look like:

```cli
python train.py --training_data some_input_path --learning_rate 0.01 --learning_rate_schedule time-based --model_output some_output_path
```

If no value is specified at runtime, `learning_rate` and `learning_rate_schedule` will use the default value.

- If all inputs/outputs provide values during runtime, the command line will look like:
```cli
python train.py --training_data some_input_path --max_epocs 10 --learning_rate 0.01 --learning_rate_schedule time-based --model_output some_output_path
```

## Next steps

* [Install and use the CLI (v2)](how-to-configure-cli.md)
* [Train models with the CLI (v2)](how-to-train-model.md)
* [CLI (v2) YAML schemas](reference-yaml-overview.md)
