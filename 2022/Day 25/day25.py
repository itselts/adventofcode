snafu = [list(x.strip()) for x in open("./input.csv").read().splitlines()]
# print(snafu)

map = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
inverse = {v: k for k,v in map.items()}

decimal = []

for num in snafu:
    dec = 0
    for i,x in enumerate(num[::-1]):
        dec += map[x] * (5 ** i)
    decimal.append(dec)

total = sum(decimal)
print(total)

snafu_num = []
while total:
    d = total % 5
    match d:
        case 0:
            snafu_num.append("0")
        case 1:
            snafu_num.append("1")
        case 2:
            snafu_num.append("2")
        case 3:
            snafu_num.append("=")
            total += 2
        case 4:
            snafu_num.append("-")
            total += 1
    total //= 5

print("".join(snafu_num[::-1]))
    

