import numpy as np
import math


lines = []
with open('09.txt', 'r') as f:
    for line in f.readlines():
        lines.append([int(i) for i in line.strip()])


grid = np.array(lines)


# ======================================================================================================================
def get_neighbors(grid, row, col):
    neighbors = []
    neighbors.append(grid[row-1][col]) if row > 0 else None # up
    neighbors.append(grid[row+1][col]) if row < len(grid)-1 else None # down
    neighbors.append(grid[row][col-1]) if col > 0 else None # left
    neighbors.append(grid[row][col+1]) if col < len(grid[row])-1 else None # right
    return neighbors

def part_one():
    low_peaks = 0

    # brute force
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            val = grid[row][col]
            neighbors = get_neighbors(grid, row, col)
            if val < min(neighbors):
                low_peaks += val + 1

    return low_peaks
# ======================================================================================================================

def get_neighbor_positions(grid, row, col):
    neighbors = []
    neighbors.append((row-1,col)) if row > 0 else None # up 
    neighbors.append((row+1,col)) if row < len(grid)-1 else None # down
    neighbors.append((row,col-1)) if col > 0 else None # left
    neighbors.append((row,col+1)) if col < len(grid[row])-1 else None # right
    return neighbors


def find_low_peaks(grid):
    low_peaks = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            val = grid[row][col]
            neighbors = get_neighbor_positions(grid, row, col)
            neighbor_vals = [grid[n[0]][n[1]] for n in neighbors]
            if val < min(neighbor_vals):
                low_peaks.append((row, col))

    return low_peaks

# quick and dirty recursive method
# I know it's bad form to put a mutable list as an method args :(
def get_basin(grid, pos, visited=[]):
    row, col = pos[0], pos[1]
    val = grid[row][col]

    # base case: already visited
    if pos in visited:
        return None

    # base case: number is 9
    if val == 9:
        return None

    # base case: all neighbors are 9
    neighbors = get_neighbor_positions(grid, row, col)
    neighbor_vals = [grid[n[0]][n[1]] for n in neighbors]

    if neighbor_vals[0] == 9 and neighbor_vals.count(neighbor_vals[0]) == len(neighbor_vals):
        return None

    # recursive case: recur the closest neighbor
    visited.append(pos)

    for n in neighbors:
        get_basin(grid, n, visited)

    return visited


def part_two():
    low_peaks = find_low_peaks(grid)
    basin_sizes = [len(get_basin(grid, peak, [])) for peak in low_peaks]
    return math.prod(sorted(basin_sizes)[-3:])


print(part_one())
print(part_two()) # suprisingly fast