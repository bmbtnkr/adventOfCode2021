import numpy as np
import string
import itertools


lines = []
with open('08_test.txt', 'r') as f:
    lines = f.readlines()

# ----------------------------------------------------------------------------------------------------------------------
def part_one():
    d = {2:1, 3:7, 4:4, 7:8} # len(input string): signal number
    result = 0

    for line in lines:
        output_chars = line.strip().split('|')[-1].split()

        for i in output_chars:
            if d.get(len(i)):
                result += 1

    return result
# ----------------------------------------------------------------------------------------------------------------------

# signal number: signal sections
d_decode = {0: [0, 1, 2, 4, 5, 6],
            1: [2, 5],
            2: [0, 2, 3, 4, 6],
            3: [0, 2, 3, 5, 6],
            4: [1, 2, 3, 5],
            5: [0, 1, 3, 5, 6],
            6: [0, 1, 3, 4, 5, 6],
            7: [0, 2, 5],
            8: [0, 1, 2, 3, 4, 5, 6],
            9: [0, 1, 2, 3, 5, 6]
            } 

def display_grid(sections):
    grid = np.empty((6,7), dtype=np.str)

    grid[:] = ' '
    grid[1:5,0] = sections[0]
    grid[0,1:3] = sections[1]
    grid[5,1:3] = sections[2]
    grid[1:5,3] = sections[3]
    grid[0,4:6] = sections[4]
    grid[5,4:6] = sections[5]
    grid[1:5,6] = sections[6]

    grid = grid.T

    for i in grid:
        print(''.join(i))


def get_key(my_dict, value, return_str=False):
    for k, v in my_dict.items():
         if v == value:
             return k
    if return_str:
        return '.'
    return None


def check_section(hint, number_shape, sections):
    for c in hint:
        section = get_key(sections, c)
        signals = d_decode[number_shape]

        if not section in signals:
            # print(f'ERROR: c: {c} section: {section} signals{signals}')
            return False
        return True


def check_grid(sections, input_chars):
    """
    Check known key lengths: len(2) => shape 1 => sections [4,5]
    """
    for hint in sorted(input_chars, key=len):
        if len(hint) == 2: # shape 1 => sections [4,5]
            if not check_section(hint, 1, sections):
                return False

        if len(hint) == 3: # shape 7 => sections [0,2,5]
            if not check_section(hint, 7, sections):
                return False

        if len(hint) == 4: # shape 4 => sections [1, 2, 3, 5]
            if not check_section(hint, 4, sections):
                return False

        if len(hint) == 7: # shape 8 => sections [0, 1, 2, 3, 4, 5, 6]
            if not check_section(hint, 8, sections):
                return False

    return True


def test_permutation(hint_list, sections):
    decoded_value = ''

    for hint in hint_list:
        signals = []

        for c in hint:
            signals.append(get_key(sections, c))

        decoded_value += str(get_key(d_decode, sorted(signals), return_str=True))

    if '.' not in decoded_value and len(decoded_value) == len(hint_list):
        return decoded_value


def part_two():
    final_result = 0

    for line in lines:
        input_chars = line.strip().split('|')[0].split()
        output_chars = line.strip().split('|')[-1].split()

        # brute force method, check all permutations
        perms = [''.join(p) for p in itertools.permutations('abcdefg')]
        for perm in perms:
            sections = {i:perm[i] for i in range(7)}

            # check if the input chars of known length work
            if not check_grid(sections, input_chars):
                continue

            # check that result against all chars
            if not test_permutation(input_chars, sections):
                continue
        
            final_result += int(test_permutation(output_chars, sections))
                    
    return final_result


print(part_one())
print(part_two())