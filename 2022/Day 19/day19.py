from collections import deque
from datetime import datetime
import functools

startTime = datetime.now()

data = open("./input.csv").read().splitlines()
blueprints = {}


for line in data:
    num = int(line.split()[1].replace(":", ""))
    ore_rob = int(line.split()[6])
    clay_rob = int(line.split()[12])
    obs_rob = (int(line.split()[18]), int(line.split()[21]))
    geo_rob = (int(line.split()[27]), int(line.split()[30]))

    blueprints[num] = {"ore_rob": ore_rob, "clay_rob": clay_rob, "obs_rob": obs_rob, "geo_rob": geo_rob}

part2 = True
def dfs(blueprint):
    # State vector: (ore, clay, obisidian, geode, ore robots, clay robots, obisidian robots, geode robots, time left)
    if part2 == False:
        stack = deque([(0,0,0,0,1,0,0,0,24)])
    else:
        stack = deque([(0,0,0,0,1,0,0,0,32)])
    seen = set()
    max_geode = 0
    print(blueprint)

    # optimizing parameters
    most_ore = max((blueprint['ore_rob'], blueprint['clay_rob'], blueprint['obs_rob'][0], blueprint['geo_rob'][0]))
    most_clay = blueprint['obs_rob'][1]
    most_obs = blueprint["geo_rob"][1]

    while stack:
        cur = stack.pop()
        ore, clay, obsidian, geode, ore_rob, clay_rob, obs_rob, geo_rob, t = cur
        seen.add(cur)

        if geode > max_geode:
            max_geode = geode

        # Everything that can happen in the next minute
        if t >= 1:

            # Pruning heuristic
            if sum(i for i in range(1,t)) + t*geo_rob + geode < max_geode: 
                continue

            # Do nothing
            if (ore <= most_ore) or (clay <= most_clay) or (obsidian <= most_obs):
                new = (ore+ore_rob, clay+clay_rob, obsidian+obs_rob, geode+geo_rob, ore_rob, clay_rob, obs_rob, geo_rob, t-1)
                if (new not in stack) and (new not in seen):
                    stack.append(new)

            # Build ore robot
            if ore >= blueprint['ore_rob'] and ore_rob < most_ore:
                new = (ore-blueprint['ore_rob']+ore_rob, clay+clay_rob, obsidian+obs_rob, geode+geo_rob, ore_rob+1, clay_rob, obs_rob, geo_rob, t-1)
                if (new not in stack) and (new not in seen):
                    stack.append(new)

            # Build clay robot
            if ore >= blueprint['clay_rob'] and clay_rob < most_clay:
                new = (ore-blueprint['clay_rob']+ore_rob, clay+clay_rob, obsidian+obs_rob, geode+geo_rob, ore_rob, clay_rob+1, obs_rob, geo_rob, t-1)
                if (new not in stack) and (new not in seen):
                    stack.append(new)

            # Build obisidian robot
            if (ore >= blueprint['obs_rob'][0]) and (clay >= blueprint['obs_rob'][1]) and obs_rob < most_obs:
                new = (ore-blueprint['obs_rob'][0]+ore_rob, clay-blueprint['obs_rob'][1]+clay_rob, obsidian+obs_rob, geode+geo_rob, ore_rob, clay_rob, obs_rob+1, geo_rob, t-1)
                if (new not in stack) and (new not in seen):
                    stack.append(new)

            # Build geode robot
            if (ore >= blueprint['geo_rob'][0]) and (obsidian >= blueprint['geo_rob'][1]):
                new = (ore-blueprint['geo_rob'][0]+ore_rob, clay+clay_rob, obsidian-blueprint['geo_rob'][1]+obs_rob, geode+geo_rob, ore_rob, clay_rob, obs_rob, geo_rob+1, t-1)
                if (new not in stack) and (new not in seen):
                    stack.append(new)

    return  max_geode


if part2 == False:
    print(sum(blueprint*dfs(blueprints[blueprint]) for blueprint in blueprints))
    print(datetime.now() - startTime)
else:
    print(functools.reduce(lambda x, y: x*y, [dfs(blueprints[blueprint]) for blueprint in blueprints if blueprint in [1,2,3]]))
    print(datetime.now() - startTime)