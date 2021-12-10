import numpy as np
from pprint import pprint

fish = [3,4,3,1,2]
fish = [2,5,3,4,4,5,3,2,3,3,2,2,4,2,5,4,1,1,4,4,5,1,2,1,5,
2,1,5,1,1,1,2,4,3,3,1,4,2,3,4,5,1,2,5,1,2,2,5,2,4,4,1,4,5,
4,2,1,5,5,3,2,1,3,2,1,4,2,5,5,5,2,3,3,5,1,1,5,3,4,2,1,4,4,
5,4,5,3,1,4,5,1,5,3,5,4,4,4,1,4,2,2,2,5,4,3,1,4,4,3,4,2,1,
1,5,3,3,2,5,3,1,2,2,4,1,4,1,5,1,1,2,5,2,2,5,2,4,4,3,4,1,3,
3,5,4,5,4,5,5,5,5,5,4,4,5,3,4,3,3,1,1,5,2,4,5,5,1,5,2,4,5,
4,2,4,4,4,2,2,2,2,2,3,5,3,1,1,2,1,1,5,1,4,3,4,2,5,3,4,4,3,
5,5,5,4,1,3,4,4,2,2,1,4,1,2,1,2,1,5,5,3,4,1,3,2,1,4,5,1,5,
5,1,2,3,4,2,1,4,1,4,2,3,3,2,4,1,4,1,4,4,1,5,3,1,5,2,1,1,2,
3,3,2,4,1,2,1,5,1,1,2,1,2,1,2,4,5,3,5,5,1,3,4,1,1,3,3,2,2,
4,3,1,1,2,4,1,1,1,5,4,2,4,3]


fish = np.array(fish, dtype=np.byte)

"""
# part 1
days = 80
for day in range(days):
    for f in range(len(fish)):
        if fish[f] == 0:
            fish[f] = 6
            fish = np.append(fish, 8)
        else:
            fish[f] -= 1
print(len(fish))
"""

# part 2: use a hashmap
fish_dict = {k:0 for k in range(9)}
for i in fish:
    fish_dict[i] += 1

days = 80
for day in range(days):
    zeros = fish_dict[0]
    for i in range(1, 9):
        fish_dict[i-1] = fish_dict[i]
    fish_dict[8] = zeros
    fish_dict[6] += zeros

print(sum(fish_dict.values()))



