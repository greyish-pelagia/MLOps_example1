from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

MODEL_PATH = Path(__file__).with_name("model.joblib")


def load_data():
    return load_iris()


def train_model():
    data = load_data()
    model = DecisionTreeClassifier(random_state=42)
    model.fit(data.data, data.target_names[data.target])
    return model


def save_model(model):
    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    save_model(train_model())
