#!/usr/bin/python3

# https://adventofcode.com/2019/day/10

import math
from collections import defaultdict

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


def brute_force(asteroid_map: dict):
    # For each asteroid, calculate the angles of all other asteroid
    most_in_sight = -1
    best_coord = None
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
            most_in_sight = seen
            best_coord = (x, y)
    print('Best coord:', best_coord)
    x = best_coord[0]
    y = best_coord[1]
    angle_list = {}
    for (x2, y2) in asteroid_map:
        if x2 == x and y2 == y:
            continue
        opposite = y-y2
        adjacent = x2-x
        angle = math.atan2(adjacent, opposite)
        if angle < 0:
            angle = 2*math.pi + angle
        if angle not in angle_list:
            angle_list[angle] = {'count': 0, 'asteroids': {}}
        angle_list[angle]['count'] += 1
        angle_list[angle]['asteroids'][(x2, y2)] = math.sqrt((x2-x)**2 + (y2-y)**2)

    vaporized_index = 1
    item_list = angle_list.items()
    new_item_list = []
    while len(item_list) > 0:
        print('----------Starting cycle')
        for (angle, value) in sorted(item_list):
            if value['count'] == 0:
                continue
            print('Evaluating', angle, value)
            value['count'] -= 1
            min_dist = 99999999
            min_coord = None
            for asteroid, distance in value['asteroids'].items():
                if distance < min_dist:
                    min_dist = distance
                    min_coord = asteroid
            print(vaporized_index, ': Vaporizing', min_coord)
            # if vaporized_index == 200:
            #     print(min_coord[0] * 100 + min_coord[1])
            #     break
            del value['asteroids'][min_coord]

            new_item_list.append((angle, value))
            vaporized_index += 1
        item_list = new_item_list
        new_item_list = []



# (23, 19) is new best
# (23, 19) has 278
if __name__ == "__main__":
    # parsed_input = read_input('day10_input.txt')
    # print(brute_force(read_input('day10_test5.txt')))
    print(brute_force(read_input('day10_input.txt')))
    pass