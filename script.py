from flask import Flask, jsonify, request
from edi_converter import get_json_response_for_edi, get_latest_from_db
from finetune_script import finetune_model

app = Flask(__name__)


@app.route('/api/data', methods=['POST'])
def get_data():
    return jsonify(get_json_response_for_edi(request.data.decode("utf-8")))

@app.route('/api/train', methods=['GET'])
def train_data():
    return jsonify(finetune_model())

@app.route('/api/tunedmodels/latest', methods=['GET'])
def get_latest_tuned_model():
    return jsonify(get_latest_from_db())

if __name__ == '__main__':
    app.run()
