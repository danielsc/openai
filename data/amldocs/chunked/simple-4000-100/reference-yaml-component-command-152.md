
If no value is specified at runtime, `learning_rate` and `learning_rate_schedule` will use the default value.

- If all inputs/outputs provide values during runtime, the command line will look like:
```azurecli
python train.py --training_data some_input_path --max_epocs 10 --learning_rate 0.01 --learning_rate_schedule time-based --model_output some_output_path
```


## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
- [Create ML pipelines using components (CLI v2)](how-to-create-component-pipelines-cli.md)
