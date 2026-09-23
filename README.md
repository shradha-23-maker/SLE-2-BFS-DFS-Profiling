# Algorithmic Profiling: BFS vs. DFS Search

An empirical profiling project comparing Breadth-First Search (BFS) and Depth-First Search (DFS) using execution time, nodes explored, `timeit`, and `py-spy`.

---

## 📌 Overview

- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **Author:** Shradha Dhananjay Kumbhar (PRN: 25UAM030)
- **Problem Domain:** Graph search
- **Graph Size:** 12 nodes
- **Start Node:** A
- **Search Algorithms:** BFS and DFS
- **Profiling Tools:** `timeit` and `py-spy`

Both algorithms were implemented as separate Python programs and tested on the same graph and set of goal nodes.

---

## 📊 Performance Comparison

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time | 2.1641 µs | 2.3998 µs |
| Average Nodes Explored | 6.5 | 6.5 |
| Worst-Case Time | 3.5306 µs | 4.2753 µs |
| py-spy Samples | 4 | 13 |
| py-spy Errors | 0 | 0 |

### Key Observations

- BFS recorded a lower average measured execution time than DFS in this experiment.
- Both algorithms explored the same average number of nodes: **6.5**.
- BFS also recorded a lower measured worst-case time in this experiment.
- The measured execution time is specific to this graph, implementation, and system environment.
- The results should not be treated as a universal statement that BFS is always faster than DFS.
- `py-spy` was used to generate flame graphs showing sampled CPU execution activity.

---

## 🚀 How to Run

### 1. Install py-spy

```text
pip install py-spy

2. Run BFS
python bfs.py
3. Profile BFS
py-spy record -o bfs_profile.svg -- python bfs.py
4. Run DFS
python dfs.py
5. Profile DFS
py-spy record -o dfs_profile.svg -- python dfs.py
6. View the Flame Graphs

Open the following SVG files in a web browser:

bfs_profile.svg
dfs_profile.svg
📁 Repository Contents
bfs.py — BFS implementation with execution-time and node-count measurement.
dfs.py — DFS implementation with execution-time and node-count measurement.
bfs_profile.svg — py-spy profiling output for BFS.
dfs_profile.svg — py-spy profiling output for DFS.
contribution_log.md — Contribution and AI usage log.
README.md — Project documentation.
🤖 AI Contribution

ChatGPT was used to understand the SLE-2 requirements, organize the profiling procedure, explain the BFS and DFS programs, interpret the collected results, and prepare the documentation.

The programs were edited and executed locally. The profiling experiments were performed, results were collected, the py-spy flame graphs were generated, and the final evidence was checked by the student.

📝 Conclusion

BFS and DFS were implemented as separate programs and evaluated on the same 12-node graph. Execution time and the number of explored nodes were measured using the same experimental setup.

For this particular experiment, BFS recorded a lower average measured execution time than DFS, while both algorithms explored the same average number of nodes. The results provide an empirical comparison of BFS and DFS under the selected test conditions.