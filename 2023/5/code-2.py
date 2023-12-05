#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def is_in_range(x, start, count):
    return x >= start and x < start + count

def convert(dest_type, src_start, dest_start, count):
    def conversion(x):
        if is_in_range(x, src_start, count):
            return (dest_type, dest_start + (x-src_start))
        else:
            return (dest_type, None)
    return conversion

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    seeds = []
    conversions = defaultdict(list)
    for line in input:
        if not line:
            continue
        if line.startswith('seeds: '):
            raw_seeds = [int(x) for x in line.split(': ')[1].split()]
            for i in range(len(raw_seeds)//2):
                seeds.append((raw_seeds[i*2], raw_seeds[i*2+1]))
        elif 'map:' in line:
            src_type = line.split('-to-')[0]
            dest_type = line.split('-to-')[1].split()[0]
        else:
            dest_start, src_start, count = [int(x) for x in line.split()]
            conversions[dest_type].append(convert(src_type, dest_start, src_start, count))
    for i in range(10_000_000_000):
        current_type = 'location'
        current_value = i
        while current_type != 'seed':
            for conversion in conversions[current_type]:
                result = conversion(current_value)
                if result[1]:
                    current_type, current_value = result
                    break
            else:
                current_type = result[0]
        for seed in seeds:
            if is_in_range(current_value, seed[0], seed[1]):
                print(f'found seed {seed} at {i}')
                return

main()
