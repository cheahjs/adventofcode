#!/usr/bin/env python3

import collections

input = [l.strip() for l in open('day4-1.txt').readlines()]

draws = [int(i) for i in input[0].split(',')]

bingo_boards = {}
# number -> [(i, x, y)]
bingo_numbers = collections.defaultdict(list)


def parse_bingo_board(board_index, lines):
    # row x column
    board = []
    bingo_boards[board_index] = board
    for x, row in enumerate(lines):
        board.append([])
        for y, col in enumerate(row.split()):
            num = int(col)
            bingo_numbers[num].append((board_index, x, y))
            board[x].append([num, False])

def check_bingo(board):
    def check_horizontal(row):
        for col in row:
            if col[1] == False:
                return False
        return True
    def check_vertical(board, col):
        for row in board:
            if row[col][1] == False:
                return False
        return True

    for row in board:
        if check_horizontal(row):
            return True
    for i in range(len(board)):
        if check_vertical(board, i):
            return True
    return False

def count_bingo(board):
    sum = 0
    for row in board:
        for col, marked in row:
            if not marked:
                sum += col
    return sum

i = 2
b = 0
while i < len(input):
    parse_bingo_board(b, input[i:i+5])
    i += 6
    b += 1

br = False
for draw in draws:
    # only check boards that have been touched
    marked_boards = []
    for (board_index, x, y) in bingo_numbers[draw]:
        if board_index not in bingo_boards:
            continue
        marked_boards.append(board_index)
        bingo_boards[board_index][x][y][1] = True
    for board_index in marked_boards:
        if check_bingo(bingo_boards[board_index]):
            board = bingo_boards.pop(board_index)
            if len(bingo_boards) == 0:
                sum = count_bingo(board)
                flag = sum * draw
                print('Bingo', draw, 'Sum', sum, 'Flag', flag)