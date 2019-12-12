#!/usr/bin/python3

# https://adventofcode.com/2019/day/10

import math

def read_input(file: str) -> dict:
    asteroid_map: dict = {}
    lines = [l.strip() for l in open(file).readlines()]

    x_index = 0
    y_index = 0

    for line in lines:
        for point in line:
            if point == '#':
                asteroid_map[(x_index, y_index)] = True
            x_index += 1
        y_index += 1
        x_index = 0

    return asteroid_map


def brute_force(asteroid_map: dict) -> int:
    # For each asteroid, calculate the angles of all other asteroid
    most_in_sight = -1
    for (x, y) in asteroid_map:
        angle_list = {}
        for (x2, y2) in asteroid_map:
            if x2 == x and y2 == y:
                continue
            opposite = y2-y
            adjacent = x2-x
            angle = math.atan2(opposite, adjacent)
            angle_list[angle] = True
        seen = len(angle_list)
        if seen > most_in_sight:
            print((x, y), 'is new best')
            most_in_sight = seen
        print((x,y), 'has', seen)
    return most_in_sight


if __name__ == "__main__":
    parsed_input = read_input('day10_input.txt')
    print(brute_force(parsed_input))
    pass