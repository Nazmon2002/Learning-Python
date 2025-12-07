import heapq


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


def main():
    with open("input.txt", "r") as f:
        content = f.read().split()  

    content = list(map(int, content))
    idx = 0
    test_case_num = 1

    while idx < len(content):
        R, C = content[idx], content[idx+1]
        idx += 2

        grid = []
        for _ in range(R):
            row = content[idx:idx+C]
            grid.append(row)
            idx += C

        sr, sc = content[idx], content[idx+1]
        idx += 2
        tr, tc = content[idx], content[idx+1]
        idx += 2

        start = (sr, sc)
        target = (tr, tc)

        print(f"\n--- Test Case {test_case_num} ---")
        cost, path = a_star_search(grid, start, target)

        if path is None:
            print("Path not found using A*")
        else:
            print(f"Path found with cost {cost} using A*")
            print("Shortest Path:", path)

        test_case_num += 1

if __name__ == "__main__":
    main()
