#!/usr/bin/env python3

from dataclasses import dataclass
import re
import collections
import itertools
import functools
from collections import defaultdict

@dataclass
class Monkey:
    items: list[int]
    op: str
    divisible_test: list[int]
    inspect_count: int

    def eval(self, param):
        old = param
        return eval(self.op)

def main():
    inp = [x for x in open('input.txt').read().strip().split('\n')]

    monkeys: list[Monkey] = []
    cm = 1
    for line in inp:
        if line.startswith("Monkey"):
            monkey = Monkey(None, None, None, 0)
            monkeys.append(monkey)
        elif line.startswith("  Starting items:"):
            line = line.replace("  Starting items: ", "")
            monkey.items = [int(x) for x in line.split(', ')]
        elif line.startswith("  Operation: "):
            monkey.op = line.replace("  Operation: new = ", "")
        elif line.startswith("  Test:"):
            monkey.divisible_test = [int(line.split(' ')[-1])]
            cm *= int(line.split(' ')[-1])
        elif line.startswith("    If"):
            monkey.divisible_test.append(int(line.split(' ')[-1]))

    print(monkeys)

    for r in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspect_count += 1
                item = monkey.eval(item)
                item %= cm
                if item % monkey.divisible_test[0] == 0:
                    monkeys[monkey.divisible_test[1]].items.append(item)
                else:
                    monkeys[monkey.divisible_test[2]].items.append(item)
            monkey.items = []
        if (r+1) % 100 == 0:
            print(f'Round {r+1}')
            for i, monkey in enumerate(monkeys):
                print(f'Monkey {i} inspected items {monkey.inspect_count} times.')
    monkeys.sort(key=lambda x: x.inspect_count, reverse=True)
    print(monkeys[0].inspect_count * monkeys[1].inspect_count)
main()
