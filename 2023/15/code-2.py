#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def hash(input):
    value = 0
    for char in input:
        value += ord(char)
        value *= 17
        value = value % 256
    return value

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    steps = input[0].split(',')
    total = 0
    boxes = [[] for _ in range(256)]
    labels = set()
    for step in steps:
        if '-' in step:
            label = step.replace('-', '')
            box = hash(label)
            boxes[box] = [b for b in boxes[box] if b[0] != label]
        elif '=' in step:
            label, power = step.split('=')
            power = int(power)
            labels.add(label)
            box = hash(label)
            for i, (l, p) in enumerate(boxes[box]):
                if l == label:
                    boxes[box][i] = (l, power)
                    break
            else:
                boxes[box].append((label, power))
    total = 0
    for b, box in enumerate(boxes):
        for i, (label, power) in enumerate(box):
            p = (b+1) * (i+1) * power
            print(label, p)
            total += p
    print(total)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
