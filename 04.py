from pprint import pprint
import numpy as np

data = []
file_path = '04.txt'
with open(file_path, 'r') as f:
    for line in f.readlines():
        if line.strip().split():
            data.append(line.strip().split())

input_nums = [int(i) for i in data[0][0].split(',')]
input_boards = data[1:]

class BingoBoard(object):
    def __init__(self, grid):
        # self.dataset = dataset
        self.grid = np.array(grid)
        self.empty_grid = np.chararray((5,5))
        self.winning_num = None

    def get_position(self, n):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                if n in self.grid[row] and self.grid[row][column] == n:
                    return row, column

    def get_num(self, x, y):
        return self.grid[x][y]

    def fill_in_num(self, n):
        if self.get_position(n):
            row, col = self.get_position(n)
            self.empty_grid[row][col] = 'x'

    def check_board(self, n):
        full_row = np.chararray((5,))
        full_row[:] = 'x'
    
        for row in range(len(self.grid)):
            if all(self.empty_grid[row] == full_row):
                self.winning_num = n
                return True

        for column in range(len(self.grid.T)):
            if all(self.empty_grid.T[column] == full_row):
                self.winning_num = n
                return True

        return False

size = 5
l = []
boards = []

for i in range(len(input_boards)):
    if i % size == 0:
        l.clear()

    l.append([int(j) for j in input_boards[i]])

    if i % size == size-1:
        board = BingoBoard(l[:])
        boards.append(board)

def play_bingo(input_nums, boards):
    for n in input_nums:
        for b in boards:
            b.fill_in_num(n)
            if b.check_board(n):
                return b

board_inst = play_bingo(input_nums, boards)

def get_unmarked_sum(board):
    grid = board.grid
    empty_grid = board.empty_grid
    winning_num = board.winning_num

    unmarked_sum = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if not empty_grid[row][column] == b'x':
                unmarked_sum += grid[row][column]

    return unmarked_sum, winning_num, unmarked_sum * winning_num

print(get_unmarked_sum(board_inst))

# part 2
def play_bingo(input_nums, boards):
    winning_boards = []

    for n in input_nums:
        for b in boards:
            b.fill_in_num(n)
            if b.check_board(n):
                if b not in winning_boards:
                    winning_boards.append(b)

                if len(winning_boards) == len(boards):
                    return winning_boards

    return winning_boards

winning_boards = play_bingo(input_nums, boards)
last_board = list(winning_boards)[-1]
print(get_unmarked_sum(last_board))
