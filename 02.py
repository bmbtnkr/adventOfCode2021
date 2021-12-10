data = []

file_path = '02.txt'
# file_path = '02_test.txt'

with open(file_path, 'r') as f:
    for i in f.readlines():
        data.append(i.split())


# part 1
position, depth = 0, 0
for i in range(len(data)):
    if 'forward' in data[i]:
        position += int(data[i][1])
    else:
        if 'up' in data[i]:
            depth -= int(data[i][1])
        if 'down' in data[i]:
            depth += int(data[i][1])
    # print(data[i], position, depth)

print(position)
print(depth)
print(position*depth)
print()


position, depth, aim = 0, 0, 0
for i in range(len(data)):
    movement, x = data[i]
    x = int(x)

    if 'forward' in movement:
        position += x
        depth += (aim * x)

    if 'up' in movement:
        # depth -= x
        aim -= x

    if 'down' in movement:
        # depth += x
        aim += x

    # print(data[i])
    # print(f'position: {position}, depth: {depth}, aim: {aim}')

print(position)
print(depth)
print(position*depth)