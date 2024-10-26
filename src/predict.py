import pandas as pd
import joblib

def make_prediction(model_path, input_data):
    # Load the model
    model = joblib.load(model_path)
    
    # Predict using the model
    predictions = model.predict(input_data[['GrLivArea', 'BedroomAbvGr', 'FullBath']])
    return predictions

if __name__ == "__main__":
    # Example usage
    test_data = pd.read_csv('data/test.csv')
    predictions = make_prediction('models/model.joblib', test_data)
    print(predictions)
