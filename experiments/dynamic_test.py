from src.grid import generate_grid
from src.dynamic import add_dynamic_obstacle, replan
from src.astar import get_path

grid = generate_grid(70, 0.2)
start = (0, 0)
goal = (69, 69)

for step in range(5):
    grid = add_dynamic_obstacle(grid)
    parent = replan(grid, start, goal)
    path = get_path(parent, goal)

    print(f"Step {step} - Path Length:", len(path))
