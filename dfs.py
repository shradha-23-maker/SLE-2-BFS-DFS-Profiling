import timeit

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": ["K"],
    "H": ["L"],
    "I": ["L"],
    "J": ["L"],
    "K": ["L"],
    "L": []
}


def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_explored = 0

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            nodes_explored += 1

            if node == goal:
                return nodes_explored

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return nodes_explored


start = "A"
goals = list(graph.keys())

results = []

for goal in goals:
    total_time = timeit.timeit(
        lambda: dfs(start, goal),
        number=1000
    )

    nodes = dfs(start, goal)
    average_time = total_time / 1000

    results.append((goal, nodes, average_time))


best = min(results, key=lambda x: x[1])
worst = max(results, key=lambda x: x[1])

average_nodes = sum(x[1] for x in results) / len(results)
average_time = sum(x[2] for x in results) / len(results)


print("======================================")
print("             DFS PROFILING")
print("======================================")

print("\nBest Case")
print("Goal:", best[0])
print("Nodes Explored:", best[1])
print("Time:", best[2] * 1_000_000, "microseconds")

print("\nAverage Case")
print("Average Nodes:", average_nodes)
print("Average Time:", average_time * 1_000_000, "microseconds")

print("\nWorst Case")
print("Goal:", worst[0])
print("Nodes Explored:", worst[1])
print("Time:", worst[2] * 1_000_000, "microseconds")