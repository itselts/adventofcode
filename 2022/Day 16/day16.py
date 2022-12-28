import re 

data = open("./input.csv").read().split("\n")

flow = {} # Flow of each valve
graph = {} # Adjacency dictionary of each room

for line in data:
    f, g = line.split(";")
    flow[f[6:8]] = int(f.split("=")[-1])
    g = g.replace("valves", "valve")
    g = g.replace("tunnels", "tunnel")
    g = g.replace("leads", "lead")
    graph[f[6:8]] = g.replace(" tunnel lead to valve ", "").split(", ")

print(graph)

dists = {}

for valve in flow:
    if flow[valve] and valve != "AA":
        continue

    dists[valve] = {valve: 0}