#!/usr/bin/env

import collections

grid = collections.defaultdict(int)

for line in open('day5-1.txt').readlines():
    line = line.strip()
    points = line.split(' -> ')
    start = [int(i) for i in points[0].split(',')]
    end = [int(i) for i in points[1].split(',')]

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
        # diagonal, exactly 45 degrees
        steps = abs(start[0] - end[0]) + 1
        initial_x, initial_y = start[0],  start[1]
        x_step = -1 if start[0] > end[0] else 1
        y_step = -1 if start[1] > end[1] else 1
        for i in range(steps):
            grid[(initial_x+(i*x_step), initial_y+(i*y_step))] += 1

count = 0
for key, value in grid.items():
    if value > 1:
        count += 1

print(count)
