import re
from collections import deque

f = "input"

map = {}
for r, line in enumerate(open(f"./{f}.csv").read().splitlines()):
    if line == "":
        break
    for c, x in enumerate(line):
        map[(r,c)] = x

dirs = deque(re.split('([\d]+)', open(f"./{f}.csv").read().splitlines()[-1])) # Directions split between numeric and alphabetic
cycle = ["E", "S", "W", "N"]

(x,y), orient = (min([k for k,v in map.items() if v in ['.', '#']]), "E") # Initial conditions



while dirs:
    dir = dirs.popleft()

    if not dir.isnumeric(): # Changing the orientation if it is L or R
        if dir == "R":
            orient = cycle[(cycle.index(orient)+1) % 4] 
        elif dir == "L":
            orient = cycle[(cycle.index(orient)-1) % 4] 
    else:
        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])]) # Indicies for the current column that are non-blank (Either . or #)
        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]]) # Indicies for the current row that are non-blank (Either . or #)

        count = int(dir)
        while count:
            #print((x,y), orient)
            if orient == "N":
                index = (column.index(x) - 1) % len(column)

                if index == len(column) - 1: # If we hit the end of the column by going around (Blank space/Orientation change going around cube)
                    if 0 <= y <= 49: # Edge N2
                        if map[(y+50,50)] == "#":
                            break
                        orient = "E"
                        x,y = y+50,50
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 50 <= y <= 99: # Edge N5
                        if map[(y+100, 0)] == "#":
                            break 
                        orient = "E"
                        x, y = y+100, 0
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 100 <= y <= 149: # Edge N6
                        if map[(199, y-100)] == "#":
                            break
                        orient = "N"
                        x, y = 199, y-100
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                else:
                    if map[(column[index], y)] == "#": # If hit a wall
                        break
                    x = column[index]
                    count -= 1

            elif orient == "E":
                index = (row.index(y) + 1) % len(row)

                if index == 0: # If we hit the start of the row by going around (Blank space/Orientation change going around cube)
                    if 0 <= x <= 49: # Edge E6
                        if map[(100+(49-x),99)] == "#":
                            break
                        orient = "W"
                        x, y = 100+49-x, 99
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 50 <= x <= 99: # Edge E4
                        if map[(49, 50+x)] == "#":
                            break
                        orient = "N"
                        x, y = 49, 50+x
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 100 <= x <= 149: # Edge E3
                        if map[(149-x+0, 149)] == "#":
                            break
                        orient = "W"
                        x, y = 149-x+0, 149
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 150 <= x <= 199: # Edge E1
                        if map[(149, x-100)] == "#":
                            break
                        orient = "N"
                        x, y = 149, x-100
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                else:
                    if map[(x, row[index])] == "#":
                        break
                    y = row[index]
                    count -= 1

            elif orient == "S":
                index = (column.index(x) + 1) % len(column)
                
                if index == 0: # If we hit the start of the column by going around (Blank space/Orientation change going around cube)
                    if 0 <= y <= 49: # Edge S1
                        if map[(0, y+100)] == "#":
                            break
                        orient = "S"
                        x, y = 0, y+100
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 50 <= y <= 99: # Edge S3
                        if map[(y+100, 49)] == "#":
                            break
                        orient = "W"
                        x, y = y+100, 49
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 100 <= y <= 149: # Edge S6
                        if map[(y-50,99)] == "#":
                            break
                        orient = "W"
                        x, y = y-50, 99
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                else:
                    if map[(column[index], y)] == "#":
                        break
                    x = column[index]
                    count -= 1

            else:
                index = (row.index(y) - 1) % len(row)

                if index == len(row) - 1: # if we hit the end of the row by going around (Blank space/Orientation change going around cube)
                    if 0 <= x <= 49: # Edge W5
                        if map[(100+49-x,0)] == "#":
                            break
                        orient = "E"
                        x, y = 100+49-x, 0
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 50 <= x <= 99: # Edge W4
                        if map[(100, x-50)] == "#":
                            break
                        orient = "S"
                        x, y = 100, x-50
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 100 <= x <= 149: # Edge W2
                        if map[(0+149-x, 50)] == "#":
                            break
                        orient = "E"
                        x, y = 0+149-x, 50
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                    if 150 <= x <= 199: # Edge W1
                        if map[(0, x-100)] == "#":
                            break
                        orient = "S"
                        x, y = 0, x-100
                        column = sorted([coord[0] for coord in map if (coord[1] == y and map[coord] in [".", "#"])])
                        row = sorted([coord[1] for coord in map if coord[0] == x and map[coord] in [".", "#"]])
                        count -= 1
                        continue
                else:
                    if map[(x, row[index])] == "#":
                        break
                    y = row[index]
                    count -= 1
                
print(1000*(x+1) + 4*(y+1) + cycle.index(orient))