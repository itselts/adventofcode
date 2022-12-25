data = [x.split(" -> ") for x in open("./input.csv").read().splitlines()]
parse = lambda x: [tuple(map(int, a.split(","))) for a in x]
data = [parse(x) for x in data]
# print(data)

# rocks = 1, sand = 0
grid = {}

for paths in data:
    for i, coord in enumerate(paths[:-1]):
        dx = paths[i+1][0] - paths[i][0]
        dy = paths[i+1][1] - paths[i][1]
        
        x1, y1 = paths[i]
        x2, y2 = paths[i+1]

        if dx == 0:
            for j in range(min(y1, y2), max(y1, y2)+1):
                grid[(x1, j)] = 1
        else:
            for j in range(min(x1, x2), max(x1, x2)+1):
                grid[(j, y1)] = 1


def fall(grid):
    cx, cy = (500, 0)
    k=0
    while True:
        if (cx, cy+1) not in grid.keys():
            cx, cy = cx, cy+1
            k += 1
            if k == 10000:
                return False
            continue
        else:
            if (cx-1, cy+1) not in grid.keys():
                cx, cy = cx-1, cy+1
                continue
            elif (cx+1, cy+1) not in grid.keys():
                cx, cy = cx+1, cy+1
                continue
            else:
                return (cx, cy)


i = 0
part2 = True

if part2 == False:
    while fall(grid):
        i += 1
        grid[fall(grid)] = 0

    print(i)
else:
    y_max = max(y for x,y in grid.keys())
    y_max += 2
    
    for x in range(0, 1000):
        grid[(x, y_max)] = 1

    i = 0
    while fall(grid) != (500,0):
        i += 1
        grid[fall(grid)] = 0

    print(i+1)



