#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def convert(dest_type, src_start, dest_start, count):
    def conversion(x):
        # print(f'testing {x} against {src_start} to {src_start+count} ({dest_start} + {x-src_start})')
        if x >= src_start and x < src_start + count:
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
            seeds = [int(x) for x in line.split(': ')[1].split()]
        elif 'map:' in line:
            src_type = line.split('-to-')[0]
            dest_type = line.split('-to-')[1].split()[0]
        else:
            dest_start, src_start, count = [int(x) for x in line.split()]
            conversions[src_type].append(convert(dest_type, src_start, dest_start, count))
    lowest_location = 1 << 31
    for seed in seeds:
        current_type = 'seed'
        current_value = seed
        while current_type != 'location':
            for conversion in conversions[current_type]:
                result = conversion(current_value)
                if result[1]:
                    # print(f'converted {current_type} ({current_value}) to {result}')
                    current_type, current_value = result
                    break
            else:
                current_type = result[0]
        print(seed, current_value)
        lowest_location = min(lowest_location, current_value)
    print(lowest_location)

main()
