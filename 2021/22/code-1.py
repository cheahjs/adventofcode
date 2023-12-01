#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from __future__ import annotations


class Cube:
    def __init__(self, state, x_l, x_h, y_l, y_h, z_l, z_h) -> None:
        self.state = state
        self.x_l = x_l
        self.x_h = x_h
        self.y_l = y_l
        self.y_h = y_h
        self.z_l = z_l
        self.z_h = z_h

    def volume(self) -> int:
        return (abs(self.x_h - self.x_l) + 1) * (abs(self.y_h - self.y_l) + 1) * (abs(self.y_h - self.y_l) + 1)

    def intersect(self, cube: Cube) -> bool:
        if cube.x_l < self.x_h:
            return True
        if self.x_h < cube.x_l:
            return True
        if cube.y_l < self.y_h:
            return True
        if self.y_h < cube.y_l:
            return True
        if cube.z_l < self.z_h:
            return True
        if self.z_h < cube.z_l:
            return True
        return False

    def overlap(self, cube: Cube) -> list[Cube]:
        return [self]

def main():
    input = []
    for l in open('test-2.txt').read().strip().split('\n'):
        state, raw_bounds = l.split(' ')
        x, y, z = [j.split('=')[1] for j in raw_bounds.split(',')]
        xl, xh = [int(j) for j in x.split('..')]
        yl, yh = [int(j) for j in y.split('..')]
        zl, zh = [int(j) for j in z.split('..')]
        input.append(Cube(state, xl, xh, yl, yh, zl, zh))

    cubes = set()
    for command, (x_b, y_b, z_b) in input:


    print(len(space))


main()
