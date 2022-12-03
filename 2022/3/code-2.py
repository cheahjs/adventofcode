#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def char_to_priority(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-64+26

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    priority_sum = 0
    sets = [{c for c in line} for line in input]
    for i in range(len(sets)//3):
        collision = sets[i*3] & sets[i*3+1] & sets[i*3+2]
        assert(len(collision) == 1)
        priority_sum += sum([char_to_priority(x) for x in collision])
    print(priority_sum)

main()
