#!/usr/bin/env python3

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'
ROCK_ENC = 'X'
PAPER_ENC = 'Y'
SCISSORS_ENC = 'Z'

lines = [x.strip() for x in open('input.txt').readlines()]
my_score = 0
for line in lines:
    [opp, me] = line.split(' ')
    if me == ROCK_ENC:
        my_score += 1
        if opp == ROCK:
            my_score += 3
        elif opp == PAPER:
            my_score += 0
        elif opp == SCISSORS:
            my_score += 6
    elif me == PAPER_ENC:
        my_score += 2
        if opp == ROCK:
            my_score += 6
        elif opp == PAPER:
            my_score += 3
        elif opp == SCISSORS:
            my_score += 0
    elif me == SCISSORS_ENC:
        my_score += 3
        if opp == ROCK:
            my_score += 0
        elif opp == PAPER:
            my_score += 6
        elif opp == SCISSORS:
            my_score += 3
    else:
        print('unknown me:', me)
        exit(1)
print(my_score)