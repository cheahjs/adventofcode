#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import numpy
from collections import defaultdict

A = lambda *a: numpy.array(a)

def search(costs, robots, max_time):
    # store (time, robots, ores)
    s = set()
    q = [(0, robots, (0,0,0,0))]
    max_geodes = 0
    max_geodes_time = defaultdict(int)
    while q:
        t, r, o = q.pop(0)
        # print(t,r,o)
        
        if (t,r,o) in s:
            continue
        s.add((t,r,o))

        if (max_time-t)*r[3] < max_geodes:
            continue
        if max_geodes_time[t] > r[3]:
            continue
        max_geodes_time[t] = r[3]

        if t == max_time:
            max_geodes = max(max_geodes, o[3])
        
        # mining phase
        new_ores = tuple([o[i] + r[i] for i in range(len(o))])

        # build phase
        # greed for geode
        if all([o[j] >= costs[3][j] for j in range(4)]):
            new_robots = list(r)
            new_robots[3] += 1
            new_new_ores = tuple([new_ores[j] - costs[3][j] for j in range(4)])
            q.append((t+1, tuple(new_robots), new_new_ores))
        else:
            for i in range(3):
                cost = costs[i]

                # check if we have too many already
                if sum([x[i] for x in costs]) < robots[i]:
                    continue

                # check for mats
                if all([o[j] >= cost[j] for j in range(len(cost))]):
                    new_robots = list(r)
                    new_robots[i] += 1
                    new_new_ores = tuple([new_ores[j] - cost[j] for j in range(len(cost))])
                    q.append((t+1, tuple(new_robots), new_new_ores))
            # no build
            q.append((t+1, robots, new_ores))

    return max_geodes

def main():
    inp = [x for x in open('test.txt').read().strip().split('\n')]
    ore_cost = []
    clay_cost = []
    obsidian_cost = []
    geode_cost = []
    for line in inp:
        matches = re.match(
            r'.+ore robot costs (\d+) ore.+clay robot costs (\d+) ore.+obsidian robot costs (\d+) ore and (\d+) clay.+costs (\d+) ore and (\d+) obsidian.+', line)
        ore_cost.append(int(matches[1]))
        clay_cost.append(int(matches[2]))
        obsidian_cost.append((int(matches[3]), int(matches[4])))
        geode_cost.append((int(matches[5]), int(matches[6])))
    
    puzzle = 0
    for i in range(len(ore_cost)):
        costs = [
            (ore_cost[i], 0, 0, 0),
            (clay_cost[i], 0, 0, 0),
            (obsidian_cost[i][0], obsidian_cost[i][1], 0, 0),
            (geode_cost[i][0], 0, geode_cost[i][1], 0)
        ]
        geodes = search(costs, (1, 0, 0, 0), 24)
        print(i+1, geodes, (i+1)*geodes)
        puzzle += (i+1)*geodes
    print(geodes)

main()
