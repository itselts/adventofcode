from copy import deepcopy 

file = "input"

part2 = False
grove = {}
cycle = ["N", "S", "W", "E"]

n = 0
for i, line in enumerate(open(f"./{file}.csv").read().splitlines()):
    for j, x in enumerate(line):
        if x == "#":
            grove[n] = (i,j)
            n += 1

def move(dir, i, j):
    '''Check whether it is empty based on direction, as well as the propsed move coords.'''
    positions = {v for k,v in grove.items()}
    if dir == "N":
        return all([s not in positions for s in [(i-1, j-1), (i-1, j), (i-1, j+1)]]), (i-1, j)
    elif dir == "S":
        return all([s not in positions for s in [(i+1, j-1), (i+1, j), (i+1, j+1)]]), (i+1, j)
    elif dir == "E":
        return all([s not in positions for s in [(i+1, j+1), (i-1, j+1), (i, j+1)]]), (i, j+1)
    else:
        return all([s not in positions for s in [(i+1, j-1), (i-1, j-1), (i, j-1)]]), (i, j-1)


# True if there are no adjacent elves
alone = lambda i,j: all([s not in {v for k,v in grove.items()} for s in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]])

for k in range(100):
    old_grove = deepcopy(grove)
    # First half 
    proposed = []
    overlap = set()
    for elf in grove:
        i, j = grove[elf][0], grove[elf][1]
        if alone(i, j):
            proposed.append((i,j))
            overlap.add((i,j))
            continue

        propose = (i,j)
        for dir in cycle:
            if move(dir,i,j)[0]:
                if move(dir,i,j)[1] in proposed:
                    overlap.add(move(dir,i,j)[1])
                propose = move(dir,i,j)[1]
                break
        proposed.append(propose)

    # Second half
    for elf in grove:
        if proposed[elf] not in overlap:
                grove[elf] = proposed[elf]
    cycle = cycle[1:] + list(cycle[0])

    if part2 == False:
        if k == 9:
            ymin = min(v[1] for k,v in grove.items())
            ymax = max(v[1] for k,v in grove.items())
            xmin = min(v[0] for k,v in grove.items())
            xmax = max(v[0] for k,v in grove.items())

            print((ymax-ymin+1)*(xmax-xmin+1)-len(grove))
            break
    else:
        if grove == old_grove:
            print(k)
            break

