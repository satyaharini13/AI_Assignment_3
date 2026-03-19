import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            cost = current_cost + weight

            if cost < distances[neighbor]:
                distances[neighbor] = cost
                parent[neighbor] = current_node
                heapq.heappush(pq, (cost, neighbor))

    return distances, parent


def get_path(parent, goal):
    path = []
    while goal:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]
