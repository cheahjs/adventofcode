#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from PIL import Image, ImageDraw

def main():
    marked = {}
    folds = []
    for x in open('input.txt').read().strip().split('\n'):
        if 'fold along' in x:
            clean = x.replace('fold along ', '')
            split = clean.split('=')
            folds.append([split[0], int(split[1])])
        elif x.isspace() or x == '':
            continue
        else:
            split = x.split(',')
            marked[(int(split[0]), int(split[1]))] = True

    print('Dots visible', len(marked))
    for dir, pos in folds:
        print(f'Folding along {dir}={pos}')
        for x, y in list(marked.keys()):
            if dir == 'x':
                # fold left
                # marked left (x < pos), no change
                # marked right (x > pos), move from x to
                # x = pos + d
                # new_x = pos - d
                #       = (x-d) - d
                #       = x - 2(x-pos)
                if x < pos:
                    continue
                new_x = x - 2*(x-pos)
                # print(f'Moving {x},{y} to {new_x},{y}')
                del marked[(x, y)]
                marked[(new_x, y)] = True
            else:
                # fold up
                # marked above (y < pos), no change
                # marked below (y > pos), move from y to
                # y = pos + d
                # new_y = pos - d
                #       = (y-d) - d
                #       = y - 2(y-pos)
                if y < pos:
                    continue
                new_y = y - 2*(y-pos)
                # print(f'Moving {x},{y} to {x},{new_y}')
                del marked[(x, y)]
                marked[(x, new_y)] = True
        print('Dots visible', len(marked))

    grid = [[' ']*100 for x in range(100)]
    for x, y in marked:
        grid[y][x] = '█'
    for row in grid:
        print(''.join(row))
    # img = Image.new('RGB', (60, 10), color='white')
    # for x, y in marked:
    #     img.putpixel((x, y), (0,0,0))
    # display(img.resize((600, 100), Image.NEAREST))

main()
