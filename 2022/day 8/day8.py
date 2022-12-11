import numpy as np

with open("./input.csv") as file:
    data = file.read().splitlines()

for i, row in enumerate(data):
    data[i] = list(row)

grid = np.array(data, int)

# part 1
seen = set()

def look_left(index, grid):
    x, y = index
    if y == 0:
        return True
    else:
        return all([value < grid[index] for value in grid[x, :y]])

def look_right(index, grid):
    x, y = index
    if y == grid.shape[1]:
        return True
    else:
        return all([value < grid[index] for value in grid[x, y+1:]])

def look_up(index, grid):
    x, y = index
    if x == 0:
        return True
    else:
        return all([value < grid[index] for value in grid[:x, y]])

def look_down(index, grid):
    x, y = index
    if x == grid.shape[0]:
        return True
    else:
        return all([value < grid[index] for value in grid[(x+1):, y]])

for index in np.ndindex(grid.shape):
    if look_left(index, grid):
        seen.add(index)
    if look_right(index, grid):
        seen.add(index)
    if look_up(index, grid):
        seen.add(index)
    if look_down(index, grid):
        seen.add(index)

print(len(seen))

