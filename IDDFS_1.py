import random

class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.numberOfNodes = 0
        self.depth = 0
        self.maxDepth = 0
        self.goalFound = False

    def iterativeDeepening(self, adjacencyMatrix, Source, destination):
        self.numberOfNodes = len(adjacencyMatrix) - 1
        while not self.goalFound:
            self.depthLimitedSearch(adjacencyMatrix, Source, destination)
            self.maxDepth += 1
            if self.goalFound:
                print("\nGoal Found at depth", self.depth)
                return
            self.depth = 0
            self.stack = []

    def depthLimitedSearch(self, adjacencyMatrix, Source, goal):
        visited = [0] * (self.numberOfNodes + 1)
        self.stack.append(Source)
        print("\nAt Depth", self.maxDepth)
        print('\n', Source, end='\t')

        while self.stack:
            element = self.stack[-1]
            found = False
            for destination in range(1, self.numberOfNodes + 1):
                if self.depth < self.maxDepth:
                    if adjacencyMatrix[element][destination] == 1 and visited[destination] == 0:
                        visited[destination] = 1
                        self.depth += 1
                        self.stack.append(destination)
                        print(destination, end='\t')
                        if destination == goal:
                            self.goalFound = True
                            return
                        found = True
                        break

            if not found:
                self.stack.pop()
                self.depth -= 1


if __name__ == "__main__":
    try:
        print("Enter the number of nodes in the graph\n")
        number_of_nodes = int(input().strip())

        adjacency_matrix = [[0] * (number_of_nodes + 1) for _ in range(number_of_nodes + 1)]

        for i in range(1, number_of_nodes + 1):
            for j in range(1, number_of_nodes + 1):
                if i != j:
                    adjacency_matrix[i][j] = random.choice([0, 1])
                else:
                    adjacency_matrix[i][j] = 0

        print("\nRandomly Generated Adjacency Matrix:")
        for row in adjacency_matrix[1:]:
            print(row[1:])

        print("\nEnter the Source for the graph\n")
        Source = int(input().strip())
    

        print("\nEnter the destination for the graph\n")
        destination = int(input().strip())

        iterativeDeepening = IterativeDeepening()
        iterativeDeepening.iterativeDeepening(adjacency_matrix,Source, destination)

    except ValueError:
        print("Wrong Input format")
