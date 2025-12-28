import heapq

def read_input(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    idx = 0
    rows, cols = map(int, lines[idx].split())
    idx += 1

    grid = []
    for _ in range(rows):
        grid.append(list(map(int, lines[idx].split())))
        idx += 1

    start = tuple(map(int, lines[idx].split()))
    idx += 1

    target = tuple(map(int, lines[idx].split()))

    return grid, start, target


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, target):
    rows, cols = len(grid), len(grid[0])

    # Priority queue: (f_cost, g_cost, node, path)
    pq = []
    heapq.heappush(pq, (manhattan(start, target), 0, start, [start]))

    visited = set()

    while pq:
        f, g, (r, c), path = heapq.heappop(pq)

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == target:
            return True, g, path

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 0 and (nr, nc) not in visited):

                new_g = g + 1
                new_f = new_g + manhattan((nr, nc), target)
                heapq.heappush(
                    pq,
                    (new_f, new_g, (nr, nc), path + [(nr, nc)])
                )

    return False, None, []


# ---------- MAIN ----------
filename = "input_a_star.txt"
grid, start, target = read_input(filename)

found, cost, path = a_star(grid, start, target)

if found:
    print(f"Path found with cost {cost} using A*")
    print("Shortest Path:", path)
else:
    print("Path not found using A*")
