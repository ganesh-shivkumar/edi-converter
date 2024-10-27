import google.generativeai as genai
from load_creds import load_creds
from populate_edi855_data import get_database

creds = load_creds()
genai.configure(credentials=creds)

edi855_json_db = get_database("edi855_edi_json_data")
model_collection = edi855_json_db["finetune_model_names"]

models = model_collection.find().sort({"timestamp":-1})
tuned_model = "models/gemini-1.5-flash"
latest_tuned_model_name = ""
for model in models:
    tuned_model = genai.GenerativeModel(model_name=model.get("tunedmodelname"))
    latest_tuned_model_name = model.get("tunedmodelname") + " : " + model.get("timestamp")
    break

def get_latest_from_db():
    return latest_tuned_model_name

def get_json_response_for_edi(edi) :
    tuned_prompt = """Convert the given EDI into JSON as per tuned model.""" + edi
    tuned_response = tuned_model.generate_content(tuned_prompt)
    return tuned_response.text

def generic_prompt(edi, json, chat_input) :
    chat_prompt = """Consider the EDI given below""" + edi + '\n'
    chat_prompt = chat_prompt + """Consider the EDI given below""" + json + '\n'
    chat_prompt = chat_prompt + """Give the answer for the questions based on the edi and json passed.""" + chat_input
    default_flash_model = genai.GenerativeModel("models/gemini-1.5-flash")
    input_response = default_flash_model.generate_content(chat_prompt)
    return input_response.text