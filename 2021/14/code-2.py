#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import json
from collections import defaultdict, Counter

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    template = input[0]
    pair_map = {}
    for x in input[2:]:
        parts = x.split(' -> ')
        pair_map[parts[0]] = parts[1]

    pairs = {}
    for pair, ins in pair_map.items():
        pair_1 = pair[0] + ins
        pair_2 = ins + pair[1]
        pairs[pair] = [pair_1, pair_2]

    pair_counts = Counter()
    for i in range(len(template)-1):
        pair_counts[template[i:i+2]] += 1

    # display(pair_counts)

    for step in range(1, 40+1):
        # print('Step', step)
        new_counts = Counter()
        for pair, count in pair_counts.items():
            new_pairs = pairs[pair]
            for new_pair in new_pairs:
                new_counts[new_pair] += count
            pair_counts[pair] -= count
        pair_counts += new_counts

    char_counter = Counter()
    for pair, count in pair_counts.items():
        # first char of each pair overlaps with prev char
        char_counter[pair[1]] += count
    char_counter[template[0]] += 1

    counts = char_counter.most_common()
    mc_c, mc_n = counts[0]
    lc_c, lc_n = counts[-1]
    print(mc_c, mc_n)
    print(lc_c, lc_n)
    print(mc_n - lc_n)


main()
