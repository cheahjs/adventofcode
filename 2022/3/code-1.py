#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    priority_sum = 0
    for line in input:
        half_a, half_b = line[:len(line)//2], line[len(line)//2:]
        map_a = {c for c in half_a}
        map_b = {c for c in half_b}
        collision = map_a & map_b
        priority_sum += sum([ord(x)-96 if x.islower() else ord(x)-(64-26) for x in collision])
    print(priority_sum)

main()
