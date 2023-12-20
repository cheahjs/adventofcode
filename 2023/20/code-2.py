#!/usr/bin/env python3

from dataclasses import dataclass
import json
import math
import re
import collections
import itertools
import functools
import sys
from collections import defaultdict, namedtuple

@dataclass
class S:
    typ: str
    high: int
    ins: dict
    outs: list

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    state = defaultdict(lambda: S(None, False, {}, []))
    for line in input:
        start, outs = line.split(' -> ')
        ends = outs.split(', ')
        # flip flop
        if start[0] == '%':
            start = start[1:]
            state[start].typ = 'flip'
        elif start[0] == '&':
            start = start[1:]
            state[start].typ = 'and'
        else:
            state[start].typ = 'broadcast'
        state[start].outs = ends
        for out in ends:
            state[out].ins[start] = False
    
    # find the and gate that triggers rx
    and_gate = list(state['rx'].ins.keys())[0]
    # find all the dependencies of the and gate
    deps = {x: None for x in state[and_gate].ins.keys()}
    # find the number of presses needed to trigger each dependency
    presses = 0
    while any(x is None for x in deps.values()):
        if presses % 100000 == 0:
            print(presses)
        presses += 1
        q = [('button', 'broadcaster', 0)]
        while q:
            from_, to, high = q.pop(0)
            if not high and to in deps:
                if deps[to] is None:
                    deps[to] = presses
                    print(f'{to} triggered at {presses}')
            s = state[to]
            # print(f'{from_} -{"high" if high else "low"}-> {to}')
            if s.typ == 'broadcast':
                for out in s.outs:
                    q.append((to, out, high))
            elif s.typ == 'flip':
                if high:
                    continue
                s.high = not s.high
                for out in s.outs:
                    q.append((to, out, s.high))
            elif s.typ == 'and':
                s.ins[from_] = high
                send = not all(s.ins.values())
                for out in s.outs:
                    q.append((to, out, send))
    print(deps)
    print(math.lcm(*deps.values()))


main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
