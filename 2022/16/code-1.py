#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

MAX_STEPS = 30


def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]
    V, F, D = set(), dict(), defaultdict(lambda: 1_000_000)
    for line in inp:
        matches = re.match(
            r'Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
        valve, flow_rate, tunnels = matches[1], int(
            matches[2]), matches[3].split(', ')
        V.add(valve)
        if flow_rate > 0:
            F[valve] = flow_rate
        for u in tunnels:
            D[valve, u] = 1

    # floyd-warshall to get min cost of each pairwise node
    for k, i, j in itertools.product(V, V, V):
        if D[i, j] > D[i, k] + D[k, j]:
            D[i, j] = D[i, k] + D[k, j]

    # memoized DFS
    @functools.cache
    def search(u, remaining_time, unopened_valves):
        return max(
            [
                # take D[u,v] time to visit v, open valve v, take one minute to start release, and continue releasing
                F[v] * (remaining_time-D[u, v]-1) + search(v, remaining_time-D[u, v]-1, unopened_valves-{v})
                for v in unopened_valves if D[u, v] < remaining_time
            ] + [0]
        )

    print(search('AA', 30, frozenset(F)))


main()
