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
        for chunk_start, count in chunks:
            chunk_end = chunk_start+count
            for map_start, map_count, map_dest_start, map_dest_type in current_map:
                map_end = map_start+map_count
                # start falls somewhere in the map range
                if is_in_range(chunk_start, map_start, map_count):
                    # end also falls in the map range, chunk is fully mapped
                    if is_in_range(chunk_end, map_start, map_count):
                        # add [map(start), map(end)] to new_chunks
                        # [dest_start + (chunk-map start), count)
                        new_chunks.append((map_dest_start + chunk_start - map_start, count))
                    # end falls outside the map range, chunk is partially mapped
                    else:
                        # add [map(start), map(map_end)) to new_chunks
                        # [dest_start + (chunk-map start), map_end - chunk_start]
                        new_chunks.append((map_dest_start + chunk_start - map_start, map_end - chunk_start))
                        # add [map_end, end) to chunks
                        # this might be a new chunk, or it might overlap with the next map
                        # new_chunks.append((map_dest_start, end - map_end))
                # start falls outside the map range, but end falls inside the map range
                elif is_in_range(chunk_end, map_start, map_count):
                    # add [map_start, chunk_end) to new_chunks
                    # [dest_start, chunk_end - map_start)]
                    new_chunks.append((map_dest_start, map_end - chunk_start))
                else:
                    new_chunks.append((chunk_start, count))
        chunks = new_chunks
        current_type = current_map[0][3]


main()
