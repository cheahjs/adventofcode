#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

X = 0
Y = 1

FACES = [
    [0, 1],  # right +y
    [1, 0],  # down +x
    [0, -1],  # left -y
    [-1, 0],  # up -x
]


def main():
    f = open('input.txt').read()
    raw_map, raw_directions = f.split('\n\n')
    mapp = {}
    cur = None
    face = 0
    max_x = 0
    max_y = 0
    for x, row in enumerate(raw_map.split('\n')):
        max_x = x
        for y, val in enumerate(row.strip('\n')):
            max_y = max(max_y, y)
            if val == ' ':
                continue
            if x == 0 and cur is None:
                cur = (x, y)
            mapp[(x, y)] = val

    @functools.cache
    def get_start_y(x):
        for y in range(max_y+1):
            if (x, y) in mapp:
                return y

    @functools.cache
    def get_end_y(x):
        end = None
        for y in range(max_y+1):
            if (x, y) in mapp:
                end = y
        return end

    @functools.cache
    def get_start_x(y):
        for x in range(max_x+1):
            if (x, y) in mapp:
                return x

    @functools.cache
    def get_end_x(y):
        end = None
        for x in range(max_x+1):
            if (x, y) in mapp:
                end = x
        return end

    steps = map(int, re.findall(r'\d+', raw_directions))
    rotates = re.findall(r'[LR]', raw_directions)
    for i, count in enumerate(steps):
        # move
        dir = FACES[face]
        print(f'moving {count} steps in {dir} from {cur}')
        for j in range(count):
            new = [cur[X]+dir[X], cur[Y]+dir[Y]]
            # print(f'attempting to move to {new}')
            # check surface bounds
            if tuple(new) not in mapp:
                # we need to wrap
                match face:
                    case 0:
                        # wrap to left
                        new[Y] = get_start_y(new[X])
                    case 1:
                        # wrap to top
                        new[X] = get_start_x(new[Y])
                    case 2:
                        # wrap to right
                        new[Y] = get_end_y(new[X])
                    case 3:
                        # wrap to bottom
                        new[X] = get_end_x(new[Y])
                print(f'wrapped to: {new}')
            # wall check
            if mapp[tuple(new)] == '#':
                print(f'hit wall at {new}')
                break
            # move
            cur = tuple(new)

        # rotate
        if i < len(rotates):
            rotate = rotates[i]
            face += 1 if rotate == 'R' else -1
            face = face % len(FACES)

    print(cur)
    print((cur[X]+1)*1000 + 4*(cur[Y]+1) + face)

main()
