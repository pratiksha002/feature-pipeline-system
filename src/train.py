import pandas as pd
import pickle
import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from src.pipeline_builder import build_pipeline

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def train_model():
    data = {
        "age": [25, 30, None, 35, 40, None],
        "city": ["Mumbai", "Delhi", "Mumbai", None, "Delhi", "Mumbai"],
        "salary": [50000, 60000, 55000, 65000, 70000, 62000]
    }

    df = pd.DataFrame(data)

    x = df[["age", "city"]]
    y = df["salary"]

    numerical_features = ["age"]
    categorical_features = ["city"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    pipeline = build_pipeline(numerical_features, categorical_features)

    x_train_transformed = pipeline.fit_transform(x_train)

    x_test_transformed = pipeline.transform(x_test)

    model = LinearRegression()
    model.fit(x_train_transformed, y_train)

    os.makedirs("models", exist_ok=True)
    os.makedirs("pipelines", exist_ok=True)

    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("pipelines/preprocess_pipeline.pkl", "wb") as f:
        pickle.dump(pipeline, f)

    return model, pipeline


if __name__ == "__main__":
    train_model()
    print("Training complete!")