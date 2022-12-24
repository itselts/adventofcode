pairs = [[*map(eval, x.split())] for x in open("./input.csv").read().split("\n\n")]

def compare(l, r):
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
