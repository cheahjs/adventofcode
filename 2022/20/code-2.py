#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    inp = [(i, int(x)*811589153) for i, x in enumerate(open('input.txt').read().strip().split('\n'))]
    c = collections.deque(inp)
    for _ in range(10):
        for i, x in inp:
            # move x to the front of the list by rotating left
            c.rotate(-c.index((i, x)))
            # remove the element
            c.popleft()
            # rotate left by the number of times the value says we rotate
            c.rotate(-x % len(c))
            # reinsert the popped element
            c.appendleft((i, x))
    # the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value 0
    # removing indices, and rotate zero to the head
    c = collections.deque([v for k, v in c])
    c.rotate(-c.index(0))
    print(c[1000%len(c)] + c[2000%len(c)] + c[3000%len(c)])

main()
