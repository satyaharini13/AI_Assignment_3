import random

def generate_grid(size, density):
    return [[1 if random.random() < density else 0 for _ in range(size)] for _ in range(size)]
