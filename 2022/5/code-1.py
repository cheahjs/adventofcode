#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().split('\n')]

    stack_size = 9
    highest_stack = 8
    instruction_start = highest_stack+2
    stacks = [[] for i in range(stack_size)]

    for i in range(highest_stack):
        line = input[i]
        for j in range(stack_size):
            crate = line[1+(j*4)]
            if crate != ' ':
                stacks[j].append(crate)
    
    for i in range(instruction_start, len(input)):
        line = input[i]
        params = re.match(r'^move (\d+) from (\d+) to (\d+)', line).group(1, 2, 3)
        print(params)
        count = int(params[0])
        src = int(params[1])-1
        dst = int(params[2])-1
        for j in range(count):
            crate = stacks[src].pop(0)
            stacks[dst].insert(0, crate)

    print(stacks)
    print(''.join([x[0] for x in stacks]))
main()
