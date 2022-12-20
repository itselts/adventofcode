with open("./input.csv") as file:
    data = [x.split(' ') for x in file.read().splitlines()]

rope = [0] * 2
seen = {0}
sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)

dir = {"L": -1, "R": +1, "U": +1j, "D": -1j}

# head of rope is rope[0]
for line in data:
    for _ in range(int(line[1])):
        rope[0] += dir[line[0]]
        delta = rope[0] - rope[1]
        if abs(delta) >= 2:
            rope[1] += complex(sign(delta.real), sign(delta.imag))
            seen.add(rope[1])

print(len(seen))        
