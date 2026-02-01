import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler

def train_models(csv_path):
    df = pd.read_csv(csv_path)

    # FIX percentage column
    if "Shooting accuracy %" in df.columns:
        df["Shooting accuracy %"] = (
            df["Shooting accuracy %"]
            .astype(str)
            .str.replace("%", "", regex=False)
            .astype(float)
        )

    features = [
        "Age",
        "Appearances",
        "Shots",
        "Shots on target",
        "Shooting accuracy %",
        "Assists",
        "Passes per match",
        "Big chances created"
    ]

    df = df.dropna(subset=features + ["Goals"])

    X = df[features]
    y_reg = df["Goals"]

    # Classification target
    df["High_Performer"] = (df["Goals"] >= df["Goals"].median()).astype(int)
    y_clf = df["High_Performer"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train_reg, y_test_reg = train_test_split(
        X_scaled, y_reg, test_size=0.2, random_state=42
    )

    _, _, y_train_clf, y_test_clf = train_test_split(
        X_scaled, y_clf, test_size=0.2, random_state=42
    )

    reg_model = LinearRegression()
    reg_model.fit(X_train, y_train_reg)

    clf_model = LogisticRegression(max_iter=2000)
    clf_model.fit(X_train, y_train_clf)

    return reg_model, clf_model, scaler, features, df
