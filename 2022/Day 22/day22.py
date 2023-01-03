import re
from collections import deque

f = "input"

map = {}
for r, line in enumerate(open(f"./{f}.csv").read().splitlines()):
    if line == "":
        break
    for c, x in enumerate(line):
        map[(r,c)] = x

dirs = deque(re.split('([\d]+)', open(f"./{f}.csv").read().splitlines()[-1]))

cycle = ["E", "S", "W", "N"]
rmax = max(coord[0] for coord in map.keys())
cmax = max(coord[1] for coord in map.keys())

cur, orient = (min([k for k,v in map.items() if v in ['.', '#']]), "E")

print((rmax, cmax))

while dirs:
    x, y = cur
    column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
    row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
    dir = dirs.popleft()
    if not dir.isnumeric():
        if dir == "R":
            orient = cycle[(cycle.index(orient)+1) % 4] 
        elif dir == "L":
            orient = cycle[(cycle.index(orient)-1) % 4] 
    else:
        count = int(dir)
        while count:
            if orient == "N":
                index = (column.index(x) - 1) % len(column)
                if map[(column[index], y)] == "#":
                    break
                x = column[index]
                cur = x, y
                count -= 1
            elif orient == "E":
                index = (row.index(y) + 1) % len(row)
                if map[(x, row[index])] == "#":
                    break
                y = row[index]
                cur = x, row[index]
                count -= 1
            elif orient == "S":
                index = (column.index(x) + 1) % len(column)
                if map[(column[index], y)] == "#":
                    break
                x = column[index]
                cur = x, y
                count -= 1
            else:
                index = (row.index(y) - 1) % len(row)
                if map[(x, row[index])] == "#":
                    break
                y = row[index]
                cur = x, y
                count -= 1

print(1000*(x+1) + 4*(y+1) + cycle.index(orient))

