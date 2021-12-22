#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

class Die():
    def __init__(self) -> None:
        self.cur_roll = 1
        self.throws = 0

    def roll(self) -> int:
        roll = self.cur_roll
        self.cur_roll += 1
        if self.cur_roll > 100:
            self.cur_roll = 1
        self.throws += 1
        return roll

def main():
    input = [int(x.split(': ')[1])
             for x in open('input.txt').read().strip().split('\n')]
    print(input)
    score = [0, 0]
    cur = [input[0], input[1]]
    player = 0
    die = Die()

    while score[0] < 1000 and score[1] < 1000:
        rolls = [die.roll(), die.roll(), die.roll()]
        print(
            f'Player {player+1} rolls {rolls[0]} + {rolls[1]} + {rolls[2]} and moves to space {((cur[player] + sum(rolls) - 1) % 10) + 1} for a total score of {score[player] + ((cur[player] + sum(rolls) - 1) % 10) + 1}')
        cur[player] = ((cur[player] + sum(rolls) - 1) % 10) + 1
        score[player] += cur[player]
        player = (player + 1) % 2

    player = (player + 1) % 2
    print(
        f'Player {player+1} reached score {score[player]}, die rolled {die.throws} times.')
    player = (player + 1) % 2
    print(
        f'Loser {player+1} reached score {score[player]}, flag: {score[player]*die.throws}')


main()
