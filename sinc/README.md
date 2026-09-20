# Example: Finding the maximum of *sinc* function

![Animated demo of Redsho in operation on a 2D variant of the sinc function
](splash.gif?raw=true)

The [sinc function](https://en.wikipedia.org/wiki/Sinc_function)
(*sin*(*x*) / *x*) is a fun
optimization challenge because it has a clear global maximum, but many
local maxima, which can trick naive optimizers.


![Two dimensional sinc function
](https://raw.githubusercontent.com/brohrer/blog_images/refs/heads/main/evopowell/two_d_sinc.png)

This is a two-dimensional variant

*z* = (*sin*(*x*) / *x*) * (*sin*(*y*) / *y*)

Run with

```python3
uv run run.py
```

This generates a progress plot in `reports/optimizer_results.png`
showing how the best-so-far error evolves as more
parameter combinations are tried.

![Animated demo of Redsho in operation on a 2D variant of the sinc function
](typical_results.png)

Running it several times gives you a sense of how rapidly the optimizer
converges. Due to randomness, sometimes it lucks into the best solution
quickly, and sometimes it takes a little longer.

The history of parameter combinations tried is reported in
`reports/optimizer_reports.csv`. This allows you to do follow up
visualizations and explorations if you wish.

And for a flourish, there is also a multi-panel visualization of the
run, including a rendering of the evaluation function and illustration
of the locations that were tried in `reports/visualization.png`.

![Fancier visualization of the completed run
](typical_visualization.png)

