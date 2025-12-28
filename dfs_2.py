def read_multiple_test_cases(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    test_cases = []
    i = 0
    n = len(lines)

    while i < n:
        # ✅ Ensure grid size line exists
        if i >= n:
            break

        rows_cols = lines[i].split()
        if len(rows_cols) != 2:
            break

        rows, cols = map(int, rows_cols)
        i += 1

        # ✅ Ensure enough grid rows exist
        if i + rows > n:
            break

        grid = []
        for _ in range(rows):
            grid.append(list(map(int, lines[i].split())))
            i += 1

        # ✅ Ensure target line exists
        if i >= n or "target" not in lines[i].lower():
            break

        target = int(lines[i].split(":")[1].strip())
        i += 1

        test_cases.append((grid, target))

    return test_cases


def find_path_with_target_sum(grid, target):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    path = []

    def dfs(r, c, current_sum):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
            return False

        current_sum += grid[r][c]
        path.append((r, c))
        visited[r][c] = True

        if current_sum == target:
            return True

        # right, down, left, up
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            if dfs(r + dr, c + dc, current_sum):
                return True

        visited[r][c] = False
        path.pop()
        return False

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True, path

    return False, []


# -------- Main Program --------
filename = "input_dfs.txt"
test_cases = read_multiple_test_cases(filename)

for idx, (grid, target) in enumerate(test_cases, start=1):
    found, path = find_path_with_target_sum(grid, target)
    print(f"Case #{idx}:")
    if found:
        print("Path found")
        print("DFS Traversal Order:", path)
    else:
        print("Path not found")
    print()
