#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import json
import copy
from collections import defaultdict
import cProfile

class Chain():
    def __init__(self, prev_chain: Chain = None):
        if prev_chain == None:
            self.visited = []
            self.two_small = None
        else:
            self.visited = prev_chain.visited[:]
            self.two_small = prev_chain.two_small

    def has_visited(self, point):
        return point in self.visited

    def visit(self, point):
        if point not in ['start', 'end'] and is_small(point) and self.has_visited(point):
            if self.two_small != None:
                return False
            self.two_small = point
        if point == 'start' and len(self.visited) > 0:
            return False
        self.visited.append(point)
        return True


def is_small(point: str):
    return point.islower()

def visit(graph, start, prev_chain: Chain):
    new_chain = Chain(prev_chain)
    if not new_chain.visit(start):
        return [None]
    if start == 'end':
        return [new_chain]

    chains = []
    next_points = graph[start]
    for point in next_points:
        chains.extend(visit(graph, point, new_chain))

    return chains


def main():
    # map of point -> connected points
    graph = defaultdict(list)

    for line in open('input.txt').read().strip().split('\n'):
        parts = line.split('-')
        graph[parts[0]].append(parts[1])
        graph[parts[1]].append(parts[0])

    paths = visit(graph, 'start', Chain())
    print(len([x for x in paths if x != None]))


# cProfile.run('main()')
main()
