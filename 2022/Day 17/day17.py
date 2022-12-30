import collections

data = collections.deque(list(open("./input.csv").read()))
dirs = {">": +1, "<": -1}

stack = {(x+0j) for x in range(1,8)}

# Note that the 4th rock is the first element in the list due to modulo operator 
rocks = [{(3+0j), (4+0j), (5+0j), (6+0j)},
    {(4+0j), (3+1j), (4+1j), (5+1j), (4+2j)}, 
    {(3+0j), (4+0j), (5+0j), (5+1j), (5+2j)},
    {(3+0j), (3+1j), (3+2j), (3+3j)},
    {(3+0j), (3+1j), (4+0j), (4+1j)}]


part2 = True
m = 5 * len(data) # Modulous

if part2 == False:
    n = len(data)
    rock_i = 0
    dir_i = 0
    max_height = 0j
    while rock_i != 2022: # New rock
        rock_i += 1
        rock = {pos+max_height+4j for pos in rocks[(rock_i % 5)-1 if rock_i % 5 != 0 else 4]}
        while True: # New direction of jet
            dir_i += 1
            dir = data[(dir_i % n)-1 if dir_i % n != 0 else n-1]

            # Jet push 
            rock_moved = {pos+dirs[dir] for pos in rock}
            if (0 not in [int(pos.real) for pos in rock_moved]) and (8 not in [int(pos.real) for pos in rock_moved]) and not (rock_moved & stack):
                rock = rock_moved

            # Gravity drop
            rock_moved = {pos-1j for pos in rock}
            if rock_moved & stack:
                stack |= rock
                max_height = complex(0, max(pos.imag for pos in stack))
                break
            rock = rock_moved

    print(max_height)            
else:
    n = len(data)
    rock_i = 0
    dir_i = 0
    max_height = 0j
    seen = []
    while True: # New rock
        rock_i += 1
        rock = {pos+max_height+4j for pos in rocks[(rock_i % 5)-1 if rock_i % 5 != 0 else 4]}
        while True: # New direction of jet
            dir_i += 1
            dir = data[(dir_i % n)-1 if dir_i % n != 0 else n-1]

            # Jet push 
            rock_moved = {pos+dirs[dir] for pos in rock}
            if (0 not in [int(pos.real) for pos in rock_moved]) and (8 not in [int(pos.real) for pos in rock_moved]) and not (rock_moved & stack):
                rock = rock_moved

            # Gravity drop
            rock_moved = {pos-1j for pos in rock}
            if rock_moved & stack:
                stack |= rock
                max_height = complex(0, max(pos.imag for pos in stack))
                break
            rock = rock_moved
        
        top_stack = frozenset({pos-(max_height-50) for pos in stack if pos.imag > max_height.imag-50})
        new = (top_stack, (rock_i % 5)-1 if rock_i % 5 != 0 else 4, (dir_i % n)-1 if dir_i % n != 0 else n-1)
        
        if new not in seen:
            seen.append(new)
        else:
            repeat = len(seen)-seen.index(new) # Cycle repeating length. (Every 35 rocks)
            start = seen.index(new) + 1 # The i-th rock where the pattern first appears
            print((start, repeat, max_height))
            break
    # TEST INPUT: For top stack of depth 50 - Cycle starts at 47th rock (height 76), repeats every 35 rocks which adds (129-76)=53 height. (1000000000000-47)%35 = 3. 3 extra rocks add 2 height (max_height(47+3)-max_height(47))
    print(((1000000000000-47)//35)*53 + 76 + (78-76))

    # ACTUAL INPUT: For top stack of depth 50 - Cycle starts at 102th rock (height 154), repeats every 1745 rocks which adds (2892-154)=2738 height. (1000000000000-102)%1745 = 908. 908 extra rocks add 2 heights (max_height(102+908)-max_height(102))
    print(((1000000000000-102)//1745)*2738 + 154 + (1567-154))
    

        