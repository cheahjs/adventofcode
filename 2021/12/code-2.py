#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import json
import copy
from collections import defaultdict


class Chain():
    def __init__(self) -> None:
        self.path = []
        self.visited = {}
        self.two_small = None

    def has_visited(self, point):
        return point in self.visited

    def visit(self, point):
        if point not in ['start', 'end'] and is_small(point) and self.has_visited(point):
            if self.two_small != None:
                return False
            self.two_small = point
            # make two decisions:
            # 1. visit again and mark two_small -> visit
            # 2. don't visit again -> return False
        if point == 'start' and len(self.path) > 0:
            return False
        self.path.append(point)
        self.visited[point] = True
        return True


def is_small(point: str):
    return point.lower() == point


def visit(graph, start, prev_chain: Chain):
    # print('Visiting', start, 'with path', prev_chain.path)

    new_chain = copy.deepcopy(prev_chain)
    if not new_chain.visit(start):
        return [None]
    if start == 'end':
        return [new_chain]

    chains = []
    next_points = graph[start]
    for point in next_points:
        chains.extend(visit(graph, point, new_chain))

    return [x for x in chains if x != None]


def main():
    # map of point -> connected points
    graph = defaultdict(list)

    for line in open('input.txt').read().strip().split('\n'):
        parts = line.split('-')
        graph[parts[0]].append(parts[1])
        graph[parts[1]].append(parts[0])

    paths = visit(graph, 'start', Chain())
    # print('\n'.join(sorted([','.join(path.path) for path in paths])))
    print(len(paths))


main()
