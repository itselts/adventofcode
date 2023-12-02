with open('input.txt') as f:
    sum = 0
    for line in f.read().splitlines():
        l, ll = 0, True
        r, rr = 0, True
        for i in range(len(line)):
            print(i, line[i], line[~i])
            if ll or rr:
                if ll and line[i].isdigit():
                    l = i
                    ll = False
                if rr and line[~i].isdigit():
                    r = i
                    rr = False
        sum += int(line[l] + line[~r])
