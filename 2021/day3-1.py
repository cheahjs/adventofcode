#!/usr/bin/env python3

import collections

def power_consumption(gamma_rate, epsilon_rate):
    return gamma_rate*epsilon_rate


# input = [int(l, 2) for l in open('day1-1.txt').readlines()]

# # LSB = index 0

# # Gamma rate = MSB at most common MSB in input, little endian
# # Epsilon rate =

input = [l.strip() for l in open('day3-1.txt').readlines()]

counts = collections.defaultdict(int)

for l in input:
    for i in range(len(l)):
        counts[i] += 1 if l[i] == '1' else 0

gamma_str = ''
epsilon_str = ''
for i in range(len(input[0])):
    count = counts[i]
    if count > len(input)/2:
        gamma_str = gamma_str + '1'
        epsilon_str = epsilon_str + '0'
    else:
        gamma_str = gamma_str + '0'
        epsilon_str = epsilon_str + '1'

gamma_rate = int(gamma_str, 2)
epsilon_rate = int(epsilon_str, 2)

print(f'Gamma: {gamma_str}\tEpsilon: {epsilon_str}')
print(f'Gamma: {gamma_rate}\tEpsilon: {epsilon_rate}\tPower: {power_consumption(gamma_rate, epsilon_rate)}')
