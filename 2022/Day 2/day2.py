path = "C:/Users/Elton/Documents/GitHub/adventofcode/2022/Day 2/"



def get_score(input):
    if input == "A X":
        return 1 + 3
    elif input == "B Y":
        return 2 + 3
    elif input == "C Z":
        return 3 + 3
    elif input == "A Y":
        return 2 + 6
    elif input == "B Z":
        return 3 + 6
    elif input ==  "C X":
        return 1 + 6
    elif input == "A Z":
        return 3
    elif input == "B X":
        return 1
    else:
        return 2


def solve1(input_file):
    with open(path+input_file) as file:
        data = file.read().splitlines()

    total = 0
    for i in data:
        total += get_score(i)
    return total


def to_win(input):
    if input == "A X":
        return "Z"
    elif input == "B Y":
        return "Y"
    elif input == "C Z":
        return "X"
    elif input == "A Y":
        return "X"
    elif input == "B Z":
        return "Z"
    elif input ==  "C X":
        return "Y"
    elif input == "A Z":
        return "Y"
    elif input == "B X":
        return "X"
    else:
        return "Z"    

def solve2(input_file):
    with open(path+input_file) as file:
        data = file.read().splitlines()
    total = 0
    for i in data:
        total += get_score(i[0:2]+to_win(i))
    return total

print(solve2("input1.csv"))



