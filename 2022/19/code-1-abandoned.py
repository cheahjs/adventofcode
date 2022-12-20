#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
import sys
sys.setrecursionlimit(5000)

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    ore_cost = []
    clay_cost = []
    obsidian_cost = []
    geode_cost = []
    t_best = defaultdict(int)
    for line in inp:
        matches = re.match(
            r'.+ore robot costs (\d+) ore.+clay robot costs (\d+) ore.+obsidian robot costs (\d+) ore and (\d+) clay.+costs (\d+) ore and (\d+) obsidian.+', line)
        ore_cost.append(int(matches[1]))
        clay_cost.append(int(matches[2]))
        obsidian_cost.append((int(matches[3]), int(matches[4])))
        geode_cost.append((int(matches[5]), int(matches[6])))
    @functools.cache
    def search(idx, t, ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot):
        # if geode_robot > 0:
            # print(f't={t}, ore={ore} ({ore_robot}), clay={clay} ({clay_robot}), obs={obsidian} ({obsidian_robot}), geode={geode} ({geode_robot})')
        # collection phase
        new_ore = ore_robot
        new_clay = clay_robot
        new_obsidian = obsidian_robot
        new_geode = geode_robot
        # build phase
        build_options = [(0, 0, 0, 0, 0, 0, 0)]
        if ore >= geode_cost[idx][0] and obsidian >= geode_cost[idx][1]:
            build_options.append((geode_cost[idx][0], 0, geode_cost[idx][1], 0, 0, 0, 1))
        if ore >= obsidian_cost[idx][0] and clay >= obsidian_cost[idx][1]:
            build_options.append((obsidian_cost[idx][0], obsidian_cost[idx][1], 0, 0, 0, 1, 0))
        if ore >= clay_cost[idx]:
            build_options.append((clay_cost[idx], 0, 0, 0, 1, 0, 0))
        if ore >= ore_cost[idx]:
            build_options.append((ore_cost[idx], 0, 0, 1, 0, 0, 0))
            
        # post-collection
        ore += new_ore
        clay += new_clay
        obsidian += new_obsidian
        geode += new_geode
        if t == 23:
            return geode
        if t_best[t] > geode:
            return 0
        t_best[t] = geode
        return max([search(idx, t+1, ore-o[0], clay-o[1], obsidian-o[2], geode, ore_robot+o[3], clay_robot+o[4], obsidian_robot+o[5], geode_robot+o[6]) for o in build_options])

    puzzle = 0
    for i in range(len(ore_cost)):
        geode = search(i, 0, 0, 0, 0, 0, 1, 0, 0, 0)
        print(i+1, geode, (i+1)*geode)
        puzzle += (i+1)*geode
    print(puzzle)

main()
