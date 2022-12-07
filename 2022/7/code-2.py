#!/usr/bin/env python3

import re
import collections
import itertools
import functools
from collections import defaultdict
from dataclasses import dataclass
from typing import Type, Optional

@dataclass
class Node():
    parent: Type['Node']
    name: str
    is_dir: bool
    size: int
    children: dict[str, Type['Node']]

    def resolve_path(self) -> str:
        if self.name == '/':
            return ''
        return self.parent.resolve_path() + '/' + self.name

    def get_size(self) -> int:
        if not self.is_dir:
            return self.size
        return sum([child.get_size() for child in self.children.values()])

    def print(self, indent: int) -> None:
        print(f"{' '*indent}- {self.name} ({'dir, size=' if self.is_dir else 'file, size='}{str(self.get_size())})")
        for child in self.children.values():
            child.print(indent + 2)


def main():
    input = [x for x in open('input.txt').read().strip().split('\n')]

    i = 0
    root = Node(parent=None, name='/', is_dir=True, size=0, children={})
    cwd = root
    while i < len(input):
        line = input[i]
        args = line.split(' ')
        assert(args[0] == '$')
        if args[1] == 'cd':
            if args[2] == '/':
                cwd = root
            elif args[2] == '..':
                cwd = cwd.parent
            else:
                cwd = cwd.children[args[2]]
        elif args[1] == 'ls':
            i += 1
            while i < len(input):
                new_line = input[i]
                new_args = new_line.split(' ')
                if new_args[0] == '$':
                    i -= 1
                    break
                if new_args[0] == 'dir':
                    cwd.children[new_args[1]] = Node(parent=cwd, name=new_args[1], is_dir=True, size=0, children={})
                else:
                    cwd.children[new_args[1]] = Node(parent=cwd, name=new_args[1], is_dir=False, size=int(new_args[0]), children={})
                i += 1
        i += 1
    root.print(0)

    dir_sizes = {}
    queue: list[Node] = [root]
    total_avail = 70000000
    cur_free = total_avail - root.get_size()
    req_free = 30000000
    rem_free = req_free - cur_free
    smallest_dir = total_avail
    puzzle = -1
    while len(queue) > 0:
        pop = queue.pop()
        if pop.is_dir:
            queue.extend(pop.children.values())
            dir_size = pop.get_size()
            dir_sizes[pop.resolve_path()] = dir_size
            if dir_size < smallest_dir and dir_size > rem_free:
                puzzle = dir_size
    print(dir_sizes)
    print(puzzle)


main()
