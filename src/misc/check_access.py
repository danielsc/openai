from azureml.core import Run
keyname = "openai-key"
print(f"checking secret {keyname}")
run = Run.get_context()
secret_value = run.get_secret(name=keyname)
if secret_value.startswith("sk"):
  print("looking good")
else:
  print("secret doesn't look right")