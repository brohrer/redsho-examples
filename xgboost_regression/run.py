from redsho.optimizer import optimize
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
from xgboost import XGBRegressor

n_iter = int(1e3)

# Wine quality dataset from UC Irvine Machine Learning Repository
# full description here
# https://archive.ics.uci.edu/dataset/186/wine+quality
wine_quality = fetch_ucirepo(id=186)

X_all = wine_quality.data.features
y_all = wine_quality.data.targets

parameter_grid = {
    "gamma": [0, 0.01, 0.02, 0.05],
    "grow_policy": ["depthwise", "lossguide"],
    "learning_rate": [0.05, 0.1, 0.15, 0.2, 0.25, 0.3],
    "max_depth": [6, 8, 10, 12, 16, 20],
    "n_estimators": [10, 20, 50, 100, 150, 200],
    "objective": ["reg:squarederror", "reg:absoluteerror"],
}

X_train, X_test, y_train, y_test = train_test_split(
    X_all,
    y_all,
    test_size=0.2,
)


def evaluate(
    *,
    gamma,
    grow_policy,
    learning_rate,
    max_depth,
    n_estimators,
    objective,
):
    model = XGBRegressor(
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

    for predicted, actual in zip(predictions, y_test["quality"]):
        error += abs(float(predicted) - float(actual))

    mae = error / predictions.size

    print(f"mean absolute error: {mae}", end="\r")

    return mae


print()
print()

error, params = optimize(
    parameter_grid,
    evaluate,
    n_iter=n_iter,
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
