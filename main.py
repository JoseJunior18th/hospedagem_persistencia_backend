from flask import Flask, request, jsonify
from flask_cors import CORS
import service

app = Flask(__name__)
CORS(app)

@app.route("/save-activities", methods=['POST'])
def saveData():
    data = request.get_json()
    service.saveExecute(data)
    print(data)
    return jsonify({"message": "Recebido com sucesso!"}), 200

@app.route("/query-sum", methods=['GET'])
def query():
    return service.querySum()

@app.route("/query-descriptions", methods=["GET"])
def queryDesc():
    return service.queryDescriptions()

if __name__ == '__main__':
    app.run(debug=True, port=3030)