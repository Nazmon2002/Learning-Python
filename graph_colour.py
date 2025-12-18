def is_safe(vertex, graph, color, c):
    for adj in graph[vertex]:
        if color[adj] == c:
            return False
    return True


def graph_coloring_util(vertex, graph, color, n, k):
    if vertex == n:
        return True

    for c in range(1, k + 1):
        if is_safe(vertex, graph, color, c):
            color[vertex] = c
            if graph_coloring_util(vertex + 1, graph, color, n, k):
                return True
            color[vertex] = 0 

    return False


def solve_two_cases(filename):
    with open(filename, "r") as file:
        case_no = 1

        while True:
            line = file.readline().strip()
            if not line:
                break  

            n, m, k = map(int, line.split())
            graph = [[] for _ in range(n)]

            for _ in range(m):
                u, v = map(int, file.readline().split())
                graph[u].append(v)
                graph[v].append(u)

            color = [0] * n

            print(f"Case #{case_no}:")
            if graph_coloring_util(0, graph, color, n, k):
                print(f"Coloring Possible with {k} Colors")
                print("Color Assignment:", color)
            else:
                print(f"Coloring Not Possible with {k} Colors")
            print()

            case_no += 1


solve_two_cases("input1.txt")
