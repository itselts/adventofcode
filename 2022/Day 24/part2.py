from collections import deque

blizzards = {}
boundaries = set()
min_steps = 100

n=0
for k, line in enumerate(open("./input.csv").read().splitlines()):
    for i, x in enumerate(line):
        if x in [">", "<", "v", "^"]:
            blizzards[n] = [complex(i,k), x]
            n += 1
        if x == "#":
            boundaries.add(complex(i,k))

xmax = int(max(p.real for p in boundaries))
ymax = int(max(p.imag for p in boundaries))

dirs = {">": (+1+0j), "<": (-1+0j), "^": (0-1j), "v": (0+1j)}

def print_grid(blizzards, pos):
    for y in range(ymax+1):
        print("".join("#" if complex(x,y) in boundaries else ("@" if complex(x,y) in [v[0] for v in blizzards.values()] else ("E" if complex(x,y) == pos else ".")) for x in range(xmax+1)))
    print("\n")

def next_bliz():
    '''Blizzard shift.'''
    for b in blizzards:
        dir = blizzards[b][1]
        new_bliz_pos = blizzards[b][0] + dirs[dir]
        if new_bliz_pos in boundaries:  
            if new_bliz_pos.real == 0:
                blizzards[b][0] = complex(xmax-1, new_bliz_pos.imag)
                continue
            if new_bliz_pos.real == xmax:
                blizzards[b][0] = complex(1, new_bliz_pos.imag)
                continue
            if new_bliz_pos.imag == 0:
                blizzards[b][0] = complex(new_bliz_pos.real, ymax-1)
                continue
            if new_bliz_pos.imag == ymax:
                blizzards[b][0] = complex(new_bliz_pos.real, 1)
                continue
        blizzards[b][0] = new_bliz_pos
        continue

# BFS 
# State: (current position, end1, start1, steps taken)
stack = deque([((1+0j), False, False, 0)])
seen = {(((1+0j), False, False, 0))}
old_step = -1

while stack:
    #print(len(stack))
    finished = False
    cur_pos, end1, start2, steps = stack.popleft()
    seen.add((cur_pos, end1, start2, steps))

    if steps > old_step: # Blizzard shift
        print(old_step, steps)
        old_step = steps 
        next_bliz()
        occupied = set()
        for k in blizzards:
            occupied.add(blizzards[k][0])

    # Staying in palce
    if (cur_pos not in occupied) and ((cur_pos, end1, start2, steps+1) not in seen) and ((cur_pos, end1, start2, steps+1) not in stack):
        stack.append((cur_pos, end1, start2, steps+1))
        #seen.add((cur_pos, end1, start2, steps+1))

    # Moving to empty space
    for adj in [cur_pos+move for move in dirs.values()]:
        if adj == complex(xmax-1, ymax) and (end1 == True) and (start2 == True): # If we finish our return trip
            finished = True
            print("DONE")
            print(steps+1)
            break
        if (0 <= adj.real <= xmax) and (0 <= adj.imag <= ymax):
            if adj in boundaries:
                    continue
            if (adj not in occupied) and ((adj, end1, start2, steps+1) not in seen) and ((adj, end1, start2, steps+1) not in stack):
                if adj == complex(xmax-1, ymax) and (end1 == False) and (start2 == False):
                    stack = deque([])
                    stack.append((adj, True, False, steps+1))
                    #seen.add((adj, True, False, steps+1))
                    print("End reached once.")
                    break
                elif adj == complex(1, 0) and (end1 == True) and (start2 == False):
                    stack = deque([])
                    stack.append((adj, True, True, steps+1))
                    #seen.add((adj, True, True, steps+1))
                    print("Start reached again.")
                    break
                else:
                    stack.append((adj, end1, start2, steps+1))
                
            

    if finished:
        break
