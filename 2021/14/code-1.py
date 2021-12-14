#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict, Counter

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    template = input[0]
    pairs = {}
    for x in input[2:]:
        parts = x.split(' -> ')
        pairs[parts[0]] = parts[1]

    for step in range(1, 10+1):
        new_template = ''
        print('Step', step)
        for i in range(len(template)-1):
            pair = template[i:i+2]
            new_template += pair[0] + pairs[pair]
        new_template += template[-1]
        # print(new_template)
        template = new_template

    counter = Counter(template)
    counts = counter.most_common()
    mc_c, mc_n = counts[0]
    lc_c, lc_n = counts[-1]
    print(mc_c, mc_n)
    print(lc_c, lc_n)
    print(mc_n - lc_n)


main()
