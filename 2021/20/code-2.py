#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def print_grid(grid):
    lowest_x = min([x for x, y in grid])
    highest_x = max([x for x, y in grid])
    lowest_y = min([y for x, y in grid])
    highest_y = max([y for x, y in grid])
    for x in range(lowest_x-5, highest_x+5):
        for y in range(lowest_y-5, highest_y+5):
            print('#' if (x, y) in grid else ' ', end='')
        print()


def count_lit(grid):
    count = 0
    for pos in grid:
        count += 1
    return count

def main():
    input = [x for x in open('test.txt').read().strip().split('\n')]

    grid = set()
    enhance = input[0]

    for x, x_val in enumerate(input[2:]):
        for y, y_val in enumerate(x_val):
            if y_val == '#':
                grid.add((x, y))

    print('Initially lit:', count_lit(grid))

    background_lit = False
    for step in range(0, 50):
        new_grid = set()

        x_min =  min([x for x,y in grid])
        x_max = max([x for x,y in grid])
        y_min =  min([y for x,y in grid])
        y_max = max([y for x,y in grid])
        print(x_min, x_max, y_min, y_max)

        for x in range(x_min-2, x_max+3):
            for y in range(y_min-2, y_max+3):
                index = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        oob = not (
                            x_min < x + dx < x_max) or not (
                                y_min < y + dy < y_max)
                        index <<= 1
                        index |= (x + dx, y + dy) in grid or (oob and background_lit)
                if enhance[index] == '#':
                    new_grid.add((x, y))

        grid = new_grid
        background_lit = enhance[-1 if background_lit else 0] == '#'
        print(f'After step {step+1}, we have {count_lit(grid)} lit (new background: {background_lit})')

main()
