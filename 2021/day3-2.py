#!/usr/bin/env python3

def power_consumption(gamma_rate, epsilon_rate):
    return gamma_rate*epsilon_rate


def count_and_filter_bits(input, bit_pos, most_common):
    if len(input) == 1:
        return input
    count = 0
    ones = []
    zeroes = []
    for l in input:
        if l[bit_pos] == '1':
            count += 1
            ones.append(l)
        else:
            zeroes.append(l)
    if count >= len(input)-count:
        # Ones most common
        if most_common:
            return ones
        else:
            return zeroes
    else:
        # Zeroes most common
        if most_common:
            return zeroes
        else:
            return ones


input = [l.strip() for l in open('day3-1.txt').readlines()]

oxygen_list = input
co2_list = input
for i in range(len(input[0])):
    oxygen_list = count_and_filter_bits(oxygen_list, i, True)
    co2_list = count_and_filter_bits(co2_list, i, False)

print('Oxygen', oxygen_list, int(oxygen_list[0], 2))
print('CO2', co2_list, int(co2_list[0], 2))
print('Value', int(oxygen_list[0], 2)*int(co2_list[0], 2))
