# XGBoost for regression

[XGBoost](https://xgboost.readthedocs.io/en/stable/index.html)
is a well known tool for using gradient-boosted decision trees,
alongside [CatBoost](https://catboost.ai) and
[LightGBM](https://lightgbm.readthedocs.io/en/latest/index.html).
XGBoost provides the engineer a lot of control, in the form of a lot of
parameters that can be adjusted. While the amount of control it gives can be
intoxicating, it can also be overwhelming. Like a pitcher of margaritas.
This makes it a prime candidate for some hyperparameter optimization.

This example showcases redsho's ability to handle both categorical and
numerical parameters, and how it does some exploration, but tends to
spend most of its time in the neighborhood of the best solutions found
so far.

In particular, this model learns to predict the quality of a wine
(rated on an integer scale from 1-10), from a variety of other
characteristics, like pH and percent alcohol. 

## Installing XGBoost

The Python package used here is `xgboost-cpu`. While it doesn't make use of
GPUs, like the full `xgboost` package does, it is considerably smaller
and simpler. It can require one extra setup step on MacOS at least. From
the command line

```bash
brew install libomp
```

to install the libraries it relies on.

## Run the example

From the command line

```bash
uv run run.py
```

to run the example. This will let you watch the error for each parameter
collection scoll by. The error is the average amount that the model
is off by on the quality assessment.

When the run is done it gives you a final report that looks like

```text
Lowest mean absolute error found: 0.3979377508163452
at parameter values:
    gamma: 0
    grow_policy: depthwise
    learning_rate: 0.12
    max_depth: 10
    n_estimators: 250
    objective: reg:squarederror
```

(The actual lowest error and parameter values depends on how the data
gets split into training and test groups, which is different every time.)
