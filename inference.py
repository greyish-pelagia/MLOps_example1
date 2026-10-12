from pathlib import Path

import joblib


def load_model():
    return joblib.load(Path(__file__).with_name("model.joblib"))


def predict(model, data):
    features = [
        [
            data["sepal_length"],
            data["sepal_width"],
            data["petal_length"],
            data["petal_width"],
        ]
    ]
    return str(model.predict(features)[0])
