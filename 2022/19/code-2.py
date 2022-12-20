#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import numpy
from collections import defaultdict

A = lambda *a: numpy.array(a)

def gen_heuristic(t, max_t, state):
    ores, robots = state
    geodes = ores[3] + (max_t-t)*robots[3]
    h = geodes*10000 + (robots[2]+ores[2])*100 + (robots[1]+ores[1])*10 + (robots[0]+ores[0])
    return h

def search(blueprint, max_time):
    # ores, robots
    q = [(A(0, 0, 0, 0), A(1, 0, 0, 0))]
    # bfs per time tick
    for t in range(max_time):
        new_q = []
        for ores, robots in q:
            for cost, more_robots in blueprint:
                if all(ores >= cost):
                    new_q.append((ores+robots-cost, robots+more_robots))
        q = sorted(new_q, key=functools.partial(gen_heuristic, t, max_time))[-10000:]
    return max(q, key=lambda x: x[0][3])[0][3]

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    blueprints = []
    for line in inp:
        _, ore, clay, obsa, obsb, geodea, geodeb = map(int, re.findall(r'\d+', line))
        blueprints.append((
            (A(ore, 0, 0, 0), A(1, 0, 0, 0)),
            (A(clay, 0, 0, 0), A(0, 1, 0, 0)),
            (A(obsa, obsb, 0, 0), A(0, 0, 1, 0)),
            (A(geodea, 0, geodeb, 0), A(0, 0, 0, 1)),
            (A(0, 0, 0, 0), A(0, 0, 0, 0))
        ))
    
    puzzle = 1
    for i, bp in enumerate(blueprints):
        if i > 2:
            break
        geodes = search(bp, 32)
        print(i+1, geodes)
        puzzle *= geodes
    print(puzzle)

main()
