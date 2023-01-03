from sympy.solvers import solve
from sympy import Symbol

input = open("./input.csv").read().splitlines()

monkeys = {}
for line in input:
    monkey, operation = line.split(": ")
    if operation.isnumeric():
        monkeys[monkey] = int(operation)
    else:
        monkeys[monkey] = operation.split(" ")


def rec(monkey, monkeys):
    o = monkeys[monkey]

    match o:
        case int():
            return o
        case list():
            match o[1]:
                case "+":
                    return rec(o[0], monkeys) + rec(o[2], monkeys)
                case "-":
                    return rec(o[0], monkeys) - rec(o[2], monkeys)
                case "*":
                    return rec(o[0], monkeys) * rec(o[2], monkeys)
                case "/":
                    return rec(o[0], monkeys) / rec(o[2], monkeys)

print(int(rec("root", monkeys)))


# Part 2
def rec2(monkey, monkeys):
    o = monkeys[monkey]

    if monkey == "root":
        return (rec2(o[0], monkeys), rec2(o[2], monkeys))

    match o:
        case int():
            return str(o)
        case list():
            match o[0]:
                case "humn":
                    match o[1]:
                            case "+":
                                return "(x+" + rec2(o[2], monkeys) + ")"
                            case "-":
                                return "(x-" + rec2(o[2], monkeys) + ")"
                            case "*":
                                return "(x*" + rec2(o[2], monkeys) + ")"
                            case "/":
                                return "(x/" + rec2(o[2], monkeys) + ")"
            match o[2]:
                case "humn":
                    match o[1]:
                            case "+":
                                return "(" + rec2(o[0], monkeys) + "+n)"
                            case "-":
                                return "(" + rec2(o[0], monkeys) + "-n)"
                            case "*":
                                return "(" + rec2(o[0], monkeys) + "*n)"
                            case "/":
                                return "(" + rec2(o[0], monkeys) + "/n)"
            match o[1]:
                case "+":
                    return "(" + rec2(o[0], monkeys) + "+" + rec2(o[2], monkeys) + ")"
                case "-":
                    return "(" + rec2(o[0], monkeys) + "-" + rec2(o[2], monkeys) + ")"
                case "*":
                    return "(" + rec2(o[0], monkeys) + "*" + rec2(o[2], monkeys) + ")"
                case "/":
                    return "(" + rec2(o[0], monkeys) + "/" + rec2(o[2], monkeys) + ")"


#x = Symbol('x')
#print(solve("("+(rec2("root", monkeys)[0]+")"+"-("+rec2("root", monkeys)[0])+")", x))

print(rec2("root", monkeys)[0]+ "=" + rec2("root", monkeys)[1])
# paste into https://www.mathpapa.com/simplify-calculator/