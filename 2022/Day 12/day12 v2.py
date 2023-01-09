from collections import deque, defaultdict
from copy import deepcopy

grid = {complex(i,j): x for j, line in enumerate(open("./input.csv").read().splitlines()) for i,x in enumerate(line)}

S_coord = [k for k,v in grid.items() if v == "S"][0]
E_coord = [k for k,v in grid.items() if v == "E"][0]

grid[S_coord] = "a"
grid[E_coord] = "z"

grid = {k: ord(v) for k,v in grid.items()}

stack = deque([S_coord])
dist = defaultdict(lambda : 100000)
dist[S_coord] = 0

dirs = [-1, +1, -1j, +1j] # left, right, up, down

while stack:
    cur = stack.popleft()
    for dir in dirs:
        if (cur+dir in grid) and (grid[cur+dir] <= grid[cur]+1):
            ndst = dist[cur] + 1
            if ndst < dist[cur+dir]:
                dist[cur+dir] = ndst
                stack.append(cur+dir)

print(dist[E_coord])


