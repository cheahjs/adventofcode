#!/usr/bin/env python3

from dataclasses import dataclass
import json
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
    
    pulses = {True: 0, False: 0}
    for i in range(1000):
        pulses[False] += 1
        q = [('button', 'broadcaster', 0)]
        while q:
            from_, to, high = q.pop(0)
            s = state[to]
            # print(f'{from_} -{"high" if high else "low"}-> {to}')
            if s.typ == 'broadcast':
                for out in s.outs:
                    q.append((to, out, high))
                pulses[high] += len(s.outs)
            elif s.typ == 'flip':
                if high:
                    continue
                s.high = not s.high
                for out in s.outs:
                    q.append((to, out, s.high))
                pulses[s.high] += len(s.outs)
            elif s.typ == 'and':
                s.ins[from_] = high
                send = not all(s.ins.values())
                for out in s.outs:
                    q.append((to, out, send))
                pulses[send] += len(s.outs)
    print(pulses)
    print(pulses[0]*pulses[1])


main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
