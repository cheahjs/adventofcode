#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from bitstring import BitArray, BitStream
from collections import defaultdict

LITERAL = 4
SUM = 0
PRODUCT = 1
MIN = 2
MAX = 3
GREATER_THAN = 5
LESS_THAN = 6
EQUAL_TO = 7

def parse_subpacket(a: BitStream, depth=0):
    d = '  '*depth
    version = a.read('uint:3')
    type_id = a.read('uint:3')
    print(d, 'Version:', version, 'Type:', type_id)
    if type_id == LITERAL:
        continuation = True
        val = BitArray()
        while continuation:
            continuation = a.read(1).uint
            val.append(a.read(4))
        # print(d, 'Literal:', val.uint)
        return val.uint
    else:
        # Operator packet
        sub_packet_vals = []
        length_type_id = a.read(1).uint
        if length_type_id == 0:
            # the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet
            total_length = a.read(15).uint
            print(d, 'Total length', total_length)
            cur_pos = a.pos
            while a.pos < cur_pos + total_length:
                sub_packet_vals.append(parse_subpacket(a, depth+1))
        else:
            # the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            number_of_subpackets = a.read(11).uint
            print(d, 'Subpackets:', number_of_subpackets)
            for i in range(number_of_subpackets):
                sub_packet_vals.append(parse_subpacket(a, depth+1))

        if type_id == PRODUCT:
            return functools.reduce(lambda acc, x: acc*x, sub_packet_vals)
        elif type_id == SUM:
            return sum(sub_packet_vals)
        elif type_id == MIN:
            return min(sub_packet_vals)
        elif type_id == MAX:
            return max(sub_packet_vals)
        elif type_id == GREATER_THAN:
            return 1 if sub_packet_vals[0] > sub_packet_vals[1] else 0
        elif type_id == LESS_THAN:
            return 1 if sub_packet_vals[0] < sub_packet_vals[1] else 0
        elif type_id == EQUAL_TO:
            return 1 if sub_packet_vals[0] == sub_packet_vals[1] else 0



def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]

    for line in input:
        a = BitStream('0x' + line)
        print(line)
        print('Calculated:', parse_subpacket(a))
        print('------------')

main()
