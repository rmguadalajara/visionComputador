from flask import Flask, request, jsonify
from modelo1 import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()  # Asume que los datos se envían como JSON en el cuerpo de la solicitud
    prediction = predict(data)
    return jsonify(prediction.tolist())  # Convierte la predicción a JSON

if __name__ == '__main__':
    app.run(debug=True)