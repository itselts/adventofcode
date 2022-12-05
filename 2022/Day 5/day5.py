import pandas as pd
from collections import deque

path = "C:/Users/Elton/Documents/GitHub/adventofcode/2022/Day 5/"

with open(path+"input.csv") as file:
    data = file.read().splitlines()

# print(list(map(len,data)))

stack_input = data[:9]
move_input = data[10:]

for i, r in enumerate(stack_input):
    stack_input[i] = list(r)

print(pd.DataFrame(stack_input))

stack = {}
for i in range(1,10):
    stack[i] = []


for i, r in pd.DataFrame(stack_input).iterrows():
    for j, c in r.items():
        if (j-1) % 4 == 0 and c.isalpha():
            stack[int((j-1)/4) + 1] = stack[int((j-1)/4) + 1] + [c]

#for key in stack.keys():
#    stack[key] = deque(stack[key])


#print(move_input)
for i in move_input:
    m, f, t = int(i.split(' ')[1]), int(i.split(' ')[3]), int(i.split(' ')[5])

    delta = stack[f][:m]
    # delta = delta[::-1] # COMMENT OUT FOR PART 2

    stack[f], stack[t] = stack[f][m:], delta + stack[t]

top = []
for i in range(1,10):
    top.append(stack[i][0])
print(''.join(top))


