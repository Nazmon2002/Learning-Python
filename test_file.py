def read_test_cases(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    test_cases = []
    i = 0
    n = len(lines)

    while i < n:
        # ---- Read grid size safely ----
        if i >= n:
            break
        parts = lines[i].split()
        if len(parts) != 2:
            break
        rows, cols = map(int, parts)
        i += 1

        # ---- Read grid safely ----
        if i + rows > n:
            break
        grid = []
        for _ in range(rows):
            grid.append(list(map(int, lines[i].split())))
            i += 1

        # ---- Read start safely ----
        if i >= n or not lines[i].lower().startswith("start"):
            break
        start = tuple(map(int, lines[i].split(":")[1].split()))
        i += 1

        # ---- Read target safely ----
        if i >= n or not lines[i].lower().startswith("target"):
            break
        target = tuple(map(int, lines[i].split(":")[1].split()))
        i += 1

        test_cases.append((grid, start, target))

    return test_cases


def iddfs(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    max_depth = rows * cols

    def dfs(node, depth, path, visited):
        if depth < 0:
            return False

        if node == target:
            path.append(node)
            return True

        r, c = node
        visited.add(node)
        path.append(node)

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 0 and (nr, nc) not in visited):
                if dfs((nr, nc), depth - 1, path, visited):
                    return True

        path.pop()
        visited.remove(node)
        return False

    for depth in range(max_depth + 1):
        path = []
        visited = set()
        if dfs(start, depth, path, visited):
            return True, depth, path

    return False, max_depth, []


# ---------- MAIN ----------
filename = "input_iddfs.txt"
test_cases = read_test_cases(filename)

for idx, (grid, start, target) in enumerate(test_cases, start=1):
    found, depth, path = iddfs(grid, start, target)

    print(f"Case #{idx}:")
    if found:
        print(f"Path found at depth {depth} using IDDFS")
        print("Traversal Order:", path)
    else:
        print(f"Path not found at max depth {depth} using IDDFS")
    print()
