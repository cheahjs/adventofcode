#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
import heapq

def print_debug(grid):
    print('\n'.join([''.join([str(i) for i in x]) for x in grid]))


def main():
    grid = [[int(i) for i in x]
             for x in open('input.txt').read().strip().split('\n')]
    
    # print_debug(grid)

    rows = len(grid)
    cols = len(grid[0])

    # distance = risk level
    distance = {(x,y): 2**31 for y in range(cols) for x in range(rows)}
    distance[(0,0)] = 0

    target = (rows-1, cols-1)

    visited = []
    pq = []
    heapq.heappush(pq, (0, (0, 0)))

    while len(pq) > 0:
        dist, cur_node = heapq.heappop(pq)
        visited.append(cur_node)
        # print('Visiting', cur_node, 'current cost:', dist)

        for adj in [(1, 0), (0, 1)]:
            new_node = (cur_node[0] + adj[0], cur_node[1] + adj[1])
            # print('Checking', new_node, 'from', cur_node)
            if not (new_node[0] < rows and new_node[1] < cols):
                # print('Ignoring', new_node)
                continue
            cost = grid[new_node[0]][new_node[1]]
            if new_node in visited:
                # print('Already visited', new_node)
                continue
            old_cost = distance[new_node]
            new_cost = distance[cur_node] + cost
            # print(cur_node, 'to', new_node, 'prev cost:', old_cost, 'new_cost:', new_cost)
            if new_cost < old_cost:
                heapq.heappush(pq, (new_cost, new_node))
                distance[new_node] = new_cost

    # display(distance)
    print(distance[target])


main()
