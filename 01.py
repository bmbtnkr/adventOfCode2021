data = []

with open('01.txt', 'r') as f:
    for i in f.readlines():
        data.append(int((i).replace('\n', '')))

# data = [199,200, 208, 210, 200, 207, 240, 269, 260, 263] 

# part 1
def calc_depth(data):
    count = 0

    for i in range(len(data)):
        if data[i] > data[i-1]:
            count+=1

    return count

print(calc_depth(data))


# part 2
import numpy as np

def moving_data(data, kernel=3):
    l = []
    for i in range(kernel-1, len(data)):
        data_sum = 0
        for j in range(kernel):
            data_sum += data[i-j]
        l.append(data_sum)
    return l

# print(calc_depth(moving_data(data)))

data = moving_data(data)
print(calc_depth(data))

# print(np.array(np.random.rand(10)))


# 1477, 1523