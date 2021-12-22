#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from typing import Tuple

@functools.cache
def next(pos1, pos2, score1, score2) -> Tuple[int, int]:
    if score1 >= 21:
        return (1, 0)
    if score2 >= 21:
        return (0, 1)

    acc = (0, 0)

    for rolls in itertools.product([1, 2, 3], repeat=3):
        new_pos1 = (pos1+sum(rolls))%10
        new_score1 = score1 + (new_pos1 + 1)

        # swap 1 and 2 so we roll the dices for 2
        w2, w1 = next(pos2, new_pos1, score2, new_score1)
        acc = (acc[0]+w1, acc[1]+w2)

    return acc

def main():
    input = [int(x.split(': ')[1])
             for x in open('input.txt').read().strip().split('\n')]
    # offset by one so we index from 0-9 instead of 1-10 to make modulo math work
    cur = [input[0]-1, input[1]-1]

    print(max(next(cur[0], cur[1], 0, 0)))

main()
