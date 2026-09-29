# Mission Control: prepare training telemetry
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model():
    # Mission Control: load space-object telemetry
    data = pd.read_csv("data/sample_objects.csv")

    # Mission Control: create prototype observation labels
    data["risk"] = [
        "HIGH",
        "MEDIUM",
        "LOW",
        "HIGH",
        "MEDIUM"
    ]

    # Mission Control: select telemetry features
    X = data[["distance_km", "velocity_km_s", "size_m"]]

    # Mission Control: select mission risk labels
    y = data["risk"]

    # Mission Control: train the observation classifier
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model