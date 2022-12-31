import collections

cubes = {tuple(map(int, (x.split(",")))) for x in open("./test.csv").read().splitlines()} # All cubes within 25x25x25

surround = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

surface = 0
for cube in cubes:
    for neighbour in surround(*cube):
        if neighbour not in cubes:
            surface += 1

# print(sum((s not in cubes) for c in cubes for s in surround(*c)))
print(surface)
    
# Part 2
stack = [(0,0,0)]
seen = set()
surface = 0
while stack:
    cur = stack.pop()
    for neighbour in surround(*cur):
        x,y,z = neighbour
        if (neighbour not in seen) and (0<=x<=5) and (0<=y<=5) and (0<=z<=5):
            if neighbour not in cubes:    
                stack.append(neighbour)
            elif neighbour in cubes:
                surface += 1
    seen.add(cur)

print(surface)


'''seen = set()
todo = [(-1,-1,-1)]

stack = [(0,0,0)]
seen = set()
surface = 0
while stack:
    here = stack.pop()
    stack += [s for s in (surround(*here) - cubes - seen) if all(-1<=c<=25 for c in s)]
    seen |= {here}

print(sum((s in seen) for c in cubes for s in surround(*c)))'''