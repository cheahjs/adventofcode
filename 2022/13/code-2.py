#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from functools import cmp_to_key

RIGHT = 'right'
OUT = 'out'
CONTINUE = 'continue'

def compare(a, b):
    # print('comparing', a, b)
    # both ints
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return RIGHT
        elif a > b:
            return OUT
        elif a == b:
            return CONTINUE
    # one int
    if isinstance(a, int):
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])
    # both lists
    if isinstance(a, list) and isinstance(b, list):
        ac = a.copy()
        bc = b.copy()
        while len(ac) > 0 and len(bc) > 0:
            ax = ac.pop(0)
            bx = bc.pop(0)
            comp = compare(ax, bx)
            if comp != CONTINUE:
                return comp
        # left list empty first
        if len(ac) == 0 and len(bc) > 0:
            # print('left list empty')
            return RIGHT
        # right list empty first
        elif len(bc) == 0 and len(ac) > 0:
            # print('right list empty')
            return OUT
        # both empty
        else:
            return CONTINUE

def sort_compare(a, b):
    comp = compare(a, b)
    assert(comp != CONTINUE)
    if comp == RIGHT:
        return -1
    elif comp == OUT:
        return 1

def main():
    packets = [eval(y) for x in open('input.txt').read().strip().split('\n\n') for y in x.split('\n') ]
    packets.append([[2]])
    packets.append([[6]])
    
    packets.sort(key=cmp_to_key(sort_compare))
    a = 0
    b = 0
    for i, packet in enumerate(packets):
        print(packet)
        if packet == [[2]]:
            a = i + 1
        elif packet == [[6]]:
            b = i + 1
    print(a, b, a*b)
main()
