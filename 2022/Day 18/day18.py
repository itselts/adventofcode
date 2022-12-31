import collections

cubes = {tuple(map(int, (x.split(",")))) for x in open("./input.csv").read().splitlines()} # All cubes within 25x25x25

surround = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

surface = 0
for cube in cubes:
    for neighbour in surround(*cube):
        if neighbour not in cubes:
            surface += 1

# print(sum((s not in cubes) for c in cubes for s in surround(*c)))
print(surface)
    
# Part 2
stack =[(-1,-1,-1)]
seen = set()
surface = 0
exterior = set()
while stack:
    cur = stack.pop()
    for neighbour in surround(*cur):
        x,y,z = neighbour
        if (neighbour not in seen) and (neighbour not in stack) and (-1<=x<=25) and (-1<=y<=25) and (-1<=z<=25):
            if (neighbour not in cubes): 
                stack.append(neighbour)
            else:
                surface += 1
                exterior.add(neighbour)
    seen.add(cur)

print(surface)
