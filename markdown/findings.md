## Empirical Synthesis: 
We created visualizations using our benchmarking data. These visualizations show that our algorithm scales more slowly than the $O(n^2)$ baseline, demonstrating improved performance as the input size increases.

| ![Benchmark Plot (Linear Scale)](Figure_1.png) | ![Benchmark Plot (Log Scale)](Figure_2.png) |
|---|---|

## Baseline Comparison: 
Our algorithmic analysis shows that our solution scales more slowly than the baseline, visually demonstrating an improvement in runtime. This comparison shows how choosing a more efficient mathematical approach can improve an algorithm's performance compared with testing every possible solution.


## Reflection: 
Write a reflection on your team’s design and debugging process. Discuss any two-stage submission improvements made from earlier weeks. Be specific about your challenges: detail specific structural pivots your team had to make, or debugging moments that led to critical breakthroughs

The main challenge we had was fining an alogirthem that was slower scaling then our baseline. As our oringal propoused alogrithem had the same scaling as our baseline. The structral pivoit we had to make was changing to use heaps. The debugging process included ensuring the function returned the correct result. We ensured this by working out the correct answer on paper before running the same input into the alogirthem. Some improvements we impliemeted from feedback from privous eariler weeks were ensuring our markdown files were formatted corrected and could display our graphs, and implimenting pytest functions to ensure the alogrithem returns the correct answer.