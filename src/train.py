import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model(train_path, model_path):
    # Load training data
    train_data = pd.read_csv(train_path)
    X_train = train_data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
    y_train = train_data['SalePrice']
    
    # Train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model('data/train.csv', 'models/model.joblib')
