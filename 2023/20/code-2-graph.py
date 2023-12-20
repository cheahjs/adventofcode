#!/usr/bin/env python3

from dataclasses import dataclass
import json
import re
import collections
import itertools
import functools
import sys
from collections import defaultdict, namedtuple

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    print("@startuml Day20")
    print('[*] --> broadcaster')
    for line in input:
        start, outs = line.split(' -> ')
        ends = outs.split(', ')
        if start[0] in ['%', '&']:
            print(f'{start[1:]} : {start[0]}')   
            start = start[1:]
        for end in ends:
            print(f'{start} --> {end}')
        
    print("@enduml")
        

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
