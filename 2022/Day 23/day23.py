from collections import deque
from copy import deepcopy

file = "input"

grove = {}
cycle = deque(["N", "S", "W", "E"])

n = 0
for i, line in enumerate(open(f"./{file}.csv").read().splitlines()):
    for j, x in enumerate(line):
        if x == "#":
            grove[n] = [(i,j), cycle]
            n += 1

def move(dir, i, j):
    '''Check whether it is empty based on direction, as well as the propsed move coords.'''
    positions = {v[0] for k,v in grove.items()}
    if dir == "N":
        return all([s not in positions for s in [(i-1, j-1), (i-1, j), (i-1, j+1)]]), (i-1, j)
    elif dir == "S":
        return all([s not in positions for s in [(i+1, j-1), (i+1, j), (i+1, j+1)]]), (i+1, j)
    elif dir == "E":
        return all([s not in positions for s in [(i+1, j+1), (i-1, j+1), (i, j+1)]]), (i, j+1)
    else:
        return all([s not in positions for s in [(i+1, j-1), (i-1, j-1), (i, j-1)]]), (i, j-1)


# True if there are no adjacent elves
alone = lambda i,j,grove: all([s not in {v[0] for k,v in grove.items()} for s in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]])

for k in range(10):
    print(k)
    # First half 
    proposed = []
    overlap = set()
    for elf in grove:
        i, j = grove[elf][0][0], grove[elf][0][1]
        cycle = grove[elf][1]
        if alone(i, j, grove):
            proposed.append((i,j))
            overlap.add((i,j))
            new_cycle = deque(list(grove[elf][1][1] + grove[elf][1][2] + grove[elf][1][3] + grove[elf][1][0]))
            grove[elf][1] = new_cycle
            continue

        propose = (i,j)
        for dir in grove[elf][1]:
            if move(dir,i,j)[0]:
                if move(dir,i,j)[1] in proposed:
                    overlap.add(move(dir,i,j)[1])
                propose = move(dir,i,j)[1]
                break
        proposed.append(propose)
        new_cycle = deque(list(grove[elf][1][1] + grove[elf][1][2] + grove[elf][1][3] + grove[elf][1][0]))
        grove[elf][1] = new_cycle



    # Second half
    for elf in grove:
        if proposed[elf] not in overlap:
                grove[elf][0] = proposed[elf]


ymin = min(v[0][1] for k,v in grove.items())
ymax = max(v[0][1] for k,v in grove.items())
xmin = min(v[0][0] for k,v in grove.items())
xmax = max(v[0][0] for k,v in grove.items())

print((ymax-ymin+1)*(xmax-xmin+1)-len(grove))

'''positions = {v[0] for k,v in grove.items()}

r = 3
positions_r = set()
for i, line in enumerate(open(f"./r{r}.csv").read().splitlines()):
    for j, x in enumerate(line):
        if x == "#":
            positions_r.add((i,j))
print(positions_r - positions)
print(len(grove))
print(len(positions_r - positions))'''
