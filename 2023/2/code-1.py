#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    RED_MAX = 12
    GREEN_MAX = 13
    BLUE_MAX = 14
    sum = 0
    for line in input:
        game_id_raw, rounds_raw = line.split(': ')
        game_id = int(game_id_raw.split(' ')[1])
        rounds = rounds_raw.split('; ')
        impossible = False
        for round in rounds:
            if impossible:
                break
            colors = round.split(', ')
            for color in colors:
                color_count, color_name = color.split(' ')
                color_count = int(color_count)
                if color_name == 'red' and color_count > RED_MAX:
                    impossible = True
                    print(f'Game {game_id} impossible: red {color_count} > {RED_MAX}')
                    break
                elif color_name == 'green' and color_count > GREEN_MAX:
                    impossible = True
                    print(f'Game {game_id} impossible: green {color_count} > {GREEN_MAX}')
                    break
                elif color_name == 'blue' and color_count > BLUE_MAX:
                    impossible = True
                    print(f'Game {game_id} impossible: blue {color_count} > {BLUE_MAX}')
                    break
        if not impossible:
            print(f'Game {game_id} possible')
            sum += game_id
    print(sum)

main()
