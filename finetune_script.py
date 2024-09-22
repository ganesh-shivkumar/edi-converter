import time
import google.generativeai as genai
from load_creds import load_creds
from edi_training_data import TrainingData
from populate_edi855_data import get_database
from datetime import datetime

creds = load_creds()
genai.configure(credentials=creds)

data_obj = TrainingData()

def finetune_model():
    base_model = "models/gemini-1.5-flash-001-tuning"
    training_data = data_obj.training_data()

    operation = genai.create_tuned_model(
        display_name="finetune-edi-855",
        source_model=base_model,
        epoch_count=20,
        batch_size=4,
        learning_rate=0.001,
        training_data=training_data,
    )

    for status in operation.wait_bar():
        time.sleep(2)

    result = operation.result()

    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    edi855_json_db = get_database("edi855_edi_json_data")
    model_collection = edi855_json_db["finetune_model_names"]
    print(result.name)

    model_1 = {
        "_id" : timestamp_str+"-tunedmodel",
        "timestamp" : timestamp_str,
        "tunedmodelname" : result.name
    }

    model_collection.insert_one(model_1)
    return result.name
