#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from tqdm import tqdm

MAX_PIECES = 1_000_000_000_000

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
    # store (piece, jet) -> (piece index, height when added, seen)
    # if (piece, jet) is seen again, then we may be at the start of a cycle
    # it may not be a cycle if the "floor" doesn't match up, so store how many times a specific cycle has been seen
    state = {}
    i_j = 0
    cur_height = 0
    cycle_count, cycle_height = None, None
    for cur_piece in range(MAX_PIECES):
        i_p = cur_piece % len(PIECES)
        piece = PIECES[i_p]
        if (i_p, i_j) in state:
            cycle_count = cur_piece-state[(i_p, i_j)][0]
            cycle_height = cur_height - state[(i_p, i_j)][1]
            seen = state[(i_p, i_j)][2]
            print(
                f'Seen a repeat of i_p:{i_p}, i_j:{i_j} at piece:{cur_piece}, cycle_count={cycle_count}, cycle_height={cycle_height}, seen={state[(i_p, i_j)][2]}')
            if seen < 3:
                cycle_count, cycle_height = None, None
        state[(i_p, i_j)] = [cur_piece, cur_height, state[(i_p, i_j)][2] + 1 if (i_p, i_j) in state else 1]

        # we're currently at the start of a cycle
        if cycle_height and cycle_count:
            # we're currently at the start of cycle that will end at the top of the tower
            if (MAX_PIECES - cur_piece) % cycle_count == 0:
                cur_height += ((MAX_PIECES - cur_piece) // cycle_count) * cycle_height
                break

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
            xb = 1 if jet[i_j] == '>' else -1
            if not is_colliding(x+xb, y):
                # we've been blown
                x += xb
            # print(f'{cur_piece}: post-blow ({jet[cur_jet % len(jet)]}: {xb})')
            # print_grid(grid, piece_to_set(x, y, piece))
            i_j = (i_j+1) % len(jet)

            # down
            if is_colliding(x, y-1):
                old_height = cur_height
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
