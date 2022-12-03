#!/usr/bin/env python3

totals = []

cur = 0
highest = 0
for line in open('input.txt').readlines():
    line = line.strip()
    if line.isspace() or line == '':
        totals.append(cur)
        if cur > highest:
            highest = cur
        cur = 0
        continue
    cur += int(line)

print(highest)