from flask import Flask, jsonify, request
from gemini_client import get_json_response_for_edi, get_latest_from_db, generic_prompt
from finetune_script import finetune_model
from user_login import create_or_login_user

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

@app.route('/api/chat', methods=['POST'])
def call_gemini():
    json_request = request.json
    edi = json_request['edi']
    json = json_request['json']
    chat_input = json_request['input']
    return jsonify(generic_prompt(edi, json, chat_input))

@app.route('/api/user/login', methods=['POST'])
def create_user():
    json_request = request.json
    username = json_request['username']
    password = json_request['password']
    action = json_request['action']
    return jsonify(create_or_login_user(username, password, action))

if __name__ == '__main__':
    app.run()
