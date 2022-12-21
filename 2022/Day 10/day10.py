import numpy as np
import pandas as pd

data = [x.split(" ") for x in open("./input.csv").read().splitlines()]

total = 0
cycle = 0
X = 1

for line in data:
    if line[0] == 'noop':
        cycle += 1
        if (cycle-20) % 40 == 0:
            total += cycle * X
        continue
    else:
        for _ in range(2):
            cycle += 1
            if (cycle-20) % 40 == 0:
                total += cycle * X
        X += int(line[1])

print(total)

# part 2
CRT = []
cycle = 0
X = 1
row = []

for line in data:
    if line[0] == 'noop':
        cycle += 1
        pos = cycle-1
        if pos in range(X-1, X+2):
            row.append('#')
        else:
            row.append('.')

        if cycle == 40:
            CRT.append(row)
            cycle = 0
            row = []

    else:
        for _ in range(2):
            cycle += 1
            pos = cycle-1
            if pos in range(X-1, X+2):
                row.append('#')
            else:
                row.append('.')

            if cycle == 40:
                CRT.append(row)
                cycle = 0
                row = []
        X += int(line[1])

print(pd.DataFrame(np.array(CRT)))