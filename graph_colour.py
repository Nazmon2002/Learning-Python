def read_graph_from_file(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    idx = 0
    N, M, K = map(int, lines[idx].split())
    idx += 1

    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, lines[idx].split())
        idx += 1
        graph[u].append(v)
        graph[v].append(u)

    return N, M, K, graph


def is_safe(vertex, color, colors, graph):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True


def graph_coloring_util(vertex, N, K, colors, graph):
    if vertex == N:
        return True

    for color in range(1, K + 1):
        if is_safe(vertex, color, colors, graph):
            colors[vertex] = color
            if graph_coloring_util(vertex + 1, N, K, colors, graph):
                return True
            colors[vertex] = 0  # Backtrack

    return False


def graph_coloring(N, K, graph):
    colors = [0] * N
    if graph_coloring_util(0, N, K, colors, graph):
        return True, colors
    return False, []


# -------- MAIN --------
filename = "input_gc.txt"
N, M, K, graph = read_graph_from_file(filename)

possible, color_assignment = graph_coloring(N, K, graph)

if possible:
    print(f"Coloring Possible with {K} Colors")
    print("Color Assignment:", color_assignment)
else:
    print(f"Coloring Not Possible with {K} Colors")
