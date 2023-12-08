#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def end_condition(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True

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
    count = 0
    print(starting_pos)
    while not end_condition(starting_pos):
        move = moves[count % len(moves)]
        new_starting_pos = []
        for pos in starting_pos:
            if move == 'L':
                new_starting_pos.append(nodes[pos][0])
            else:
                new_starting_pos.append(nodes[pos][1])
        starting_pos = new_starting_pos
        count += 1
    print(count)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
