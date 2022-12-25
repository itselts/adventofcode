# Part 2
y_max = 0
for coord in grid.keys():
    if coord[1] > y_max:
        y_max = coord[1]

y_max += 2