from src.grid import generate_grid
from src.astar import astar, get_path
import time

densities = [0.1, 0.25, 0.4]

for d in densities:
    grid = generate_grid(70, d)
    start = (0, 0)
    goal = (69, 69)

    t1 = time.time()
    parent = astar(grid, start, goal)
    t2 = time.time()

    path = get_path(parent, goal)

    print("\nDensity:", d)
    print("Path Length:", len(path))
    print("Time:", t2 - t1)
