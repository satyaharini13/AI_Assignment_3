from src.dijkstra import dijkstra, get_path
import json

with open("data/india_cities_graph.json") as f:
    graph = json.load(f)

dist, parent = dijkstra(graph, "Delhi")

print("Path:", get_path(parent, "Chennai"))
print("Distance:", dist["Chennai"])
