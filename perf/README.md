# Performance

This example is specifically designed to see which parts of redsho take
the most computation time and whether they are slow enough to merit
further streamlining.

## Timing

In `run.py`, a lightweight computation with 6 parameters is used as a
way to generate rapid iterations and ensure that most of the computation
time is due to redsho operations. Assigning 5 possible values to each
parameter gives over 15 thousand permutations and ensures that there
will be enough iterations to allow for accurate measurement.

Measuring the elapsed time for the loop and specifying the number of
iterations lets it find a time per iteration.

On my machine, this initial run takes about 55 ms per iteration.

## Finding what's slowing it down

While the loop is spinning madly, we can profile it in a separate console
using `py-spy`. Install globally with

```bash
python3 -m pip install py-spy
```

then as the optimization is running, find its process ID with

```bash
ps -a
```

There will be a line toward the bottom of the list that looks something like

```bash
38758 ttys005 0:03.81 /Users/brohrer/redsho-examples/perf/.venv/bin/python3 run.py
```

The leading "38758" is the process ID. Kick off the profiling with

```bash
sudo py-spy top --pid 38758
```

This generates a list of functions in a `top`-like profiling view.
The `3` key sorts by "OwnTime" and the `4` key sorts by "TotalTime".
The "TotalTime" column shows how much wall clock time each function
is taking *including* all of the other functions it calls.
The "OwnTime" column shows how much wall clock time the function is taking
*excluding* all those pother function calls. "OwnTime" shows where
the expensive functions are, and "TotalTime" shows which higher level
function called them.

In this run, `_encode_tile`, part of `PIL` (the Python Image Library) is
one of the worst offenders according to "OwnTime",
followed closely by `deepcopy` and 
`writerows`.

![py-spy profiling of slow version of redshow, functions sorted by owntime
](img/own_time_slow.png)

Looking at the TotalTime, it appears that calls to
variants of `draw` and `save` and other references to `Matplotlib` are
slowing things down the most.

![py-spy profiling of slow version of redshow, functions sorted by totaltime
](img/total_time_slow.png)

In this test, the results plot is re-drawn from scratch after each iteration.
In addition the entire iteration history is re-generated after each
iteration, calling the (apparently expensive) `deepcopy` on every row.
Not only is this slow, but it gets slower the longer it runs and eventually
overtakes plotting as the bottleneck.

## Toggle off per-iteration reports

To test this hypothesis, I compared against a run with the per-iteration
plotting and csv-writing turned off. Sadly it ran too quickly to measure,
so I increased the number of iterations and ran it again.

The "OwnTime" view shows that `deepcopy` is still the worst offender.

![py-spy profiling of fast version of redshow, functions sorted by owntime
](img/own_time_fast.png)

The "TotalTime" views shows that 
even though the code is no longer writing csv's every iteration,
copying is still involved in exploring new conditions to try.

![py-spy profiling of fast version of redshow, functions sorted by totaltime
](img/total_time_fast.png)

This suggests that if I wanted to speed it up further, the place to focus
would be substituting those `deepcopy` calls for something snappier.
However, stepping back and looking at the bigger picture, the time
per iteration after turning off incremental reporting plummted by more than
50 times, down to under a millisecond. Good enough for me!

## Implications

Redsho was built to walk the trade-off between sample efficiency and
robustness, not greedily seeking out the nearest peak, while also not
blindly searching through every possibility. This is a useful approach
when working with an expensive evaluation function, for instance,
training and testing a machine learning model. Any task of that magnitude
would dwarf the tiny expense of re-generating a plot and csv at each
iteration, and those incremental updates can help a human observer
decide to terminate the optimization loop early if it becomes clear that
a good enough solution has been found or that additional progress is unlikely.
For most use cases, keeping the per-iteration reports is the right call.

But for the odd duck use cases out there where computation is light
and the number of iterations is huge, I'll leave the option for
toggling off the incremental reports as an input argument `update_plots`.
