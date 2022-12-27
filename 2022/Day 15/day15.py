import copy

data = [x.split() for x in open("./input.csv").read().splitlines()]

closest = [[(int(x[2][2:-1]), int(x[3][2:-1])), (int(x[8][2:-1]), int(x[9][2:]))]  for x in data]
# print(closest)

def get_mh_dist(s, b):
    x1, y1 = s
    x2, y2 = b

    return abs(x1-x2) + abs(y1-y2)


def within(closest, y):
    '''Each sensor draws out a diamond given the Manhattan distance. Find if this diamond crossed the specified y row. 
    If it does cross, we can determine the x columns which is has scanned.'''
    seen = set()
    taken = set()
    for s, b in closest:
        x1, y1 = s
        radius = get_mh_dist(s, b)
        if y in range(y1-radius, y1+radius+1):
            dy = abs(y-y1)
            for point in range(x1-(radius-dy), x1+(radius-dy)+1):
                seen.add(point)
                taken.add(point)

    # Checking if a beacon is actually in the row. If it is, remove from seen as there is a beacon there. (Still in taken for part 2)
    for x in closest:
        if x[1][1] == y:
            if x[1][0] in seen:
                seen.remove(x[1][0])

    return seen, len(seen), taken


print(within(closest, 2000000)[1])

# Part 2
def get_freq(m):
    '''m is the max x/y coordinate. This draws out the square to be scanned row by row.'''
    comp_set = set()
    for i in range(m):
        comp_set.add(i)

    # Since the is only 1 possible position, we find the row that is not all taken.
    for i in range(m):
        print(i)
        if len(comp_set & within(closest, i)[2]) != m:
            x = (comp_set - (comp_set & within(closest, i)[2])).pop()
            y = i
            print((x,y))
            return x*4000000 + y

#print(get_freq(4000000)) Brute force too slow

# a is the intercept of the positive gradient lines
def pos_grad_int(s, b):
    sx, sy = s[0], s[1]
    r = get_mh_dist(s, b)
    corners = [(sx+r+1, sy), (sx-r-1, sy)]

    return [y-x for (x,y) in corners]
    
a = [pos_grad_int(s, b) for s,b in closest]
a = [item for sublist in a for item in sublist]

# b is the intercept of the negative gradient lines
def neg_grad_int(s, b):
    sx, sy = s[0], s[1]
    r = get_mh_dist(s, b)

    corners = [(sx+r+1, sy), (sx-r-1, sy)]

    return [y+x for y,x in corners]

b = [neg_grad_int(s, b) for s,b in closest]
b = [item for sublist in b for item in sublist]


# Get all points of intersection of all boundaries of all scanners
y_max = 4000000
poi = []
for aa in a:
    for bb in b:
        (x, y) = ((bb-aa)/2, (bb+aa)/2)
        if (0 <= x <= y_max) and (0 <= y <= y_max):
            poi.append((x, y))

poi = set(poi)
rows = set() # The set of rows to brute force check

for point in poi:
    x,y = point
    if x.is_integer() or y.is_integer():
        rows.add(y)

print(len(rows))

def get_freq(m):
    '''m is the max x/y coordinate. This draws out the square to be scanned row by row.'''
    comp_set = set()
    for i in range(m):
        comp_set.add(i)

    j=0
    # Since the is only 1 possible position, we find the row that is not all taken.
    for i in rows:
        j += 1
        if j%100 == 0:
            print(j/len(rows))

        i = int(i)
        if len(comp_set & within(closest, i)[2]) != m:
            x = (comp_set - (comp_set & within(closest, i)[2])).pop()
            y = i
            print((x,y))
            return x*4000000 + y

print(get_freq(y_max))