import csv
import os

import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend("agg")   # noqa: F401
from matplotlib import cm

module_path = os.path.dirname(__file__)
reports_dir = "reports"
reports_dir = os.path.join(module_path, "reports")
results_logfile = os.path.join(reports_dir, "optimizer_results.csv")
visualization_path = os.path.join(reports_dir, "visualization.png")


def main():
    """
    The error is multiplied by -1 here, so that it looks like the
    algorithm is trying to climb the mountain, rather than find its
    way to the bottom of a well. It's easier to visualize well and
    a bit more cheerful.
    """
    results = csv_to_condition_list(results_logfile)
    x = []
    y = []
    z = []
    best_so_far = []
    bsf = 1e-10
    for result in results:
        x.append(float(result["x"]))
        y.append(float(result["y"]))
        zval = -1 * float(result["error"])
        z.append(zval)
        bsf = max(bsf, zval)
        best_so_far.append(bsf)

    fig = plt.figure()

    # The upper left plot shows a 3D surface of the objective function.
    ax_surf = fig.add_subplot(221, projection="3d")
    x_all_hi = np.linspace(0, np.pi, 100)
    y_all_hi = np.linspace(0, np.pi, 100)
    X, Y = np.meshgrid(x_all_hi, y_all_hi)
    n_rows, n_cols = X.shape
    Z = np.zeros((n_rows, n_cols))
    for i in range(n_rows):
        for j in range(n_cols):
            Z[i, j] = -1 * evaluate({"x": X[i, j], "y": Y[i, j]})

    ax_surf.plot_surface(
        X, Y, Z, cmap=cm.inferno, linewidth=0, antialiased=False
    )
    ax_surf.set_xlabel("x")
    ax_surf.set_ylabel("y")
    ax_surf.set_xlim(0, np.pi)
    ax_surf.set_ylim(0, np.pi)
    ax_surf.set_zlim(-0.2, 1)

    # The upper right plot shows a 3D representation of the points
    # in the search space that were evaluated.
    ax_eval = fig.add_subplot(222, projection="3d")
    ax_eval.scatter(
        x,
        y,
        z,
        c=z,
        cmap=cm.inferno,
        vmax=1,
        vmin=-0.2,
        s=10,
    )

    for i in range(len(x)):
        ax_eval.plot(
            [x[i], x[i]],
            [y[i], y[i]],
            [z[i], 0],
            linewidth=0.5,
            color="blue",
        )
    ax_eval.set_xlabel("x")
    ax_eval.set_ylabel("y")
    ax_eval.set_xlim(0, np.pi)
    ax_eval.set_ylim(0, np.pi)
    ax_eval.set_zlim(-0.2, 1)

    # The lower left function shows the best error score found so far as
    # more points are evaluated.
    ax_bsf = fig.add_subplot(223)
    ax_bsf.plot(
        np.arange(len(best_so_far)) + 1,
        best_so_far,
        color="blue",
    )
    ax_bsf.set_xlabel("Points evaluated")
    ax_bsf.set_ylabel("Best value so far")
    ax_bsf.set_xlim(0, len(best_so_far) + 1)
    ax_bsf.set_ylim(-0.01, 1.01)

    # A 2D version of the plot in the upper right, showing the points
    # evaluated so far and the error associated with them.
    ax_cover = fig.add_subplot(224)
    ax_cover.scatter(
        x,
        y,
        c=z,
        vmax=1,
        vmin=-0.2,
        cmap=cm.inferno,
        s=20,
    )
    ax_cover.set_xlabel("x")
    ax_cover.set_ylabel("y")
    ax_cover.set_xlim(-0.1, np.pi + 0.1)
    ax_cover.set_ylim(-0.1, np.pi + 0.1)

    fig.savefig(visualization_path, dpi=300)
    plt.close()

    print(f"There's a 3D visualization of it in {visualization_path}.")


def evaluate(args):
    """
    The objective function is a 2D variant of the sinc function.
    """
    x0 = 1
    y0 = 1.5
    return -np.sinc(args["x"] - x0) * np.sinc(args["y"] - y0)


def csv_to_condition_list(csv_filename):
    with open(csv_filename, "rt") as csv_file:
        dict_reader = csv.DictReader(csv_file)
        return list(dict_reader)


if __name__ == "__main__":
    main()
