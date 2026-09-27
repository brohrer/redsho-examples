import pandas as pd
from palmerpenguins import load_penguins
from redsho.optimizer import optimize
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier

data = load_penguins()
data["species"] = pd.Categorical(pd.factorize(data["species"])[0])

parameter_grid = {
    "gamma": [0, 1, 2, 4],
    "grow_policy": ["depthwise", "lossguide"],
    "learning_rate": [0.5, 0.75, 1.0, 1.25, 1.5, 2.0],
    "max_depth": [2, 3, 4, 5, 6],
    "n_estimators": [2, 3, 4, 6, 8],
    "objective": ["multi:softmax", "multi:softprob"],
}

X_all = data.loc[:, data.columns != "species"]
y_all = data["species"]

# one-hot encode the categorical features
categorical_attributes = ["island", "sex"]
full_pipeline = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore"), categorical_attributes)],
    remainder="passthrough",
)

encoder = full_pipeline.fit(X_all)
X_all = encoder.transform(X_all)

X_train, X_test, y_train, y_test = train_test_split(
    X_all,
    y_all,
    test_size=0.2,
    stratify=data["species"],
)

n_iter = 100


def evaluate(
    *,
    gamma,
    grow_policy,
    learning_rate,
    max_depth,
    n_estimators,
    objective,
):
    model = XGBClassifier(
        num_class=3,
        enable_categorical=True,
        gamma=gamma,
        grow_policy=grow_policy,
        learning_rate=learning_rate,
        max_depth=max_depth,
        n_estimators=n_estimators,
        objective=objective,
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    error = 0
    for predicted, actual in zip(predictions, y_test):
        if predicted != actual:
            error += 1

    print(f"error: {error}", end="\r")

    return error


print()
print()

error, params = optimize(
    parameter_grid,
    evaluate,
    n_iter=n_iter,
    update_plots=False,
    verbose=False,
)

print()
print()
print(f"Lowest mean absolute error found: {error}")
print("at parameter values:")
for k, v in params.items():
    if k == "error":
        continue
    print(f"    {k}: {v}")

print()
print()
