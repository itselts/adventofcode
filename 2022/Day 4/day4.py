path = "C:/Users/Elton/Documents/GitHub/adventofcode/2022/Day 4/"

with open(path+"input.csv") as file:
    data = file.read().splitlines()

tot1 = 0
def is_contained(input):
    a1, a2 = input.split(",")
    
    p1, p2 = map(int,a1.split("-"))
    p3, p4 = map(int,a2.split("-"))

    #if (p1 <= p3 and p2 >= p4) or (p3 <= p1 and p4 >= p2):
    if (p1 <= p3 <= p4 <= p2) or (p3 <= p1 <= p2 <= p4):    
        return True
    else:
        return False

for i in data:
    tot1 += is_contained(i)
print(tot1)


tot2 = 0
def is_overlap(input):
    a1, a2 = input.split(",")
    
    p1, p2 = map(int,a1.split("-"))
    p3, p4 = map(int,a2.split("-")) 

    if (p1 <= p3 and p3 <= p2) or (p3 <= p1 and p1 <= p4):
        return True
    else:
        return False

for i in data:
    tot2 += is_overlap(i)
print(tot2)