#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
import heapq
from collections import defaultdict

# -----> +y
# |
# |
# v +x

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
d = {
    LEFT: (0, -1),
    UP: (-1, 0),
    RIGHT: (0, 1),
    DOWN: (1, 0)
}

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    grid = {}
    for x, row in enumerate(input):
        for y, col in enumerate(row):
            grid[(x, y)] = int(col)
    max_x = len(input)
    max_y = len(input[0])
    end = (max_x - 1, max_y - 1)
    # store (x, y, direction, steps forward)
    visited = {}
    # heat loss (cost), (x, y), direction, steps forward
    q = [(0, (0, 0), RIGHT, 1), (0, (0, 0), DOWN, 1)]
    while q:
        (heat_loss, (x, y), direction, steps) = heapq.heappop(q)
        # check for possible directions based on steps
        if steps < 4:
            # less than 4 steps, we can only go straight
            new_dirs = [direction]
        elif steps < 10:
            # less than 10 steps, we can go straight or turn left or right
            new_dirs = [direction, (direction - 1) % 4, (direction + 1) % 4]
        elif steps == 10:
            # 10 steps, we can only turn left or right
            new_dirs = [(direction - 1) % 4, (direction + 1) % 4]
        else:
            # error
            raise Exception("steps should not be more than 10")
        for new_dir in new_dirs:
            new_x = x + d[new_dir][0]
            new_y = y + d[new_dir][1]
            new_steps = steps + 1 if new_dir == direction else 1
            # ignore if we are out of bounds
            if new_x >= max_x or new_x < 0 or new_y >= max_y or new_y < 0:
                continue
            new_heat_loss = heat_loss + grid[(new_x, new_y)]
            if (new_x, new_y) == end:
                print('found end', new_heat_loss)
            # if we have not visited the node, or we have visited it but with a higher heat loss
            # then we can update the heat loss and add it to the queue
            if (new_x, new_y, new_dir, new_steps) not in visited or visited[(new_x, new_y, new_dir, new_steps)] > new_heat_loss:
                visited[(new_x, new_y, new_dir, new_steps)] = new_heat_loss
                heapq.heappush(q, (new_heat_loss, (new_x, new_y), new_dir, new_steps))
    # find the lowest heat loss at the end node
    print(min(heat_loss for (x, y, direction, steps), heat_loss in visited.items() if (x, y) == end))
        

            
main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
