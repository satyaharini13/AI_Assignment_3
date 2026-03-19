from src.astar import astar
import random

def add_dynamic_obstacle(grid):
    size = len(grid)
    x, y = random.randint(0, size-1), random.randint(0, size-1)
    grid[x][y] = 1
    return grid

def replan(grid, start, goal):
    return astar(grid, start, goal)
