# Daily summaries
## Day 1: Calorie Counting
### Part 1
- String parsing to get max of groups
- Can redo with more concise code

### Part 2
- Get the top 3 of a list

## Day 2: Rock Paper Scissors
### Part 1
- Following rule set to get scores

### Part 2
- Following another rule set

## Day 3: Rucksack Reorganization
### Part 1 
- Find the common element (Use set operations)

### Part 2
- 3 way set intersection

## Day 4: Camp Cleanup
### Part 1 
- Get pairs that have ranges that completely overlap (Inequalities problem)

### Part 2
- Get pairs that have ranges the partially overlap (Inequalities problem)
## Day 5: Supply Stacks
### Part 1
- Parsing a string image (Should just manually input it into a list)
- Stack tracking (Individual boxes moved at a time for each stack)

### Part 2
- Whole stack moved at the same time

## Day 6: Tuning Trouble
### Part 1
- String parsing and using sets to get unique elements

### Part 2
- Longer string parsing and using sets to get unique elements

## Day 7: No Space Left On Device
### Part 1
- Tree structured filesystem
- Input is in a depth-first-search structure
- Have a tracker for current folder directory
- Ignore dir lines (Only consider file sizes or cd commands)
- Use cd .. commands to propogate up the child directory size to the parent
- Dictionary to keep track of each directoy's size

### Part 2
- Minimum value of a list comprehension

## Day 8 - Treetop Tree House
### Part 1
- Tree visibilty from the edges
- Create 4 functions to look at each direction (Alternative is to rotate the grid)
- Use of all function in list comprehension 

### Part 2
- Tree visibility from each tree
- Create 4 functions to look at each direction (Alternative is to rotate the grid)

## Day 9 - Rope bridge
### Part 1 
- Short rope physics
- Using complex numbers to track 2D movement
- Use the delta and a sign function to get new position of tail

### Part 2
- 9 sectioned rope tracked using a list.

## Day 10 - Cathode Ray Tube
### Part 1
- Cycle tracking with modulo to get X at every 40 cycles.

### Part 2
- Get the letters produced from grid ASCII art

## Day 11 - Monkey in the Middle
### Part 1
- String parsing for monkeys throwing items around

### Part 2
- Modulo lowest common multiple hack to limit worry levels tracking
- functools.reduce to multiply each element in a list

## Day 12 - Hill Climbing Algorithm
### Part 1
- Dijkstra's on elevation grid
- Can also do it via a very light-weight BFS
    - Dijkstra's is  a BFS algorithm. Anytime a point gets added to the stack, it has actually found the shortest distance to that point. 
    - Implementing Dijkstra's via BFS is very helpful. 
- Creative way in handling directional movement with complex numbers, and handling cases when you are on the edge.

### Part 2
- If done via BFS, can just do a BFS for each "a" position given it is very light-weight.
- Dijkstra for each point is a lot slower.

## Day 13 - Distress Signal
### Part 1
- Comparing pairs of lists
- Using eval to parse string input of nested lists
- Unpacking operator * on map function into a list
- Match case with recursion

### Part 2
- Bubble sort

## Day 14 - Regolith Reservoir
### Part 1
- Sand falling physics. Find when the mound doesn't change anymore.
- String parsing (Can perhaps use list comprehension within list comprehension instead)
- Grid filling based on straight line coordinates
- Define my own fall function. 
    - Can redefine the void falling condition as falling below the minimum y coordinate rock
    - Can do a neat trick by defining dx, dy as all the possible fall directions checked in the correct order [(0,1), (-1,1), (1,1)]. If it is air for any of them, break/continue. 

### Part 2 
- No longer infinite void, has a base. Find when the mound covers the source.
- Finding max value of y coordinate in (x, y) dictionary keys

## Day 15 - Beacon Exclusion Zone
### Part 1
- Sensor beacon pairs that map the radius using Manhattan distance.
- Find where a beacon cannot be in a given row.
- Manhattan distances have some nice properties which can be used to solve the problem.

### Part 2
- Find the unique position in an area where the beacon has to be.
- Massive search space that cannot be brute forced.
- Problem solve to reduce the search space.
    - Can also use Z3 solver as another method


## Day 16 - Proboscidea Volcanium
### Part 1
- Stack-based DFS of a cave system traversal. Find the maximum pressure released possible. (Try recursion-based DFS in future?)
- 4 dimensional state vector.
- Dynamic node values for each step.
- 45+ nodes at depth 30.
- Floyd-Warshal algorithm (Shortest distance from any node to any node) to create smaller subgraph of 15~ nodes

### Part 2
- Introduction of an elephant that can also make decisions. (Blows up complexity)
- 6 dimensional state vector
- Heuristic used as original solution took too long (2.5 hours) and was wrong (Possible edge case when my time has run out, but not the elphants)
    - Heuristic - Rerun part 1 twice, where the opened valves of the first run is removed from the second run.
    - This greedy approach may not always work (Worked for my input data so...)
    - Branch pruning required


## Day 17 - Pyroclastic Flow
### Part 1
- Tetris with a cyclic rock/move set and start positions based on the stack height. (No rotations)
- Finding the stack height after 2022 rocks

### Part 2
- Finding the stack height after 1 million million rocks
- Cannot iterate, so must find repeating state given the move/block set is cyclic.
- State is defined by (top_stack, rock_index, move_index) with a top_stack depth of 50.
- Finicky to get all the relevant quantities 
    - Index for when the cycle begins (The first state to be seen twice)
    - Cycle length
    - Height added after each cycle
    - Starting height for when cycle begins
    - Remanining height added to get to the 1,000,000,000,000th block 

## Day 18 - Boiling Boulders
### Part 1 
- Get neighbours of each lava droplet to see if it is exposed to air.
    - Lambda function for 3D neighbours with unpacking operator (6 directions)
- 1 liner for a nested for-loop

### Part 2
- Flood fill to get only the exterior surface area.
- Bug fix: Ensure the stack only contains unique elements to prevent double counting!


## Day 19 - Not Enough Minerals
### Part 1
- Stack-based BFS of finding the maximuim geode mined by a blueprint at depth 24.
- Optimisation required with branch pruning
    - No need to build more robots than the maximum possible expenditure of that ore for a turn
    - Cut a branch short if it can never reach the current geode maximum
- Other optimisation methods
    - Can reduce the search space dimensionality by adding the cumulative geodes mined by a geo_bot for the time remaning and removing the need to track the number of geo_bots. (This can collapse different states in higher dimension to the same one in lower dimension)
    - “if you choose not to build a machine but could have then don’t build that machine until you’ve built something else”.
- When implementing search algorithms, always include a SEEN set. Only add a state to the stack iff it is both not in the stack and not in SEEN. This HEAVILY speeds up the algorithm due to massive possibilities of double-counting states.

### Part 2
- Depth of 32. Only 3 blueprints rather than 30. No changes required


## Day 20 - Grove Positioning System
### Part 1
- Shuffling of a circular list
    - "the list is circular, so moving a number off one end of the list wraps back around to the other end as if the ends were connected."
- Shuffle/Perform operations on the index list, which is the index map to the original list, in the original list order.
    - Should rename variable move to new_index for clarity
- Modulo operator to model circular list. Two edge cases:
    - Requires an if statement that if it moves to position 0, it moves to the end of the list
    - modulo len(list)-1 given Python indexing. (End of list index moves it to the start of the list)

### Part 2
- Number of moves is multiplied (Doesn't change code given modulus operator)
- 10 rounds of shuffling


## Day 21 - Monkey Math 
### Part 1
- Recursion and use of case match to evaluate root node.
- Can recode using try-except with eval

### Part 2
- No longer evaluating, but solving.
- Cannot brute force as solution is in 10*e9 magnitude
- Have to output the whole equation as a string and solve for x.
    - Recursion is now return a string rather than an evaluated expression
    - Have to remember PEDMAS and include brackets
- Used mathpapa (External. Not sure why sympy solver fails) to solve the  equation


## Day 22 - Monkey Map
### Part 1
- Traversing along a 2D board according to instructions.
- If hit a wall, stop.
- Going off the board wraps around to the opposite edge to the direction you are facing.

### Part 2
- Traversing along a 3D cube folded according to the 2D board.
- Label each face, and each off-board edge.
- Going off the board now corresponds to getting placed in one of the other off-board edges according to how the cube is folded.
    - Each 14 cases hard-coded in.
        - New coordinates on the board
        - New orientation/direction
    - Bugs galore (Are the new coordinates correct? Is the new direction on the new face correct?) 

## Day 23 - Unstable Diffusion
### Part 1
- Elves on a grid want to "spread out" according to a rule set.
- If two or more elves propose to go on a coordinate, they stay put. Need a counter for each position, as well as keeping track of where they were originially.

### Part 2
- When does the grid reach equilibrium.
- Have the grove as a set rather than dic. Makes checking condition much faster rather than calculating list comprehension each iteration.

## Day 24 - Blizzard Basin
- Dont need to check if next state is in stack, add that state into seen when it gets added to the stack.
### Part 1
- Stack based BFS. Finding the shortest path to get from start to end, where the obstacles are dynamic.
- BFS >> DFS for shortest path questions (We only need to find the earliest branch that hits the end. BFS does earliest branches first)
- Complex numbers to encode positions, as well as the deltas of moving.
- Seen set is (coordinate, step). (The step encodes everything about the blizzard locations)
    - BFS also means that we don't need to compute the blizzard locations every iteration, only every change in step.
- Create an occupied set, rather than checking if adj is in tuple([blizzards[key][0] for key in sorted(blizzards.keys())]) every iteration.
    - Drastically improves solving time

### Part 2
- Go to the end, then back to the start, and back to the end.
- Key trick: Restart the stack once you hit the end/back the first time. (The rest of the branches no longer matter)

## Day 25 - Full of Hot Air
- Converting from "SNAFU" to decimal, and from decimal to "SNAFU".
    - SNAFU to decimal is trivial: Sum up each digit value
    - Decimal to SNAFU: Get the total modulo 5 (Remainder). That dictates what the next least significant figure is in SNAFU. 
