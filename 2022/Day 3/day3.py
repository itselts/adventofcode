path = "C:/Users/Elton/Documents/GitHub/adventofcode/2022/Day 3/"

with open(path+"input.csv") as file:
    data = file.read().splitlines()

# Part 1
def get_error(input):
    l = len(input)
    first = input[:int(l/2)]
    second = input[int(l/2):]

    set1 = set(first)
    set2 = set(second)

    if len(set1.intersection(set2)) == 0:
        return None
    else:
        return set1.intersection(set2).pop()

#print(get_error("vJrwpWtwJgWrhcsFMMfFFhFp"))

def get_priority(input):
    if input == None:
        return 0
    elif input.isupper():
        return ord(input) - 38
    else:
        return ord(input) - 96

#print(get_priority(get_error("vJrwpWtwJgWrhcsFMMfFFhFp")))

total = 0
for i in data:
    total += get_priority(get_error(i))

#print(total)

# Part 2
def get_badge(input):
    return set(input[0]).intersection(set(input[1]), set(input[2])).pop()


# data=['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']

group = []
total = 0

for i in data:
    if len(group) != 3:
        group.append(i)
        continue
    else:
        total += get_priority(get_badge(group))
        group = [i] 

total += get_priority(get_badge(group))
print(total)