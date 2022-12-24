import functools

pairs = [[*map(eval, x.split())] for x in open("./input.csv").read().split("\n\n")]

def compare(l, r):
    # 1 if l < r, 0 if l == r, -1 if l > r
    match l, r:
        case int(), int():
            if l < r:
                return 1
            elif l == r:
                return 0
            else:
                return -1 
        case int(), list():
            return compare([l], r)
        case list(), int():
            return compare(l, [r])
        case list(), list():
            for ll, rr in zip(l,r):
                x = compare(ll, rr)
                if x != 0:
                    return x
            # if you reach the end of the list and nothing is triggered
            n = len(l)
            m = len(r)
            if n < m:
                return 1
            elif n == m:
                return 0
            else:
                return -1

tot = 0
for i, pair in enumerate(pairs):
    if compare(pair[0], pair[1]) == 1:
        tot += i+1

print(sum([i+1 for i, pair in enumerate(pairs) if compare(pair[0], pair[1]) == 1]))


# part 2
packets = []
for a,b in pairs:
    packets.append(a)
    packets.append(b)

packets.append([[2]])
packets.append([[6]])

for _ in range(len(packets)):
    for j in range(len(packets)-1):
        # print(compare(packets[j], packets[j-1]))
        if compare(packets[j], packets[j+1]) != 1:
            packets[j], packets[j+1] = packets[j+1], packets[j]

print(functools.reduce(lambda x, y: x*y, [i+1 for i, x in enumerate(packets) if x == [[2]] or x == [[6]]]))