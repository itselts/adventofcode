from copy import deepcopy 
from collections import defaultdict

file = "input"

part2 = True
grove = set([(i,j) for j, line in enumerate(open(f"./{file}.csv").read().splitlines()) for i, x in enumerate(list(line)) if x == "#"])
cycle = ["N", "S", "W", "E"]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def move(dir, i, j):
    '''Check whether it is empty based on direction, as well as the propsed move coords.'''
    if dir == "N":
        return all([s not in grove for s in [(i-1, j-1), (i, j-1), (i+1, j-1)]]), (i, j-1)
    elif dir == "S":
        return all([s not in grove for s in [(i-1, j+1), (i, j+1), (i+1, j+1)]]), (i, j+1)
    elif dir == "E":
        return all([s not in grove for s in [(i+1, j-1), (i+1, j), (i+1, j+1)]]), (i+1, j)
    else:
        return all([s not in grove for s in [(i-1, j-1), (i-1, j), (i-1, j+1)]]), (i-1, j)

# True if there are no adjacent elves
alone = lambda i,j: all([s not in grove for s in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]])

k=0
while True:
    k += 1
    print(k)

    #ymin = min(x[1] for x in grove)
    #ymax = max(x[1] for x in grove)
    #xmin = min(x[0] for x in grove)
    # xmax = max(x[0] for x in grove)

    #for j in range(13):
    #    print("")
    #    for i in range(13):
    #        if (i,j) in grove:
    #            print("#", end="")
    #        else:
    #            print(".", end="")

    old_grove = deepcopy(grove)

    # First half 
    transitions = set() # Pairs of old -> new
    proposed = defaultdict(lambda : 0) # Dictionary to count the number of proposals to each position

    for elf in grove:
        i, j = elf[0], elf[1]
        if alone(i, j):
            transitions.add(((i,j), (i,j)))
            proposed[(i,j)] += 1
            continue
        
        fr, to = (i,j), (i,j)
        for dir in cycle:
            if move(dir,i,j)[0]:
                fr, to = ((i,j), move(dir,i,j)[1])
                break
        proposed[to] += 1
        transitions.add((fr, to))

    # Second half
    grove = set()
    for transition in transitions:
        fr, to = transition[0], transition[1]
        if proposed[to] == 1:
            grove.add(to)
        else:
            grove.add(fr)

    cycle = cycle[1:] + list(cycle[0])

    if part2 == False:
        if k == 10:
            ymin = min(x[1] for x in grove)
            ymax = max(x[1] for x in grove)
            xmin = min(x[0] for x in grove)
            xmax = max(x[0] for x in grove)
            print((ymax-ymin+1)*(xmax-xmin+1)-len(grove))
            break
    else:
        if grove == old_grove:
            print(k)
            break

