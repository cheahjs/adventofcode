#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

SIDES = [
    # x-axis
    [1, 0, 0], [-1, 0, 0],
    # y-axis
    [0, 1, 0], [0, -1, 0],
    # z-axis
    [0, 0, 1], [0, 0, -1],
]

def main():
    cubes = set([tuple([int(a) for a in x.split(',')]) for x in open('input.txt').read().strip().split('\n')])

    # find bounding box
    min_x = min([x[0] for x in cubes])-1
    max_x = max([x[0] for x in cubes])+1
    min_y = min([x[1] for x in cubes])-1
    max_y = max([x[1] for x in cubes])+1
    min_z = min([x[2] for x in cubes])-1
    max_z = max([x[2] for x in cubes])+1

    # flood fill with BFS
    reachable = set()
    q = [(min_x,min_y,min_z)]
    while len(q) > 0:
        test = q.pop()
        reachable.add(test)
        for (dx,dy,dz) in SIDES:
            pocket = (test[0]+dx, test[1]+dy, test[2]+dz)
            # check if in bounding box
            if not (min_x <= pocket[0] <= max_x):
                # print(f'{pocket} outside x')
                continue
            if not (min_y <= pocket[1] <= max_y):
                # print(f'{pocket} outside y')
                continue
            if not (min_z <= pocket[2] <= max_z):
                # print(f'{pocket} outside z')
                continue
            # check for lava
            if pocket in cubes:
                # print(f'{pocket} is lava')
                continue
            # check if already visited
            if pocket in reachable:
                # print(f'{pocket} already visited')
                continue
            # reachable air pocket
            q.append(pocket)

    # print(reachable)

    area = 0
    for (x,y,z) in cubes:
        # check all sides for another cube
        for (dx, dy, dz) in SIDES:
            pocket = (x+dx, y+dy, z+dz)
            if pocket not in cubes and pocket in reachable:
                area += 1
    print(area)

main()
