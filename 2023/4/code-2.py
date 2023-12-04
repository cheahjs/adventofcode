#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    cards = defaultdict(int)
    for line in input:
        card_num = int(line.split(': ')[0].split()[1])
        cards[card_num] += 1
        raw_winning, raw_numbers = line.split(': ')[1].split(' | ')
        winning = set([int(x) for x in raw_winning.split()])
        numbers = [int(x) for x in raw_numbers.split()]
        count = 0
        for number in numbers:
            if number in winning:
                count += 1
                cards[card_num + count] += cards[card_num]
    print(sum(cards.values()))

main()
