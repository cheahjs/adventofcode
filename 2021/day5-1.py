#!/usr/bin/env

import collections

grid = collections.defaultdict(int)

for line in open('day5-1.txt').readlines():
    line = line.strip()
    points = line.split(' -> ')
    start = [int(i) for i in points[0].split(',')]
    end = [int(i) for i in points[1].split(',')]

    if start[0] != end[0] and start[1] != end[1]:
        print(f'Ignoring {start} and {end} due to diagonals')
        continue

    if start[0] == end[0]:
        x = start[0]
        sorted_coords = [start[1], end[1]]
        sorted_coords.sort()
        # print(sorted_coords)
        for y in range(sorted_coords[0], sorted_coords[1]+1):
            grid[(x, y)] += 1
    elif start[1] == end[1]:
        y = start[1]
        sorted_coords = [start[0], end[0]]
        sorted_coords.sort()
        # print(sorted_coords)
        for x in range(sorted_coords[0], sorted_coords[1]+1):
            grid[(x, y)] += 1
    else:
        print(f'Unknown input {line} ({start} -> {end})')

count = 0
for key, value in grid.items():
    if value > 1:
        count += 1

print(count)
