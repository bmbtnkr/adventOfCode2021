with open('07.txt', 'r') as f:
    data = f.readlines()[0].split(',')

pos = [int(i) for i in data]
pos = [16,1,2,0,4,2,7,1,2,14] # test data
pos = sorted(pos)

# part 1
min_fuel = [0, float('inf')]

for p in range(max(pos)+1):
    total_fuel = 0
    for i in range(len(pos)):
        total_fuel += abs(pos[i] - p)

    if total_fuel < min_fuel[1]:
        min_fuel[0] = p
        min_fuel[1] = total_fuel

print(min_fuel)


# part 2 
min_fuel = [0, float('inf')]

for p in range(max(pos)+1):
    total_fuel = 0
    for i in range(len(pos)):
        n = abs(pos[i] - p)
        # additional summation
        total_fuel += (n**2+n)//2

    if total_fuel < min_fuel[1]:
        min_fuel[0] = p
        min_fuel[1] = total_fuel

print(min_fuel)
