# Empirical Evaluation

## Overview
We implemented our two algorithms (`main.py`) that solve the file merging problem:
1.  **Baseline Algorithm:** A naive greedy approach that repeatedly finds the minmum elements before adding them and reinserting them into the array. 
2.  **Proposed Algorithm:** An optimized greedy approach that uses a heap, then adds and insert the computed value bak into the heap.

Unit testing (`main.py`) confirms that both algorithms return the correct minimum computing cost as they were printed out the same result..

## Benchmarking Results
We compare the performance of our two algorithms on randomly generated arrays, with varying input size ($n$) from 10 to 50,000 files, with each file being between 1 and 1000 We present the results in the plots below. The left plot shows the execution time on a linear scale, while the right plot uses a logarithmic scale for both axes.

| ![Benchmark Plot (Linear Scale)](benchmark_plot.png) | ![Benchmark Plot (Log Scale)](benchmark_plot_log.png) |
|---|---|

The empirical data aligns with our theoretical complexity analysis (`planning.md`):

*   **Baseline Quadratic Scaling:** The baseline algorithm theoretically scales at $\mathcal{O}(n^2)$ due to repeatedly scanning the remaining list for the smallest element.
*   **Proposed Algorithm Efficiency:** The proposed algorithm scales at $\mathcal{O}(n \log n)$, constrained almost entirely by the heaps. Our algorithem takes just 0.05 seconds. At $n = 6400$, the proposed algorithm is several orders of magnitude faster than the baseline. 