#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict

def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]
    sum = 0
    for line in input:
        # Convert English words to digits, starting from left to right
        new_line = ''
        for pos in range(len(line)):
            if len(line) - pos >= 3:
                if line[pos:pos+3] == 'one':
                    new_line += '1'
                elif line[pos:pos+3] == 'two':
                    new_line += '2'
                elif line[pos:pos+3] == 'six':
                    new_line += '6'
            if len(line) - pos >= 4:
                if line[pos:pos+4] == 'zero':
                    new_line += '0'
                elif line[pos:pos+4] == 'four':
                    new_line += '4'
                elif line[pos:pos+4] == 'five':
                    new_line += '5'
                elif line[pos:pos+4] == 'nine':
                    new_line += '9'
            if len(line) - pos >= 5:
                if line[pos:pos+5] == 'three':
                    new_line += '3'
                elif line[pos:pos+5] == 'seven':
                    new_line += '7'
                elif line[pos:pos+5] == 'eight':
                    new_line += '8'
            new_line += line[pos]
        print(line)
        print(new_line)
        digits = []
        for char in new_line:
            if char.isdigit():
                digits.append(char)
        num = int(''.join([digits[0], digits[-1]]))
        print(num)
        sum += num
    print(sum)

main()
