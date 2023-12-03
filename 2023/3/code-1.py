#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

adj_tests = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],  [0, 1],  [0, 1],
    [1, -1],  [1, 0],  [1, 1]
]

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    sum = 0
    board = []
    for line in input:
        row = []
        for char in line:
            row.append(char)
        board.append(row)
    current_digit = 0
    is_adjacent = False
    # Visit every cell
    for y in range(len(board)):
        for x in range(len(board[y])):
            current_char = board[y][x]
            # If char is a digit, add to current_digit
            if current_char.isdigit():
                current_digit = current_digit*10 + int(current_char)
                # check adjacent cells for symbols
                for test in adj_tests:  
                    y_test = y + test[0]
                    x_test = x + test[1]
                    if x_test < 0 or x_test >= len(board[y]):
                        continue
                    if y_test < 0 or y_test >= len(board):
                        continue
                    test_char = board[y_test][x_test]
                    if not test_char.isdigit() and test_char != '.':
                        is_adjacent = True
                        break
            # We've hit the end of a digit
            else:
                if current_digit != 0 and is_adjacent:
                    print(current_digit)
                    sum += current_digit
                current_digit = 0
                is_adjacent = False
        # Duplicate logic for end of line
        if current_digit != 0 and is_adjacent:
            print(current_digit)
            sum += current_digit
        current_digit = 0
        is_adjacent = False
    print(sum)

main()
