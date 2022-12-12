with open('./input.csv') as file:
    data = [x.strip().split(' ') for x in file]

def up(h_coord, t_coord):
    h_x, h_y = h_coord
    t_x, t_y = t_coord

    if h_y == t_y: # tail same y 
        return ((h_x, h_y+1), t_coord)
    elif t_y < h_y and abs(t_x - h_x) == 1: # tail lower y
        return ((h_x, h_y+1), (h_x, t_y+1))
    elif t_y < h_y and t_x == h_x: # tail lower y
        return ((h_x, h_y+1), (t_x, t_y+1))
    elif t_y > h_y: # tail higher
        return ((h_x, h_y+1), t_coord)


def down(h_coord, t_coord):
    h_x, h_y = h_coord
    t_x, t_y = t_coord
    
    if h_y == t_y: # tail same y 
        return ((h_x, h_y-1), t_coord)
    elif t_y > h_y and abs(t_x - h_x) == 1: # tail lower y
        return ((h_x, h_y-1), (h_x, t_y-1))
    elif t_y > h_y and t_x == h_x: # tail lower y
        return ((h_x, h_y-1), (t_x, t_y-1))
    elif t_y < h_y: # tail lower
        return ((h_x, h_y-1), t_coord)

def left(h_coord, t_coord):
    h_x, h_y = h_coord
    t_x, t_y = t_coord
    
    if h_x == t_x: # tail same x 
        return ((h_x-1, h_y), t_coord)
    elif h_x < t_x and abs(t_y - h_y) == 1: # tail right x
        return ((h_x-1, h_y), (t_x-1, h_y))
    elif h_x < t_x and t_y == h_y: # tail right x
        return ((h_x-1, h_y), (t_x-1, t_y))
    elif h_x > t_x: # tail left x
        return ((h_x-1, h_y), t_coord)

def right(h_coord, t_coord):
    h_x, h_y = h_coord
    t_x, t_y = t_coord
    
    if h_x == t_x: # tail same x 
        return ((h_x+1, h_y), t_coord)
    elif h_x > t_x and abs(t_y - h_y) == 1: # tail left x
        return ((h_x+1, h_y), (t_x+1, h_y))
    elif h_x > t_x and t_y == h_y: # tail left x
        return ((h_x+1, h_y), (t_x+1, t_y))
    elif h_x < t_x: # tail right
        return ((h_x+1, h_y), t_coord)

for move in data:
    if move[0] == 'U':
        