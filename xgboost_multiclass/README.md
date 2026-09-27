# XGBoost for multiclass classification

This is very similar to the 
[XGBoost regression](/xgboost_regression/README.md) example, but for
a classification problem (choosing a group), rather than regression
(choosing a value). Check out the regression doc for info on XGBoost.

In this example, the model tries to learn to identify species
in the exceptionally high quality
[Palmer Penguins data set](https://allisonhorst.github.io/palmerpenguins/).
344 penguins from 3 different species are included, together with data
about their flipper length, sex, bill size, mass, and island of residence.

## Run the example

From the command line

```bash
uv run run.py
```

to run the example. This will let you watch the error for each parameter
collection scoll by. The error is the number of penguins misclassified in the
test set.

The outcome of the run will look something like

```bash
Lowest mean absolute error found: 0
at parameter values:
    gamma: 0
    grow_policy: lossguide
    learning_rate: 0.75
    max_depth: 6
    n_estimators: 2
    objective: multi:softmax
```

## Penguins dataset is an easy classification problem

This is actually a bad example for showing off XGBoost, because the moddel
is so capable and the data set is so clean that almost every variant achieves
the same, very low error. Whether it is off by one penguin, or two, or zero,
depends almost entirely on the random train/test split, which I have not
taken pains to make repeatable.

A scattershot plot of the data shows just a small handful of points that
aren't neatly separable, even when limited to just two features.

![Scatterplot of penguin species by flipper and bill length. The Adelie,
Chinstrap, and Gentoo clusters have a small amount of overlap, but it
is minimal.
](https://allisonhorst.github.io/palmerpenguins/reference/figures/README-flipper-bill-1.png)

But I'm OK with that. The goal of this example is to show how redsho works
with XGBoost in a multiclass classification problem, which it does. Enjoy!
