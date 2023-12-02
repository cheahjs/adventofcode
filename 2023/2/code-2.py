#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    sum = 0
    for line in input:
        game_id_raw, rounds_raw = line.split(': ')
        game_id = int(game_id_raw.split(' ')[1])
        rounds = rounds_raw.split('; ')
        min_red, min_blue, min_green = 0, 0, 0
        for round in rounds:
            colors = round.split(', ')
            for color in colors:
                color_count, color_name = color.split(' ')
                color_count = int(color_count)
                if color_name == 'red':
                    min_red = max(min_red, color_count)
                elif color_name == 'green':
                    min_green = max(min_green, color_count)
                elif color_name == 'blue':
                    min_blue = max(min_blue, color_count)
        power = min_red*min_blue*min_green
        print(f'{game_id}: red {min_red}, green {min_green}, blue {min_blue}: {power}')
        sum += power
    print(sum)

main()
