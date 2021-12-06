#!/usr/bin/env python3

import collections


input = [int(i) for i in open('day6-1.txt').readline().split(',')]

# map of age -> population
age_population = {}
for i in range(10):
    age_population[i] = 0

for age in input:
    age_population[age] += 1

for day in range(1, 81):
    # Store spawns for after the decrement stage
    spawning = age_population[0]
    # Decrement all ages
    for i in range(1, 9):
        age_population[i-1], age_population[i] = age_population[i], age_population[i+1]
    age_population[6] += spawning
    age_population[8] += spawning
    print(f'Day {day}:\tPopulation: {sum(age_population.values())}\t{age_population}')
