import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        for d in directions:
            neighbor = (current[0]+d[0], current[1]+d[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    parent[neighbor] = current

    return parent


def get_path(parent, goal):
    path = []
    while goal:
        path.append(goal)
        goal = parent.get(goal)
    return path[::-1]
