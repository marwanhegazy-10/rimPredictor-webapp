import pandas as pd
import pickle

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def predict_outcome(model, features):
    prediction = model.predict(features)
    return prediction

def prepare_data(df, predictors):
    # Select relevant features for prediction
    features = df[predictors]
    return features

def train_model(df, predictors, target):
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import RidgeClassifier

    X = df[predictors]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RidgeClassifier(alpha=1)
    model.fit(X_train, y_train)

    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy