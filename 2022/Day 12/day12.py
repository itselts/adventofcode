import numpy as np
import math

map = [list(x) for x in open("./input.csv").read().splitlines()]
map = np.array(map)

adj = {}


def neighbour(index, map):
    row = index[0]
    col = index[1]

    valid = set()

    if map[index] == "S":
        if (col != map.shape[1]-1) and (ord(map[row, col+1]) - ord("a") <= 1): # look right
            valid.add((row, col+1))
        
        if  (col != 0) and (ord(map[row, col-1]) - ord("a") <= 1): # look left
            valid.add((row, col-1))

        if (row != map.shape[0] - 1) and (ord(map[row+1, col]) - ord("a") <= 1): # look up (But traverse down)
            valid.add((row+1, col))
        
        if (row != 0) and (ord(map[row-1, col]) - ord("a") <= 1): # look down (But traverse up)
            valid.add((row-1, col))

    else:
        if (col != map.shape[1]-1) and (ord(map[row, col+1]) - ord(map[index]) <= 1): # look right
            valid.add((row, col+1))
        
        if  (col != 0) and (ord(map[row, col-1]) - ord(map[index]) <= 1): # look left
            valid.add((row, col-1))

        if (row != map.shape[0] - 1) and (ord(map[row+1, col]) - ord(map[index]) <= 1): # look up (But traverse down)
            valid.add((row+1, col))
        
        if (row != 0) and (ord(map[row-1, col]) - ord(map[index]) <= 1): # look down (But traverse up)
            valid.add((row-1, col))

    return valid 


dist = {}
Q = set()
S = (20,0)
E = (20,40)

for index in np.ndindex(map.shape):
    Q.add(index)
    dist[index] = math.inf 

dist[S] = 0

while Q:
    
    tmp = {index: value for index, value in dist.items() if index in Q}
    u = min(tmp, key=tmp.get)
    # u = min(dist.keys() & Q, key=dist.get)
    
    if u == E:
        break
    
    Q.remove(u)
    for v in (neighbour(u, map) & Q):
        if dist[u] + 1 < dist[v]:
            dist[v] = dist[u] + 1

print(dist[E])