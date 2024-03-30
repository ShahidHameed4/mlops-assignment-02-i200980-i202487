from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('iris_classifier.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        data['sepal_length'],
        data['sepal_width'],
        data['petal_length'],
        data['petal_width'],
        data['PetalLengthCm']
    ]
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
