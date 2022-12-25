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
- String parsing for monkeys

### Part 2
- Modulo lowest common multiple hack to limit worry levels tracking
- functools.reduce to multiply each element in a list

## Day 12 - Hill Climbing Algorithm
### Part 1
- Dijkstra's on elevation grid

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
- Sand falling
- String parsing (Can perhaps use list comprehension within list comprehension instead)
- Grid filling based on straight line coordinates
- Define my own fall function. 
    - Can redefine the void falling condition as falling below the minimum y coordinate rock
    - Can do a neat trick by defining dx, dy as all the possible fall directions checked in the correct order [(0,1), (-1,1), (1,1)]. If it is air for any of them, break/continue. 

### Part 2 
- No longer infinite void, has a base
- Finding max value of y coordinate in (x, y) dictionary keys