from flask import Flask, jsonify, request
from edi_converter import get_json_response_for_edi

app = Flask(__name__)


@app.route('/api/data', methods=['POST'])
def get_data():
    print(request)
    data = get_json_response_for_edi(request.data.decode("utf-8"))
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
