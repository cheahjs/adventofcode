#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict
import numpy as np

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    moves = input[0]
    nodes = {}
    for line in input[2:]:
        src, raw_dst = line.split(' = ')
        nodes[src] = (raw_dst.replace('(', '').replace(')', '').split(', '))
    starting_pos = []
    for node in nodes:
        if node[-1] == 'A':
            starting_pos.append(node)
    loop_lens = []
    print(starting_pos)
    for start in starting_pos:
        count = 0
        cur_node = start
        while cur_node[-1] != 'Z':
            move = moves[count % len(moves)]
            if move == 'L':
                cur_node = nodes[cur_node][0]
            else:
                cur_node = nodes[cur_node][1]
            count += 1
        loop_lens.append(count)
        print(count)
    print(loop_lens)
    print(np.lcm.reduce(loop_lens))

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
