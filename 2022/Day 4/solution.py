with open("input.csv") as f:
    s = f.read().strip()

s = s.split("\n")

c = 0
for l in s:
    a,b = l.split(",")
    a1,a2 = map(int,a.split("-"))
    b1,b2 = map(int,b.split("-"))
    if a1 <= b1 <= b2 <= a2 or (
        b1 <= a1 <= a2 <= b2):
        c += 1
print(c)

c = 0
for l in s:
    a,b = l.split(",")
    a1,a2 = map(int,a.split("-"))
    b1,b2 = map(int,b.split("-"))
    if a2 >= b1 and a1 <= b2 or (
        b2 >= a1 and b1 <= a2):
        c += 1
print(c)