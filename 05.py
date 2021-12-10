import numpy as np
from pprint import pprint


INPUT_FILE_PATH = '05.txt'
GRID_SIZE = 1000

INPUT_FILE_PATH = '05_test.txt'
GRID_SIZE = 10

with open(INPUT_FILE_PATH) as f:
    content = f.readlines()
    start_list = [i.split()[0].split(',') for i in content]
    end_list = [i.split()[-1].split(',') for i in content]

grid = np.zeros(shape=(GRID_SIZE, GRID_SIZE), dtype=np.uint8)


def main():
    for index, (i, j) in enumerate(zip(start_list, end_list)):
        x1, y1 = [int(n) for n in i]
        x2, y2 = [int(n) for n in j]

        # # vertical
        # if x1 == x2:
        #     a, b = min(y1, y2), max(y1, y2)
        #     for i in range(a, b+1):
        #         grid[x1][i] += 1

        # # horizontal
        # elif y1 == y2:
        #     a, b = min(x1, x2), max(x1, x2)
        #     for i in range(a, b+1):
        #         grid[i][y1] += 1

        # diagonal
        # else:
        direction_x, direction_y = np.sign(x2 - x1), np.sign(y2 - y1)
        pos = [x1, y1]

        while pos != [x2, y2]:
            grid[pos[0], pos[1]] += 1
            pos[0] += direction_x
            pos[1] += direction_y
        grid[x2][y2] += 1

    count = 0
    for row in grid:
        for num in row:
            if num > 1:
                count += 1

    print(grid.T)
    print(count)


if __name__ == '__main__':
    main()