#!/usr/bin/env python3

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'
ARR = ['A', 'B', 'C']
MAP = {
    'A': 0,
    'B': 1,
    'C': 2
}
SCORE = {
    'A': 1,
    'B': 2,
    'C': 3
}
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

lines = [x.strip() for x in open('input.txt').readlines()]
my_score = 0
for line in lines:
    [opp, strat] = line.split(' ')
    if strat == LOSE:
        me = ARR[(MAP[opp]-1)%3]
    elif strat == DRAW:
        me = opp
        my_score += 3
    elif strat == WIN:
        me = ARR[(MAP[opp]+1)%3]
        my_score += 6
    my_score += SCORE[me]

print(my_score)