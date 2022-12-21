#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    inp = [int(x) for x in open('test.txt').read().strip().split('\n')]
    cp = inp[:]
    idx_map = [i for i in range(len(inp))]
    def validate(cur_i):
        error = False
        for i in range(cur_i, len(cp)):
            new_i = idx_map[i]
            if cp[i] != inp[new_i]:
                print(f'error: ori_i:{i} ({cp[i]}) maps to new_i:{new_i} ({inp[new_i]})')
                error = True
        if error:
            print(f'bad map: {idx_map}')
    for ori_i, _ in enumerate(idx_map):
        print(f'\ncurrent index: {ori_i}')
        cur_i = idx_map[ori_i]
        val = inp[cur_i]
        if val > 0:
            mov = val % (len(inp)-1)
        elif val == 0:
            mov = 0
        else:
            mov = val % -(len(inp)-1)
        new_i = cur_i + mov
        if new_i < 0:
            new_i = len(inp)-1+new_i
        inp.insert(new_i, inp.pop(cur_i))
        print(f'moving {val} from {cur_i} ({mov}) to {new_i}')
        print(inp)
        for (map_ori_i, map_new_i) in enumerate(idx_map):
            if map_new_i < new_i:
                continue
            if map_new_i == new_i:
                idx_map[map_ori_i] -= 1
            if map_new_i < cur_i:
                idx_map[map_ori_i] += 1
        idx_map[ori_i] = new_i
        validate(ori_i+1)


    print(inp)

main()
