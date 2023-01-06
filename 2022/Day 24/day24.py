from collections import deque

blizzards = {}
boundaries = set()
min_steps = 100

n=0
for k, line in enumerate(open("./test.csv").read().splitlines()):
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


# BFS 
# State: (current position, blizzard positions, steps taken)
stack = deque([((1+0j), 0)])
seen = {}
debug = set()
old_step = -1

while stack:
    finished = False
    cur_pos, steps = stack.popleft()
    seen[(cur_pos, tuple([blizzards[key][0] for key in sorted(blizzards.keys())]))] = steps # Dictionary that tracks seen states and the step number in which it was seen. Prevent infinite loops or finding a branch with shorter path
    

    if steps > old_step:
        old_step = steps
        print(steps)
        print_grid(blizzards, 0j)
        # Blizzard shift
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
    
    # Staying in palce
    if (cur_pos not in [v[0] for v in blizzards.values()]):
        state = (cur_pos, tuple([blizzards[key][0] for key in sorted(blizzards.keys())]))
        if (state not in seen) or (state in seen and steps+1 <= seen[state]): # Either we haven't seen the state, or we have and the current step is lower.
            stack.append((cur_pos, steps+1))
            if (state in seen): # If we have seen it, update the seen dictionary with the lower step
                del seen[state]
                seen[state] = steps+1
    
    # Moving to empty space
    for adj in [cur_pos+move for move in dirs.values()]:
        if adj == complex(xmax-1, ymax): # If we hit the end
            finished = True
            print_grid(blizzards, adj)
            print(steps+1)
            break
            if steps+1 < min_steps:
                min_steps = steps + 1
        if (1 <= adj.real <= xmax-1) and (1 <= adj.imag <= ymax-1):
            if (adj not in [v[0] for v in blizzards.values()]):
                state = (adj, tuple([blizzards[key][0] for key in sorted(blizzards.keys())]))
                if (state not in seen) or (state in seen and steps+1 <= seen[state]): 
                    stack.append((adj, steps+1))
                    if (state in seen):
                        del seen[state]
                        seen[state] = steps+1
    if finished:
        break
