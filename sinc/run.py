import matplotlib.pyplot as plt
import numpy as np

from redsho.optimizer import optimize
from visualize import main as visualize_run


def main():
    # Define your conditions - your discrete search space - by creating
    # a dictionary of key, value pairs
    # where each key is a parameter name, and each value
    # is the list of values that parameter can take.
    # Those values can be any object: numbers or strings, lists or dicts,
    # even functions of classes.
    condition_grid = {
        "x": list(np.linspace(0, np.pi, 10)),
        "y": list(np.linspace(0, np.pi, 10)),
    }

    # Choose your optimization algorithm and run its optimize() method.
    _, _ = optimize(condition_grid, evaluate)

    visualize_run()


def evaluate(x=0, y=0):
    """
    The objective function is a 2D variant of the sinc function.
    """
    x0 = 1
    y0 = 1.5
    return -np.sinc(x - x0) * np.sinc(y - y0)


if __name__ == "__main__":
    main()
