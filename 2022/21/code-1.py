#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
import dataclasses
from typing import Optional, Callable

OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

@dataclasses.dataclass
class monkey():
    value: Optional[int]
    arg1: Optional[str]
    arg2: Optional[str]
    op: Optional[Callable[[int, int], int]]

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]

    monkeys: dict[str, monkey] = {}
    for line in inp:
        args = line.split(' ')
        name = args[0][:4]
        arg1 = args[1]
        if arg1.isdecimal():
            monkeys[name] = monkey(int(arg1), None, None, None)
        else:
            monkeys[name] = monkey(None, arg1, args[3], OPS[args[2]])

    def resolve(name):
        monke = monkeys[name]
        if monke.value:
            return monke.value
        value = monke.op(resolve(monke.arg1), resolve(monke.arg2))
        monke.value = value
        return value

    print(resolve('root'))

main()
