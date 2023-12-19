#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict

def return_val(x):
    def ret(y):
        return x
    return ret

def evaluate_cond(condition, next):
    def ret(x):
        return next if eval(condition, {}, {'x': x['x'], 'm': x['m'], 'a': x['a'], 's': x['s']}) else None
    return ret

def parse_workflows(lines):
    workflows = {}
    for line in lines:
        name = line.split('{')[0]
        r_rules = line.split('{')[1].replace('}', '').split(',')
        rules = []
        for rule in r_rules:
            if ':' in rule:
                cond, next = rule.split(':')
                if next == 'A':
                    next = True
                elif next == 'R':
                    next = False
                rules.append(functools.partial(evaluate_cond, cond, next)())
            else:
                if rule == 'A':
                    rules.append(lambda x: True)
                elif rule == 'R':
                    rules.append(lambda x: False)
                else:
                    rules.append(functools.partial(return_val, rule)())
        workflows[name] = rules
    return workflows



def main(input_file):
    r_workflows, r_ratings = open(input_file).read().strip().split('\n\n')
    workflows = parse_workflows(r_workflows.split('\n'))
    ratings = [eval(x.replace('=', '":').replace('{', '{"').replace(',', ',"')) for x in r_ratings.split('\n')]
    score = 0
    for rating in ratings:
        next = 'in'
        while isinstance(next, str):
            workflow = workflows[next]
            for rule in workflow:
                next2 = rule(rating)
                if next2 is not None:
                    next = next2
                    break
        print(f'{rating}: {next}')
        if next:
            score += rating['x'] + rating['m'] + rating['a'] + rating['s']
    print(score)

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
