from load_creds import load_creds
from finetune_script import finetune_model

creds = load_creds()
tunedModelName = finetune_model()
print(tunedModelName)