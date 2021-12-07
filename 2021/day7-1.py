#!/usr/bin/env python3

input = [int(i) for i in open('day7-1.txt').readline().split(',')]

# Naive approach, test everything
max_val = max(input)

min_fuel_used = 99999999999
min_val = 0
for test in range(max_val):
    fuel_used = 0

    for i in input:
        diff = abs(i - test)
        fuel_used += diff * (diff + 1) // 2

    if fuel_used < min_fuel_used:
        min_fuel_used = fuel_used
        min_val = test

print(min_val, min_fuel_used)
