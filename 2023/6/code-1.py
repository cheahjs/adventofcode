#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import math
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    # time button held down = v = velocity of the boat
    # distance traveled = d = v * t
    # total time = t_total
    # total distance = d = v * (t_total - v)
    # solve for v * (t_total - v) > d
    # v*t_total - v^2 > d
    # v^2 - t*v + d < 0
    # v = (t +- sqrt(t^t - 4*d))/2
    # (t - sqrt(t^t - 4*d))/2 < v < (t + sqrt(t^t - 4*d))/2
    times = [int(x) for x in input[0].split()[1:]]
    distances = [int(x) for x in input[1].split()[1:]]
    ways = []
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        lower = (time - (time**2 - 4*distance)**0.5)/2
        upper = (time + (time**2 - 4*distance)**0.5)/2
        print(f'{lower} < v < {upper} for time {time} and distance {distance}')
        if lower < math.ceil(lower):
            lower = math.ceil(lower)
        elif lower == int(lower):
            lower = int(lower)+1
        if upper > math.floor(upper):
            upper = math.floor(upper)
        elif upper == int(upper):
            upper = int(upper)-1
        ways.append(upper-lower+1)
        print(lower, upper)
    print(ways)
    print(functools.reduce(lambda x, y: x*y, ways))

main()
