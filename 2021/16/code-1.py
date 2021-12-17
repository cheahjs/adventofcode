#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from bitstring import BitArray, BitStream
from collections import defaultdict

LITERAL = 4

def parse_subpacket(a: BitStream, depth=0):
    d = '  '*depth
    version = a.read('uint:3')
    type_id = a.read('uint:3')
    print(d, 'Version:', version, 'Type:', type_id)
    version_sum = version
    if type_id == LITERAL:
        continuation = True
        val = BitArray()
        while continuation:
            continuation = a.read(1).uint
            val.append(a.read(4))
        print(d, 'Literal:', val.uint)
    else:
        # Operator packet
        length_type_id = a.read(1).uint
        if length_type_id == 0:
            # the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet
            total_length = a.read(15).uint
            print(d, 'Total length', total_length)
            cur_pos = a.pos
            while a.pos < cur_pos + total_length:
                version_sum += parse_subpacket(a, depth+1)
        else:
            # the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            number_of_subpackets = a.read(11).uint
            print(d, 'Subpackets:', number_of_subpackets)
            for i in range(number_of_subpackets):
                version_sum += parse_subpacket(a, depth+1)
    return version_sum
        


def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]

    for line in input:
        a = BitStream('0x' + line)
        print('Version sum:', parse_subpacket(a))
        print('------------')

main()
