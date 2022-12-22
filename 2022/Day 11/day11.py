import re
import math
import copy
import functools

monkeys = {}

for line in open("./input.csv").read().splitlines():
    if line.startswith("Monkey"):
        monkey = int(line.split(" ")[1][0])
        monkeys[monkey] = {"Starting": None, "Operation": None, "Test": None, 1: None, 0: None, "count": 0}
    elif line.strip().startswith("Starting"):
        monkeys[monkey]["Starting"] = [int(re.findall(r'\d+', x)[0]) for x in line.strip().split(" ")[2:]]
    elif line.strip().startswith("Operation"):
        operator = line.strip().split(" ")[4]
        value = line.strip().split(" ")[5]
        if value == "old":
            monkeys[monkey]["Operation"] = [operator, value]
        else:
            monkeys[monkey]["Operation"] = [operator, int(value)]
    elif line.strip().startswith("Test"):
        dividend = int(line.strip().split(" ")[3])
        monkeys[monkey]["Test"] = dividend
    elif line.strip().startswith("If true"):
        monkeys[monkey][1] = int(line.strip().split(" ")[5])
    elif line.strip().startswith("If false"):
        monkeys[monkey][0] = int(line.strip().split(" ")[5])


tests = []
for monkey in monkeys:
    tests.append(monkeys[monkey]["Test"])

modulo = functools.reduce(lambda x,y: x*y, tests) # (a mod kn) mod n = a mod n
# Addition and multiplication preserve congruence

part1 = False

for _ in range(10000):
    for i in range(len(monkeys)):
        starting = copy.deepcopy(monkeys[i]['Starting'])
        for item in starting:
            if monkeys[i]["Operation"][0] == "*":
                if monkeys[i]["Operation"][1] == "old":
                    new = item * item
                else:
                    new = item * monkeys[i]["Operation"][1]
            else:
                new = item + monkeys[i]["Operation"][1]

            if part1 == True:
                new = math.floor(new/3)
            else:
                new %= modulo

            if (new % monkeys[i]["Test"]) == 0:
                monkeys[monkeys[i][1]]["Starting"].append(new)
                monkeys[i]["Starting"].pop(0)
                monkeys[i]["count"] += 1
            else:
                monkeys[monkeys[i][0]]["Starting"].append(new)
                monkeys[i]["Starting"].pop(0)
                monkeys[i]["count"] += 1

counts = []
for monkey in monkeys:
    counts.append(monkeys[monkey]["count"])

print(sorted(counts)[-2] * sorted(counts)[-1])
