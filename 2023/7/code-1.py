#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
import os
from collections import defaultdict

DEBUG = bool(os.environ.get('DEBUG', False))

def remap(hand):
    return hand.replace('A', 'E').replace('T', 'A').replace('J', 'B').replace('Q', 'C').replace('K', 'D')

def parse(hand):
    is_five = (False, None)
    is_four = (False, None)
    is_full_house = (False, None, None)
    is_three = (False, None)
    is_two_pair = (False, None, None)
    is_one_pair = (False, None)
    high_card = None
    for card in hand:
        if hand.count(card) == 5:
            is_five = (True, card)
            break
        elif hand.count(card) == 4:
            is_four = (True, card)
            break
        elif hand.count(card) == 3:
            is_three = (True, card)
        elif hand.count(card) == 2:
            if is_one_pair[0] and card != is_one_pair[1]:
                if is_one_pair[1] > card:
                    is_two_pair = (True, is_one_pair[1], card)
                else:
                    is_two_pair = (True, card, is_one_pair[1])
                is_one_pair = (False, None)
            else:
                is_one_pair = (True, card)
        if not high_card or card > high_card:
            high_card = card
    if is_three[0] and is_one_pair[0]:
        is_full_house = (True, is_three[1], is_one_pair[1])
        is_three = (False, None)
        is_one_pair = (False, None)
    if DEBUG:
        print(f'{"".join(sorted([x for x in hand]))}: is_five={is_five}, is_four={is_four}, is_full_house={is_full_house}, is_three={is_three}, is_two_pair={is_two_pair}, is_one_pair={is_one_pair}, high_card={high_card}')
    return (is_five, is_four, is_full_house, is_three, is_two_pair, is_one_pair, high_card)

def break_tie(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return -1
        elif a[i] < b[i]:
            return 1
    else:
        raise Exception('unexpected tie', a, b)

def compare(a, b):
    a_parsed = parse(a[0])
    b_parsed = parse(b[0])
    for i in range(len(a_parsed)):
        if a_parsed[i][0] and not b_parsed[i][0]:
            return -1
        elif not a_parsed[i][0] and b_parsed[i][0]:
            return 1
        else:
            if a_parsed[i][0]:
                return break_tie(a, b)

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    hand_bid = [(remap(y[0]), int(y[1])) for y in [x.split() for x in input]]
    if DEBUG:
        for hand, bid in hand_bid:
            parse(hand)
    else:
        hand_bid.sort(key=functools.cmp_to_key(compare), reverse=True)
        for a in hand_bid:
            print(a)
        winnings = 0
        for i in range(len(hand_bid)):
            winnings += hand_bid[i][1] * (i+1)
        print(winnings)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
