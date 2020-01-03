#!/usr/bin/python3

import io

def iterate(orbits, current_depth, object):
    # print(current_depth, object)
    if object not in orbits:
        return 0
    accumulator = 0
    orbiting_objects = orbits[object]
    for orbiters in orbiting_objects:
        accumulator += current_depth
        accumulator += iterate(orbits, current_depth+1, orbiters)
    return accumulator


def load_input():
    lines = [l.strip() for l in open('day6-input.txt').readlines()]
    orbits = {}
    for line in lines:
        before, after = line.split(')')
        if before not in orbits:
            orbits[before] = [after]
        else:
            orbits[before].append(after)
    # Start from COM, and then do a depth first search
    print(iterate(orbits, 1, "COM"))

if __name__ == "__main__":
    load_input()
    pass
