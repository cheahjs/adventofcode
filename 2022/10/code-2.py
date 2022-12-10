#!/usr/bin/env python3

from dataclasses import dataclass
import re
import collections
import itertools
import functools
from collections import defaultdict
from PIL import Image, ImageDraw

OP_ADDX = 'addx'
OP_NOOP = 'noop'

SIGNAL_CYCLES = [20, 60, 100, 140, 180, 220]

WIDTH = 40
HEIGHT = 6

@dataclass
class Op:
    name: str
    cycles_left: int
    arg: int

def load_op(line):
    parts = line.split(' ')
    if parts[0] == OP_NOOP:
        return Op(OP_NOOP, 0, 0)
    elif parts[0] == OP_ADDX:
        return Op(OP_ADDX, 1, int(parts[1]))
    return None

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]

    input_idx = 1
    cycle = 1
    register_x = 1
    cur_op = load_op(inp[0])
    while cycle < len(inp)*2:
        # print(f'Pre-Cycle {cycle}\t{cur_op}\tX {register_x}')
        print('█' if abs(((cycle-1) % 40) - register_x) <= 1 else ' ', end='')
        if cycle % 40 == 0:
            print()
        if cur_op.cycles_left == 0:
            if cur_op.name == OP_ADDX:
                register_x += cur_op.arg
            elif cur_op.name == OP_NOOP:
                pass
            if input_idx < len(inp):
                cur_op = load_op(inp[input_idx])
                input_idx += 1
            else:
                cur_op = Op(OP_NOOP, 0, 0)
        else:
            cur_op.cycles_left -= 1
        # print(f'Post-Cycle {cycle}\t{cur_op}\tX {register_x}')
        cycle += 1

main()
