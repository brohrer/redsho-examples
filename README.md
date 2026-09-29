# redsho examples

A small collection of examples showing redsho in action.
[Redsho](https://codeberg.org/brohrer/redsho)
is a discrete optimizer, originally build for complex machine learning
systems.

As of right now, there are 4 examples, each in their own subdirectory:

`sinc`: optimizes a 2D variant of the sinc function, *sin*(*x*) / *x*

`perf`: tests the execution time bottleneck in redsho and helps
    to streamline it

`xgboost_regression`: optimizes an XGBoost regression models, across
a wide variety of hyperparameters and options

`xgboost_multiclass`: same as the previous example, but with a
multiclass classification problem

## Contributing

I hope that you will copy and paste liberally from these examples. Once
you have something working of your own that you would like to share,
please open a pull request on this repo. Put your example in its own
directory, with a short README telling a new user how to run it.

I want to showcase human-authored examples that teach and celebrate
the tinkering of others, so if your example is complex or comes with
a large code base or is obviously LLM-authored,
I'll encourage you to make a repo of your own for it. But I'm strongly
biased toward accepting submissions. The more examples folks have to work
from, the easier it is for them to get started.
