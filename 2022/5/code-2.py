#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().split('\n')]

    stack_size = len(input[0])//4 + 1
    stacks = [[] for i in range(stack_size)]

    i = 0
    while True:
        line = input[i]
        if line[1] == '1':
            break
        for j in range(stack_size):
            crate = line[1+(j*4)]
            if crate != ' ':
                stacks[j].append(crate)
        i += 1

    i += 2
  
    for i in range(i, len(input)):
        line = input[i]
        params = re.match(r'^move (\d+) from (\d+) to (\d+)', line).group(1, 2, 3)
        print(params)
        count = int(params[0])
        src = int(params[1])-1
        dst = int(params[2])-1
        crates = stacks[src][0:count]
        stacks[src] = stacks[src][count:]
        stacks[dst] = crates + stacks[dst]

    print(stacks)
    print(''.join([x[0] for x in stacks]))
main()
