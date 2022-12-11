import numpy as np

with open("./input.csv") as file:
    data = file.read().splitlines()

for i, row in enumerate(data):
    data[i] = list(row)

grid = np.array(data, int)

def look_left(index, grid):
    x, y = index
    current = grid[index]
    count = 1
    if y == 0:
        return 0
    else:
        value = grid[x, y-1]
        while (value < current) and (y-count > 0):
            count += 1
            value = grid[x, y-count]
        return count

def look_right(index, grid):
    x, y = index
    current = grid[index]
    count = 1
    if y == grid.shape[1]-1:
        return 0
    else:
        value = grid[x, y+1]
        while (value < current) and (y+count != grid.shape[1]-1):
            count += 1
            value = grid[x, y+count]
        return count

def look_up(index, grid):
    x, y = index
    current = grid[index]
    count = 1
    if x == 0:
        return 0
    else:
        value = grid[x-1, y]
        while (value < current) and (x-count > 0):
            count += 1
            value = grid[x-count, y]
        return count

def look_down(index, grid):
    x, y = index
    current = grid[index]
    count = 1
    if x == grid.shape[0]-1:
        return 0
    else:
        value = grid[x+1, y]
        while (value < current) and (x+count != grid.shape[0]-1):
            count += 1
            value = grid[x+count, y]
        return count


score = {}
for index in np.ndindex(grid.shape):
    left_count = look_left(index, grid)
    right_count = look_right(index, grid)
    up_count = look_up(index, grid)
    down_count = look_down(index, grid)
    score[index] = left_count * right_count * up_count * down_count

print((max(score, key=score.get), score[max(score, key=score.get)]))