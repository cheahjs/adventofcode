#!/usr/bin/env python3

totals = []

cur = 0
for line in open('input.txt').readlines():
    line = line.strip()
    if line.isspace() or line == '':
        totals.append(cur)
        cur = 0
        continue
    cur += int(line)

totals.sort(reverse=True)
print(sum(totals[0:3]))