#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

@functools.cache
def possible_ways(record, groups, current_group_count):
    if record == "":
        if len(groups) == 0:
            return 1
        return 0
    # hit a ., so end a group if we have one
    if record[0] == '.':
        # we had a group, so end it
        if current_group_count > 0:
            if len(groups) == 0:
                return 0
            if groups[0] == current_group_count:
                # we ended a valid group, so we can continue
                return possible_ways(record[1:], groups[1:], 0)
            else:
                # we ended an invalid group, so we can't continue
                return 0
        # no group, so we can continue
        return possible_ways(record[1:], groups, current_group_count)
    if record[0] == '#':
        # start or continue a group
        return possible_ways(record[1:], groups, current_group_count + 1)
    if record[0] == '?':
        # we can treat this as either a . or ?
        return possible_ways("." + record[1:], groups, current_group_count) + possible_ways("#" + record[1:], groups, current_group_count)

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    total = 0
    for line in input:
        record, raw_groups = line.split()
        record = '?'.join([record]*5)
        record += '.'
        groups = tuple([int(x) for x in raw_groups.split(',')]*5)
        solve = possible_ways(record, groups, 0)
        # print(solve)
        total += solve
    print(total)


main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
