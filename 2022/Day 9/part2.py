with open('./input.csv') as file:
    data = [x.strip().split(' ') for x in file]

rope = [0] * 10
seen = {0}
sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)

dir = {"L": -1, "R": +1, "U": +1j, "D": -1j}

# head of rope is rope[0]
for line in data:
    for _ in range(int(line[1])):
        rope[0] += dir[line[0]]
        for i in range(len(rope)-1):
            delta = rope[i] - rope[i+1]
            if abs(delta) >= 2:
                rope[i+1] += complex(sign(delta.real), sign(delta.imag))
                if i+1 == 9:
                    seen.add(rope[i+1])
            else:
                break

print(len(seen))   