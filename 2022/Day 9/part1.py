with open('./input.csv') as file:
    data = [x.strip().split(' ') for x in file]

def up(h_coord, t_coord, n, visited=set()):
    h_x, h_y = h_coord
    t_x, t_y = t_coord
    visited.add(t_coord)

    if n == 1:
        if h_y == t_y: # tail same y 
            visited.add(t_coord)
            return ((h_x, h_y+1), t_coord, visited)
        elif t_y < h_y and abs(t_x - h_x) == 1: # tail lower y
            visited.add((h_x, t_y+1))
            return ((h_x, h_y+1), (h_x, t_y+1), visited)
        elif t_y < h_y and t_x == h_x: # tail lower y
            visited.add((t_x, t_y+1))
            return ((h_x, h_y+1), (t_x, t_y+1), visited)
        elif t_y > h_y: # tail higher
            return ((h_x, h_y+1), t_coord, visited)
    else:
        if h_y == t_y: # tail same y 
            return up((h_x, h_y+1), t_coord, n-1, visited)
        elif t_y < h_y and abs(t_x - h_x) == 1: # tail lower y
            return up((h_x, h_y+1), (h_x, t_y+1), n-1, visited)
        elif t_y < h_y and t_x == h_x: # tail lower y
            return up((h_x, h_y+1), (t_x, t_y+1), n-1, visited)
        elif t_y > h_y: # tail higher
            return up((h_x, h_y+1), t_coord, n-1, visited)


# print(up((5,1), (4,1), 4)[2])

def down(h_coord, t_coord, n, visited=set()):
    h_x, h_y = h_coord
    t_x, t_y = t_coord
    visited.add(t_coord)

    if n == 1:
        if h_y == t_y: # tail same y 
            visited.add(t_coord)
            return ((h_x, h_y-1), t_coord, visited)
        elif t_y > h_y and abs(t_x - h_x) == 1: # tail lower y
            visited.add((h_x, t_y-1))
            return ((h_x, h_y-1), (h_x, t_y-1), visited)
        elif t_y > h_y and t_x == h_x: # tail lower y
            visited.add((t_x, t_y-1))
            return ((h_x, h_y-1), (t_x, t_y-1), visited)
        elif t_y < h_y: # tail lower
            visited.add(t_coord)
            return ((h_x, h_y-1), t_coord, visited)
    else:
        if h_y == t_y: # tail same y 
            return down((h_x, h_y-1), t_coord, n-1, visited)
        elif t_y > h_y and abs(t_x - h_x) == 1: # tail lower y
            return down((h_x, h_y-1), (h_x, t_y-1), n-1, visited)
        elif t_y > h_y and t_x == h_x: # tail lower y
            return down((h_x, h_y-1), (t_x, t_y-1), n-1, visited)
        elif t_y < h_y: # tail lower
            return down((h_x, h_y-1), t_coord, n-1, visited) 


def left(h_coord, t_coord, n, visited=set()):
    h_x, h_y = h_coord
    t_x, t_y = t_coord
    visited.add(t_coord)

    if n == 1:
        if h_x == t_x: # tail same x 
            visited.add(t_coord)
            return ((h_x-1, h_y), t_coord, visited)
        elif h_x < t_x and abs(t_y - h_y) == 1: # tail right x
            visited.add((t_x-1, h_y))
            return ((h_x-1, h_y), (t_x-1, h_y), visited)
        elif h_x < t_x and t_y == h_y: # tail right x
            visited.add((t_x-1, t_y))
            return ((h_x-1, h_y), (t_x-1, t_y), visited)
        elif h_x > t_x: # tail left x
            visited.add(t_coord)
            return ((h_x-1, h_y), t_coord, visited)
        
    else:
        if h_x == t_x: # tail same x 
            return left((h_x-1, h_y), t_coord, n-1, visited)
        elif h_x < t_x and abs(t_y - h_y) == 1: # tail right x
            return left((h_x-1, h_y), (t_x-1, h_y), n-1, visited)
        elif h_x < t_x and t_y == h_y: # tail right x
            return left((h_x-1, h_y), (t_x-1, t_y), n-1, visited)
        elif h_x > t_x: # tail left x
            return left((h_x-1, h_y), t_coord, n-1, visited) 

# left((5,5), (5,4), 3)

def right(h_coord, t_coord, n, visited=set()):
    h_x, h_y = h_coord
    t_x, t_y = t_coord
    visited.add(t_coord)

    if n == 1:
        if h_x == t_x: # tail same x 
            visited.add(t_coord)
            return ((h_x+1, h_y), t_coord, visited)
        elif h_x > t_x and abs(t_y - h_y) == 1: # tail left x
            visited.add((t_x+1, h_y))
            return ((h_x+1, h_y), (t_x+1, h_y), visited)
        elif h_x > t_x and t_y == h_y: # tail left x
            visited.add((t_x+1, t_y))
            return ((h_x+1, h_y), (t_x+1, t_y), visited)
        elif h_x < t_x: # tail right
            visited.add(t_coord)
            return ((h_x+1, h_y), t_coord, visited)
    else:
        if h_x == t_x: # tail same x 
            return right((h_x+1, h_y), t_coord, n-1, visited)
        elif h_x > t_x and abs(t_y - h_y) == 1: # tail left x
            return right((h_x+1, h_y), (t_x+1, h_y), n-1, visited)
        elif h_x > t_x and t_y == h_y: # tail left x
            return right((h_x+1, h_y), (t_x+1, t_y), n-1, visited)
        elif h_x < t_x: # tail right
            return right((h_x+1, h_y), t_coord, n-1, visited)

# right((1,1), (1,1), 4)

visited = {(1,1)}
current = ((1,1), (1,1))
for move in data:
    if move[0] == 'U':
        current = up(current[0], current[1], int(move[1]))
        visited = visited.union(current[2])
    elif move[0] == 'D':
        current = down(current[0], current[1], int(move[1]))
        visited = visited.union(current[2])
    elif move[0] == 'L':
        current = left(current[0], current[1], int(move[1]))
        visited = visited.union(current[2])
    else:
        current = right(current[0], current[1], int(move[1]))
        visited = visited.union(current[2])

print(len(visited))