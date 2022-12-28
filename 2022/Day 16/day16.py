import re 
import collections
from datetime import datetime 

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


# Floyd-Warshall algorithm
dist = {valve: {adj: 1 if adj in graph[valve] else (0 if valve == adj else float('+inf')) for adj in graph} for valve in graph} 

for k in graph:
    for i in graph:
        for j in graph:
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


T = {valve for valve in graph if flow[valve] != 0} # Set of valves with non-zero flow


# DFS (add and remove at the same end)
startTime = datetime.now()
max_pressure = 0
part2 = True

if part2 == False:
    stack = [("AA", {"AA"}, 0, 30)]
    while stack:
        cur_node, opened, tot_pressure, mins = stack.pop()

        if tot_pressure >= max_pressure:
            max_pressure = tot_pressure

        for next_node in graph: # Next node is the next valve to open
            if (next_node in T) and (next_node not in opened) and (mins-1-dist[cur_node][next_node] > 0):
                new_opened = set(opened)
                new_opened.add(next_node)
                stack.append((next_node, new_opened, 
                tot_pressure + flow[next_node]*(mins-1-dist[cur_node][next_node]), 
                mins-1-dist[cur_node][next_node]))
else:
    stack = collections.deque([(("AA", "AA"), {"AA"}, 0, (26, 26))])
    while stack:
        (my_node, elephant_node), opened, tot_pressure, (my_mins, elephant_mins) = stack.pop()

        if tot_pressure >= max_pressure:
            max_pressure = tot_pressure

        for my_next in graph: # Next node is the next valve to open for me 
            for elephant_next in graph:
                if (my_next in T) and (elephant_next in T) and (my_next not in opened) and (elephant_next not in opened) and (my_mins-1-dist[my_node][my_next] > 0) and (elephant_mins-1-dist[elephant_node][elephant_next] > 0) and (my_next != elephant_next):
                    new_opened = set(opened)
                    new_opened.add(my_next)
                    new_opened.add(elephant_next)

                    stack.append(((my_next, elephant_next), new_opened,
                    tot_pressure + flow[my_next]*(my_mins-1-dist[my_node][my_next]) + flow[elephant_next]*(elephant_mins-1-dist[elephant_node][elephant_next]),
                    (my_mins-1-dist[my_node][my_next], elephant_mins-1-dist[elephant_node][elephant_next])))
            


print(max_pressure)
print(datetime.now() - startTime)


