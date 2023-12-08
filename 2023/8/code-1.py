#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    moves = input[0]
    nodes = {}
    for line in input[2:]:
        src, raw_dst = line.split(' = ')
        nodes[src] = (raw_dst.replace('(', '').replace(')', '').split(', '))
    cur_pos = 'AAA'
    count = 0
    while cur_pos != 'ZZZ':
        move = moves[count % len(moves)]
        if move == 'L':
            cur_pos = nodes[cur_pos][0]
        else:
            cur_pos = nodes[cur_pos][1]
        count += 1
    print(count)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
