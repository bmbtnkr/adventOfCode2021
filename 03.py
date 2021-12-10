from pprint import pprint
import numpy as np

data = []
file_path = '03.txt'
with open(file_path, 'r') as f:
    for line in f.readlines():
        data.append((line.strip()))

# data = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

# -----------------------------------------------
# faster solution
# -----------------------------------------------

def get_min_max_values(l, binary=True, end_early=False):
    max_str = ''
    min_str = ''
    for i in l:
        max_str += max(i, key=i.count)
        min_str += min(i, key=i.count)
        if end_early: break

    # convert str binary to int
    if binary:
        max_val = int(max_str, 2)
        min_val = int(min_str, 2)
        return max_val, min_val

    return max_str, min_str

# transpose data
t_data = [''.join(i) for i in zip(*data)]
a, b = get_min_max_values(t_data, binary=True)
print(a, b, a*b)

# ===============================================
# Part 2
# ===============================================
def get_life_support_rating_item(data, get_max=True):
    position = 0
    data_copy = data[:]

    while len(data_copy) > 1:
        # transpose
        t_data = [''.join(i) for i in zip(*data_copy)]
        
        # get min, max values
        a, b = get_min_max_values(t_data, binary=False)

        if get_max:
            remover = int(a[position])
            if int(a[position]) == int(b[position]):
                remover = 1
        else:
            remover = int(b[position])
            if int(a[position]) == int(b[position]):
                remover = 0            

        # remove any num from list without a in current position
        data_copy = [x for x in data_copy if x[position] == str(remover)]
        
        position += 1

    return data_copy[0]

o2 = get_life_support_rating_item(data, get_max=True)
co2 = get_life_support_rating_item(data, get_max=False)

o2, co2 = int(o2, 2), int(co2, 2)
print(o2, co2, o2*co2)
