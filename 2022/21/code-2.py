#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
import z3

def main():
    inp = [x for x in open('input2.txt').read().strip().split('\n')]

    solver = z3.Solver()

    monkeys = {}
    for line in inp:
        name = line[:4]
        monkey = z3.Real(name)
        monkeys[name] = monkey
    
    for line in inp:
        args = line.split(' ')
        name = args[0][:4]
        arg1 = args[1]
        monkey = monkeys[name]
        if name == 'humn':
            humn = monkey
        elif arg1.isdecimal():
            value = int(arg1)
            solver.add(monkey == value)
        else:
            arg2 = args[3]
            op = args[2]
            match op:
                case '+':
                    solver.add(monkey == monkeys[arg1] + monkeys[arg2])
                case '-':
                    solver.add(monkey == monkeys[arg1] - monkeys[arg2])
                case '*':
                    solver.add(monkey == monkeys[arg1] * monkeys[arg2])
                case '/':
                    solver.add(monkey == monkeys[arg1] / monkeys[arg2])
                case '=':
                    solver.add(monkeys[arg1] == monkeys[arg2])
                case _:
                    print('unknown op', op)
                    exit(1)
    
    print(solver.check())
    m = solver.model()
    print(m)
    print(m[humn])

main()
