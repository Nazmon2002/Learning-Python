import random

class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self):
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_depth = None

    def init(self):
        self.N = int(input("Enter grid size N: "))
        grid = [[1 if random.random() > 0.3 else 0 for _ in range(self.N)] for _ in range(self.N)]
        print("\nGenerated Grid (1 = free, 0 = obstacle):")
        for row in grid:
            print(" ".join(str(cell) for cell in row))

        sx, sy = map(int, input("\nEnter start position (row col): ").split())
        gx, gy = map(int, input("Enter goal position (row col): ").split())

        if grid[sx][sy] == 0 or grid[gx][gy] == 0:
            print("Start or goal is on an obstacle. Please rerun and try again.")
            return

        self.source = Node(sx, sy, 0)
        self.goal = Node(gx, gy, 999999)
        self.st_dfs(grid, self.source)

        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_depth)
        else:
            print("Goal cannot be reached from the starting block")

    def print_direction(self, direction, x, y):
        if direction == 0:
            print("Moving Down ({}, {})".format(x, y))
        elif direction == 1:
            print("Moving Up ({}, {})".format(x, y))
        elif direction == 2:
            print("Moving Right ({}, {})".format(x, y))
        else:
            print("Moving Left ({}, {})".format(x, y))

    def st_dfs(self, grid, node):
        grid[node.x][node.y] = 0
        for i in range(4):
            nx = node.x + self.x_move[i]
            ny = node.y + self.y_move[i]
            if 0 <= nx < self.N and 0 <= ny < self.N and grid[nx][ny] == 1:
                depth = node.depth + 1
                self.print_direction(i, nx, ny)
                if nx == self.goal.x and ny == self.goal.y:
                    self.found = True
                    self.goal_depth = depth
                    return
                child = Node(nx, ny, depth)
                self.st_dfs(grid, child)
                if self.found:
                    return

def main():
    dfs = DFS()
    dfs.init()

if __name__ == "__main__":
    main()
