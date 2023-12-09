#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def solve(seq):
    new_seq = []
    end = True
    for i in range(len(seq)-1):
        diff = seq[i+1] - seq[i]
        new_seq.append(diff)
        if diff != 0:
            end = False
    if end:
        return 0
    else:
        ret = new_seq[0] - solve(new_seq)
        return ret

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    seqs = [[int(y) for y in x.split()] for x in input]
    print(sum([seq[0] - solve(seq) for seq in seqs]))

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
