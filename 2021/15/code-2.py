#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
import heapq

def print_debug(grid):
    print('\n'.join([''.join([str(i) for i in x]) for x in grid]))

def inc(val, amount):
    new_val = val + amount
    new_val = (new_val % 10) + (new_val // 10)
    return new_val

def main():
    grid = [[int(i) for i in x]
             for x in open('input.txt').read().strip().split('\n')]

    rows = len(grid)
    cols = len(grid[0])

    new_grid = [[0 for y in range(cols*5)] for x in range(rows*5)]

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            new_grid[x][y] = val
            for i in range(1, 5):
                new_x = x + i*rows
                new_grid[new_x][y] = inc(val, i)

    for x, row in enumerate(new_grid):
        for i in range(1, 5):
            for y in range(cols):
                new_grid[x][y+i*cols] = inc(row[y], i)
    
    print_debug(new_grid)

    grid = new_grid
    rows *= 5
    cols *= 5

    # distance = risk level
    distance = {(x,y): 2**31 for y in range(cols) for x in range(rows)}
    distance[(0,0)] = 0

    target = (rows-1, cols-1)

    visited = {}
    pq = []
    heapq.heappush(pq, (0, (0, 0)))

    while len(pq) > 0:
        dist, cur_node = heapq.heappop(pq)
        visited[cur_node] = True

        for adj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_node = (cur_node[0] + adj[0], cur_node[1] + adj[1])
            if not (0 <= new_node[0] < rows and 0 <= new_node[1] < cols):
                continue
            cost = grid[new_node[0]][new_node[1]]
            if new_node in visited:
                continue
            old_cost = distance[new_node]
            new_cost = distance[cur_node] + cost
            if new_cost < old_cost:
                heapq.heappush(pq, (new_cost, new_node))
                distance[new_node] = new_cost

    print(target, distance[target])


main()
