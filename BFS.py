from collections import deque
import random

class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level

class BFS:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.found = False
        self.goal_level = 0
        self.N = 0
        self.source = None
        self.goal = None

    def init(self):
        N = int(input("Enter grid size N: "))
        graph = [[1 if random.random() > 0.3 else 0 for _ in range(N)] for _ in range(N)]
        print("\nGenerated Grid (1 = free, 0 = obstacle):")
        for row in graph:
            print(" ".join(str(cell) for cell in row))
        self.N = N

        # Input validation for start position
        while True:
            try:
                source_input = input("\nEnter start position (row col): ").split()
                if len(source_input) != 2:
                    raise ValueError("Enter exactly 2 numbers separated by space")
                source_x, source_y = map(int, source_input)
                if not (0 <= source_x < N and 0 <= source_y < N):
                    raise ValueError("Position out of grid bounds")
                if graph[source_x][source_y] == 0:
                    raise ValueError("Start position is on an obstacle")
                break
            except ValueError as e:
                print("Invalid input:", e)

        # Input validation for goal position
        while True:
            try:
                goal_input = input("Enter goal position (row col): ").split()
                if len(goal_input) != 2:
                    raise ValueError("Enter exactly 2 numbers separated by space")
                goal_x, goal_y = map(int, goal_input)
                if not (0 <= goal_x < N and 0 <= goal_y < N):
                    raise ValueError("Position out of grid bounds")
                if graph[goal_x][goal_y] == 0:
                    raise ValueError("Goal position is on an obstacle")
                break
            except ValueError as e:
                print("Invalid input:", e)

        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, 0)

        self.st_bfs(graph)

        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_level)
        else:
            print("Goal cannot be reached from starting block")

    def st_bfs(self, graph):
        queue = deque()
        visited = [[False]*self.N for _ in range(self.N)]
        queue.append(self.source)
        visited[self.source.x][self.source.y] = True

        while queue:
            u = queue.popleft()
            for dx, dy in self.directions:
                v_x, v_y = u.x + dx, u.y + dy
                if 0 <= v_x < self.N and 0 <= v_y < self.N and not visited[v_x][v_y] and graph[v_x][v_y] == 1:
                    v_level = u.level + 1
                    if v_x == self.goal.x and v_y == self.goal.y:
                        self.found = True
                        self.goal_level = v_level
                        return
                    visited[v_x][v_y] = True
                    queue.append(Node(v_x, v_y, v_level))

if __name__ == "__main__":
    bfs = BFS()
    bfs.init()
