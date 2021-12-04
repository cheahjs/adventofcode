#!/usr/bin/env python3

import collections

input = [l.strip() for l in open('day4-1.txt').readlines()]

draws = [int(i) for i in input[0].split(',')]

bingo_boards = []
# number -> [(i, x, y)]
bingo_numbers = collections.defaultdict(list)


def parse_bingo_board(board_index, lines):
    # row x column
    board = []
    bingo_boards.append(board)
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
    def check_diagonal_top(board):
        for i in range(len(board)):
            if board[i][i][1] == False:
                return False
        return True
    def check_diagonal_bottom(board):
        for i in range(len(board)):
            if board[len(board)-1-i][i][1] == False:
                return False
        return True

    for row in board:
        if check_horizontal(row):
            print('BINGO horizontal row', row)
            return True
    for i in range(len(board)):
        if check_vertical(board, i):
            print('BINGO vertical row', i)
            return True
    # if check_diagonal_top(board):
    #     print('BINGO diagonal top')
    #     return True
    # if check_diagonal_bottom(board):
    #     print('BINGO diagonal bottom')
    #     return True
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
        marked_boards.append(board_index)
        bingo_boards[board_index][x][y][1] = True
    for board_index in marked_boards:
        if not check_bingo(bingo_boards[board_index]):
            continue
        sum = count_bingo(bingo_boards[board_index])
        result = sum * draw
        print('BINGO', draw, sum, result)
        br = True
        break
    if br:
        break