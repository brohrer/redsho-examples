import time

from redsho.optimizer import optimize


def toy_evaluate(*, a, b, c, d, e, f):
    return (a + b) * (c - d) ** e % f


values = {
    "a": [4, 7, 9, 14, 20],
    "b": [2, 5, 6, 9.9, 18, 92],
    "c": [5, 8, 11, 13, 14, 15],
    "d": [0.43, 0.001, -0.83, 1.005, 67.2],
    "e": [2, 3, 4, 5],
    "f": [21, 23, 27, 583, 3714],
}

start = time.time()
optimize(values, toy_evaluate, n_iter=int(1e2), verbose=False)
elapsed = time.time() - start

# Find the number of conditions tried
results_file = "reports/optimizer_results.csv"
with open(results_file, "rt") as f:
    rows = f.readlines()

n_rows = len(list(rows)) - 1

time_per_condition = elapsed / n_rows

print(f"{int(time_per_condition * 1e6)} \u03bcs per iteration")

start = time.time()
optimize(values, toy_evaluate, n_iter=int(1e3), verbose=False, update_plots=False)
elapsed = time.time() - start

# Find the number of conditions tried
results_file = "reports/optimizer_results.csv"
with open(results_file, "rt") as f:
    rows = f.readlines()

n_rows = len(list(rows)) - 1

time_per_condition = elapsed / n_rows

print("Results plot and csv are not updated after each iteration.")
print(f"{int(time_per_condition * 1e6)} \u03bcs per iteration")
