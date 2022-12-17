#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from tqdm import tqdm

PIECES = [
    [
        [0, 0], [1, 0], [2, 0], [3, 0]
    ],
    [
                [1, 2],
        [0, 1], [1, 1], [2, 1],
                [1, 0]
    ],
    [
                        [2, 2],
                        [2, 1],
        [0, 0], [1, 0], [2, 0]
    ],
    [
        [0, 3],
        [0, 2],
        [0, 1],
        [0, 0]
    ],
    [
        [0, 1], [1, 1],
        [0, 0], [1, 0]
    ]
]

def print_grid(grid, opt_piece=set()):
    highest_y = max([y for x, y in grid] + [y for x, y in opt_piece])
    for y in range(0, highest_y+1):
        print('|', end='')
        for x in range(0, 7):
            t = (x, highest_y-y)
            if t in grid:
                print('#', end='')
            elif t in opt_piece:
                print('@', end='')
            else:
                print('.', end='')
        print('|')
    print('+-------+')

def piece_to_set(x, y, piece):
    s = set()
    for p in piece:
        s.add((x+p[0], y+p[1]))
    return s

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    jet = inp[0]
    grid = set()
    cur_jet = 0
    cur_height = 0
    for cur_piece in tqdm(range(0, 1000000000000)):
        piece = PIECES[cur_piece % len(PIECES)]

        def is_colliding(x2, y2) -> bool:
            for p in piece:
                xt, yt = x2+p[0], y2+p[1]
                if xt < 0 or xt > 6:
                    # print('collided with wall')
                    return True
                if yt < 0:
                    # print('collided with floor')
                    return True
                if (xt, yt) in grid:
                    # print('collided with piece')
                    return True
            return False

        x, y = 2, cur_height + 3
        while True:
            # blow
            xb = 1 if jet[cur_jet % len(jet)] == '>' else -1
            if not is_colliding(x+xb, y):
                # we've been blown
                x += xb
            # print(f'{cur_piece}: post-blow ({jet[cur_jet % len(jet)]}: {xb})')
            # print_grid(grid, piece_to_set(x, y, piece))
            cur_jet += 1
            # down
            if is_colliding(x, y-1):
                for p in piece:
                    xt, yt = x+p[0], y+p[1]
                    grid.add((xt, yt))
                    cur_height = max(cur_height, yt+1)
                break
            else:
                y -= 1
        #     print(f'{cur_piece}: post-drop')
        #     print_grid(grid, piece_to_set(x, y, piece))
        # print(f'{cur_piece}: post-harden')
        # print_grid(grid)
    print(cur_height)


main()
