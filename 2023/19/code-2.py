#!/usr/bin/env python3

from dataclasses import dataclass
import re
import collections
import itertools
import functools
import sys
from collections import defaultdict, namedtuple

@dataclass
class Range:
    current_workflow: str
    current_workflow_rule: int
    x: tuple[int, int]
    m: tuple[int, int]
    a: tuple[int, int]
    s: tuple[int, int]

    def count_combinations(self):
        return (self.x[1] - self.x[0] + 1) * (self.m[1] - self.m[0] + 1) * (self.a[1] - self.a[0] + 1) * (self.s[1] - self.s[0] + 1)
    
    def split(self, field, comparator, value, next):
        new_ranges = []
        match field:
            case 'x':
                match comparator:
                    case '<':
                        # x < value, reduce the top range for next
                        new_ranges.append(Range(next, 0, (self.x[0], value-1), self.m, self.a, self.s))
                        # continue for x >= value, reduce the bottom range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, (value, self.x[1]), self.m, self.a, self.s))
                    case '>':
                        # x > value, reduce the bottom range for next
                        new_ranges.append(Range(next, 0, (value+1, self.x[1]), self.m, self.a, self.s))
                        # continue for x <= value, reduce the top range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, (self.x[0], value), self.m, self.a, self.s))
            case 'm':
                match comparator:
                    case '<':
                        # m < value, reduce the top range for next
                        new_ranges.append(Range(next, 0, self.x, (self.m[0], value-1), self.a, self.s))
                        # continue for m >= value, reduce the bottom range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, self.x, (value, self.m[1]), self.a, self.s))
                    case '>':
                        # m > value, reduce the bottom range for next
                        new_ranges.append(Range(next, 0, self.x, (value+1, self.m[1]), self.a, self.s))
                        # continue for m <= value, reduce the top range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, self.x, (self.m[0], value), self.a, self.s))
            case 'a':
                match comparator:
                    case '<':
                        # a < value, reduce the top range for next
                        new_ranges.append(Range(next, 0, self.x, self.m, (self.a[0], value-1), self.s))
                        # continue for a >= value, reduce the bottom range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, self.x, self.m, (value, self.a[1]), self.s))
                    case '>':
                        # a > value, reduce the bottom range for next
                        new_ranges.append(Range(next, 0, self.x, self.m, (value+1, self.a[1]), self.s))
                        # continue for a <= value, reduce the top range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, self.x, self.m, (self.a[0], value), self.s))
            case 's':
                match comparator:
                    case '<':
                        # s < value, reduce the top range for next
                        new_ranges.append(Range(next, 0, self.x, self.m, self.a, (self.s[0], value-1)))
                        # continue for s >= value, reduce the bottom range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, self.x, self.m, self.a, (value, self.s[1])))
                    case '>':
                        # s > value, reduce the bottom range for next
                        new_ranges.append(Range(next, 0, self.x, self.m, self.a, (value+1, self.s[1])))
                        # continue for s <= value, reduce the top range
                        new_ranges.append(Range(self.current_workflow, self.current_workflow_rule+1, self.x, self.m, self.a, (self.s[0], value)))
        return new_ranges



def parse_workflows(lines):
    workflows = {}
    for line in lines:
        name = line.split('{')[0]
        rules = line.split('{')[1].replace('}', '').split(',')
        workflows[name] = rules
    return workflows


def main(input_file):
    r_workflows, _ = open(input_file).read().strip().split('\n\n')
    workflows = parse_workflows(r_workflows.split('\n'))
    ranges = [Range('in', 0, (1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    final = []
    while ranges:
        pot_range = ranges.pop()
        # end conditions
        if pot_range.current_workflow == 'A':
            final.append(pot_range)
            continue
        if pot_range.current_workflow == 'R':
            continue

        workflow = workflows[pot_range.current_workflow]
        rule = workflow[pot_range.current_workflow_rule]
        if ':' not in rule:
            pot_range.current_workflow = rule
            pot_range.current_workflow_rule = 0
            ranges.append(pot_range)
        else:
            cond, next = rule.split(':')
            field = cond[0]
            comparator = cond[1]
            value = int(cond[2:])
            ranges.extend(pot_range.split(field, comparator, value, next))
    print(final)
    print(sum(x.count_combinations() for x in final))

    

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
