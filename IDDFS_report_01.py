class IDDFS:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = start
        self.target = target
        self.R = len(grid)
        self.C = len(grid[0])
        self.goalFound = False
        self.traversal_order = []

    def iterative_deepening(self):
        max_depth = 0
        while not self.goalFound:
            visited = [[False]*self.C for _ in range(self.R)]
            path = []
            self.depth_limited_search(self.start[0], self.start[1], max_depth, 0, visited, path)
            if self.goalFound:
                print(f"Path found at depth {len(path)-1} using IDDFS")
                print("Traversal Order:", path)
                return
            max_depth += 1
            if max_depth > self.R * self.C: 
                print(f"Path not found at max depth {max_depth} using IDDFS")
                return

    def depth_limited_search(self, r, c, limit, depth, visited, path):
        if self.goalFound or depth > limit:
            return
        visited[r][c] = True
        path.append((r, c))

        if (r, c) == self.target:
            self.goalFound = True
            return

        directions = [(1,0), (-1,0), (0,1), (0,-1)] 
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.R and 0 <= nc < self.C and not visited[nr][nc] and self.grid[nr][nc] == 0:
                self.depth_limited_search(nr, nc, limit, depth + 1, visited, path)
                if self.goalFound:
                    return

        path.pop()
        visited[r][c] = False


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    idx = 0
    test_case_num = 1
    while idx < len(lines):
        R, C = map(int, lines[idx].split())
        idx += 1

        grid = []
        for _ in range(R):
            grid.append(list(map(int, lines[idx].split())))
            idx += 1

        start_line = lines[idx].replace("Start:","").strip()
        sr, sc = map(int, start_line.split())
        idx += 1

        target_line = lines[idx].replace("Target:","").strip()
        tr, tc = map(int, target_line.split())
        idx += 1

        print(f"\n--- Test Case {test_case_num} ---")
        iddfs = IDDFS(grid, (sr, sc), (tr, tc))
        iddfs.iterative_deepening()

        test_case_num += 1

if __name__ == "__main__":
    main()
