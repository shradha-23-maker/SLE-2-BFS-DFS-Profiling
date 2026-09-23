\# SLE-2: BFS and DFS Profiling



\## Course

02AML204 – Introduction to Artificial Intelligence



\## Student Details



\- \*\*Name:\*\* Shradha Dhananjay Kumbhar

\- \*\*PRN:\*\* 25UAM030

\- \*\*Division:\*\* A

\- \*\*Date:\*\* 22 September 2026



\## Objective



The objective of this SLE-2 task is to empirically compare the performance of Breadth-First Search (BFS) and Depth-First Search (DFS).



The comparison is based on:



\- Execution time

\- Number of nodes explored

\- Profiling using py-spy



\## Algorithms Used



\### 1. Breadth-First Search (BFS)



BFS explores the graph level by level using a queue.



Program:



`bfs.py`



\### 2. Depth-First Search (DFS)



DFS explores the graph by going as deep as possible before backtracking. It uses a stack.



Program:



`dfs.py`



\## Problem Used



Both algorithms were tested on the same 12-node graph.



\- Start node: `A`

\- Goal nodes: `A` to `L`

\- Number of nodes: 12



Using the same graph and goals makes the comparison fair.



\## Profiling Method



The following methods were used:



\- `timeit` for execution-time measurement

\- Manual node counting for nodes explored

\- `py-spy` for profiling and flame graphs

\- 1000 runs were used for timing each goal



\## Results



| Metric | BFS | DFS |

|---|---:|---:|

| Average Nodes Explored | 6.5 | 6.5 |

| Average Time | 2.1641 µs | 2.3998 µs |

| Worst-Case Time | 3.5306 µs | 4.2753 µs |

| py-spy Samples | 4 | 13 |

| py-spy Errors | 0 | 0 |



\## Observation



In this experiment, BFS recorded a lower average execution time than DFS.



Both algorithms explored the same average number of nodes: 6.5.



The measured result depends on the graph structure, node ordering, and system conditions.



\## Profiling Graphs



\### BFS Flame Graph



!\[BFS Profile](bfs\_profile.svg)



\### DFS Flame Graph



!\[DFS Profile](dfs\_profile.svg)



\## Files



\- `bfs.py` – BFS implementation and profiling

\- `dfs.py` – DFS implementation and profiling

\- `bfs\_profile.svg` – BFS py-spy flame graph

\- `dfs\_profile.svg` – DFS py-spy flame graph



\## AI Contribution



ChatGPT was used to understand the SLE-2 guideline, organize the profiling procedure, understand the BFS and DFS code and results, and prepare the report structure.



The programs were edited and executed locally, profiling experiments were performed, results were collected, py-spy flame graphs were generated, and the evidence was checked by the student.



\## Conclusion



BFS and DFS were implemented as separate programs and tested on the same 12-node graph. Execution time and nodes explored were measured, and py-spy was used to generate profiling flame graphs. In this experiment, BFS recorded a lower average execution time, while both algorithms explored the same average number of nodes.

