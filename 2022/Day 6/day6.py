data = list(open("./input.csv").read())

i=4
while data:
    if len(set(data[:4])) == 4:
        print(i)
        break
    else:
        del data[0]
        i += 1

data = list(open("./input.csv").read())

i=14
while data:
    if len(set(data[:14])) == 14:
        print(i)
        print(set(data[:14]))
        break
    else:
        del data[0]
        i += 1