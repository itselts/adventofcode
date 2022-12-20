from collections import defaultdict

folders = defaultdict(int)
cur = ""


for i, line in enumerate(open("./input.csv").read().splitlines()):
    if line.startswith("$ cd /"):
        cur = "root"
    elif line.startswith("$ cd"):
        if line.startswith("$ cd .."):
            child = cur
            parent = "/".join(cur.split("/")[:-1])
            folders[parent] += folders[child]
            cur = parent
            #if cur == "root":
                #folders["root"] += folders[parent]
        else:
            cur = cur + "/" + line[5:]
    elif not line.startswith("dir") and not line.startswith("$"):
        size = int(line.split(" ")[0])
        folders[cur] += size



tot = 0
for folder in folders:
    if folders[folder] <= 100000:
        tot += folders[folder]

print(tot)


# part 2
free = 70000000 - folders['root']
possible = defaultdict(int)

print(min(x for x in folders.values() if free + x >= 30000000))
