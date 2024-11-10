import google.generativeai as genai
import pathlib
from load_creds import load_creds
from db_helper import get_database, get_training_data, get_validation_data
from api_key import api_key

genai.configure(api_key=api_key())
folder = pathlib.Path(__file__).parents[0] / "files"
spec_pdf = genai.upload_file(folder / "855spec.pdf")

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
    tuned_prompt = """Convert the given EDI into JSON as per tuned model. Use the attached pdf to learn more about EDI 855.""" + edi
    tuned_response = tuned_model.generate_content(tuned_prompt)
    return tuned_response.text

def generic_prompt(edi, json, chat_input) :
    chat_prompt = """Consider the EDI given below""" + edi + '\n'
    chat_prompt = chat_prompt + """Consider the JSON given below""" + json + '\n'
    chat_prompt = chat_prompt + """Give the answer for the questions based on the edi and json passed.""" + chat_input
    default_flash_model = genai.GenerativeModel("models/gemini-1.5-flash")
    input_response = default_flash_model.generate_content([chat_prompt, spec_pdf])
    return input_response.text

def validate_data(edi, json) :
    chat_prompt = """Consider the EDI given below""" + edi + '\n'
    chat_prompt = chat_prompt + """Consider the JSON given below""" + json + '\n'
    chat_prompt = chat_prompt + """Give only the purchase order number based on the edi and json passed. Do not give any other extra text or information"""
    default_flash_model = genai.GenerativeModel("models/gemini-1.5-flash")
    po_number = default_flash_model.generate_content([chat_prompt, spec_pdf])

    validation_data = get_validation_data(po_number.text)
    chat_prompt = """Consider the EDI given below""" + edi + '\n'
    chat_prompt = chat_prompt + """Consider the VALIDATION DATA given below \n"""  + validation_data
    rules = """Validate the data for the below rules (EDI vs VALIDATION DATA) and give result for each item along with evidence \n
               1) Date in BAK section of EDI should be within than 1 month from the podate from VALIDATION DATA \n
               2) status should be success from VALIDATION DATA \n
               3) Date in ACK should be less than itemdate from the validation data for each item"""
    chat_prompt = chat_prompt + rules
    validation_response = default_flash_model.generate_content(
        chat_prompt,
        generation_config=genai.types.GenerationConfig(response_mime_type='application/json'),
        )
    return validation_response.text
