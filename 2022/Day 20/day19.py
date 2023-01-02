encrypted = [int(x) for x in open("./input.csv").read().splitlines()]

#print(len([i for i, x in enumerate(encrypted) if x==0]))
#print(len(set(encrypted))) # Values are not unique, except 0!.

indicies = list(range(len(encrypted)))

# REMEMBER, the list is circular, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.
for i, x in enumerate(encrypted):
    indicies.pop(cur := indicies.index(i))
    move = (cur+x) % (len(encrypted)-1) # Position (len(encrypted)-1) (AKA end of the list) is the start of the list
    if move == 0: # Position 0 is the end of the list.
        indicies.insert(len(encrypted)-1, i)
    else:
        indicies.insert(move, i)

decrypted = [encrypted[i] for i in indicies]
zero_index = decrypted.index(0)
print(sum([decrypted[(zero_index+x) % len(decrypted)] for x in [1000, 2000, 3000]]))


# Part 2
encrypted2 = [int(x)*811589153 for x in open("./input.csv").read().splitlines()]
indicies = list(range(len(encrypted2)))

# REMEMBER, the list is circular, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.
for _ in range(10):
    for i, x in enumerate(encrypted2):
        indicies.pop(cur := indicies.index(i))
        move = (cur+x) % (len(encrypted2)-1) # Position (len(encrypted)-1) (AKA end of the list) is the start of the list
        if move == 0: # Position 0 is the end of the list.
            indicies.insert(len(encrypted2)-1, i)
        else:
            indicies.insert(move, i)

decrypted2 = [encrypted2[i] for i in indicies]
zero_index2 = decrypted2.index(0)
print(sum([decrypted2[(zero_index2+x) % len(decrypted2)] for x in [1000, 2000, 3000]]))