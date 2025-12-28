import heapq
import random

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, target):
    R, C = len(grid), len(grid[0])

    pq = []
    heapq.heappush(pq, (heuristic(start, target), 0, start))

    parent = dict()
    g_cost = {start: 0}
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        F, G, current = heapq.heappop(pq)

        if current == target:
            path = []
            node = current
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            return G, path

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            nxt = (nr, nc)

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                new_g = G + 1
                new_f = new_g + heuristic(nxt, target)
                
                if nxt not in g_cost or new_g < g_cost[nxt]:
                    g_cost[nxt] = new_g
                    parent[nxt] = current
                    heapq.heappush(pq, (new_f, new_g, nxt))

    return None, None  

def generate_random_grid(R, C, obstacle_prob=0.2):
    """Generate a random R x C grid with obstacles"""
    grid = [[0 if random.random() > obstacle_prob else 1 for _ in range(C)] for _ in range(R)]
    return grid

def main():
    R, C = 10, 10  
    grid = generate_random_grid(R, C, obstacle_prob=0.2)

    empty_cells = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 0]
    start = random.choice(empty_cells)
    target = random.choice(empty_cells)

    print("--- Random Grid ---")
    for row in grid:
        print(row)
    print(f"Start: {start}, Target: {target}")

    cost, path = a_star_search(grid, start, target)

    if path is None:
        print("Path not found using A*")
    else:
        print(f"Path found with cost {cost} using A*")
        print("Shortest Path:", path)

if __name__ == "__main__":
    main()
