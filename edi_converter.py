import google.generativeai as genai
from load_creds import load_creds
from populate_edi855_data import get_database

creds = load_creds()
genai.configure(credentials=creds)

edi855_json_db = get_database("edi855_edi_json_data")
model_collection = edi855_json_db["finetune_model_names"]

models = model_collection.find().sort({"timestamp":-1})
tuned_model = "models/gemini-1.5-flash"
for model in models:
    latest = True
    if latest:
        tuned_model = genai.GenerativeModel(model_name=model.get("tunedmodelname"))
    latest = False


def get_json_response_for_edi( edi) :
    tuned_prompt = """Convert the given EDI into JSON as per tuned model.""" + edi
    tuned_response = tuned_model.generate_content(tuned_prompt)
    return tuned_response.text
