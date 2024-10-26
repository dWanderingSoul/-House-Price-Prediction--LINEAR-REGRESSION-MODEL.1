from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    
    # Make predictions
    predictions = model.predict(df[['GrLivArea', 'BedroomAbvGr', 'FullBath']])
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
