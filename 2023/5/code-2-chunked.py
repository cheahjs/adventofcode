#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def is_in_range(x, start, count):
    return x >= start and x < start + count

def main():
    input = [x for x in open('test.txt').read().strip().split('\n')]
    seeds = []
    maps = defaultdict(list)
    current_type = 'seed'
    chunks = []
    for line in input:
        if not line:
            continue
        if line.startswith('seeds: '):
            raw_seeds = [int(x) for x in line.split(': ')[1].split()]
            for i in range(len(raw_seeds)//2):
                chunks.append((raw_seeds[i*2], raw_seeds[i*2+1]))
        elif 'map:' in line:
            src_type = line.split('-to-')[0]
            dest_type = line.split('-to-')[1].split()[0]
        else:
            dest_start, src_start, count = [int(x) for x in line.split()]
            maps[src_type] = (src_start, count, dest_start, dest_type)
    for type in maps:
        maps[type].sort(key=lambda x: x[0])
    while current_type != 'location':
        chunks.sort(key=lambda x: x[0])
        current_map = maps[current_type]
        new_chunks = []
        for start, count in chunks:
            end = start+count
            for map_start, map_count, map_dest_start, map_dest_type in current_map:
                map_end = map_start+map_count
                # not in range
                if map_start > end:
                    break
                if map_end < start:
                    break
                # in range, process
                # chunk fully mapped
                if map_start <= start and map_end >= end:
                    new_chunks.append((map_dest_start, count, map_dest_type))
                    break
                # chunk partially mapped
                # map covers start of chunk
                if map_start <= start and map_end > start:
                    new_chunks.append((map_dest_start, map_end-start, map_dest_type))
                    break
                # map covers end of chunk
                if map_start < end and map_end >= end:
                    new_chunks.append((map_dest_start+end-map_start, map_end-end, map_dest_type))
                    break
                # map covers middle of chunk
                if map_start > start and map_end < end:
                    new_chunks.append((map_dest_start+map_start-start, map_count, map_dest_type))
                    break
        chunks = new_chunks
        current_type = current_map[0][3]


main()
