#!/usr/bin/env python3

import re
import collections
import itertools
import functools
import sys
from collections import defaultdict, namedtuple

P = namedtuple('P', ['x', 'y'])

# grid (x, y)
# -----> +y
# |
# |
# v +x
pipes = ['|', '-', 'L', 'J', '7', 'F']
left = P(0, -1)
right = P(0, 1)
up = P(-1, 0)
down = P(1, 0)
pipe_maps = {
    '|': [up, down],
    '-': [left, right],
    'L': [up, right],
    'J': [up, left],
    '7': [left, down],
    'F': [right, down],
}

def main(input_file):
    input = [x for x in open(input_file).read().strip().split('\n')]
    grid = [list(x) for x in input]
    dist = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Scan the grid to find the start position
    def find_start_pos():
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 'S':
                    return P(row, col)
    def find_connected_pipes(pos):
        cur_pipe = grid[pos.x][pos.y]
        if cur_pipe == '.':
            return None
        # print(f'finding connected pipes for {pos} ({cur_pipe})')
        connected = []
        for dir in pipe_maps[cur_pipe]:
            next_pos = P(pos.x + dir.x, pos.y + dir.y)
            if next_pos.x < 0 or next_pos.x >= len(grid) or next_pos.y < 0 or next_pos.y >= len(grid[0]):
                continue
            # print(f'evaluating dir {dir}: {next_pos}: {grid[next_pos.x][next_pos.y]}')
            if grid[next_pos.x][next_pos.y] != '.':
                connected.append(next_pos)
        return connected
    def find_loop_path():
        start_pos = find_start_pos()
        # The start is connected to two pipes, so there's two branches to explore
        # The path loops back onto the start position
        # Perform DFS to find the loop, and the furthest distance is half the length of the loop
        # We don't know what the start pipe is, so try all of them
        for start_pipe in pipes:
            print(f'Finding loop for start pipe {start_pipe}')
            grid[start_pos.x][start_pos.y] = start_pipe
            distance = 0
            cur_pos = start_pos
            last_pos = cur_pos
            visited = set()
            try:
                while distance == 0 or cur_pos != start_pos:
                    # print(f'cur_pos: {cur_pos} ({grid[cur_pos.x][cur_pos.y]}), distance: {distance}')
                    visited.add(cur_pos)
                    next_poses = find_connected_pipes(cur_pos)
                    # print(f'next_poses: {next_poses}')
                    for next in next_poses:
                        if next not in visited or (next == start_pos and distance > 2):
                            next_pos = next
                            break
                    else:
                        raise Exception('No next position found')
                    distance += 1
                    last_pos = cur_pos
                    cur_pos = next_pos
                # Check if the start is connected
                if last_pos not in find_connected_pipes(start_pos):
                    raise Exception('Start not connected')
                print(f'Loop found with total distance {distance} (half: {distance // 2})')
                return visited
            except Exception as e:
                print(e)
                continue
    loop_path = find_loop_path()
    # Use the odd-even rule to determine if a node is inside of the loop:
    # https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
    # We iterate from left-to-right.
    # Every time we traverse a vertical pipe, we flip the parity.
    # What are considered vertical pipes:
    # | is obvious
    # We can either use the pairs F7 or LJ
    # Visualise this by blowing up each point to a 3x3 grid, and casting the ray on the top or bottom row
    # On the top row, the ray would hit L and J but not F or 7, similarly vice versa
    enclosed = 0
    for x, row in enumerate(grid):
        is_enclosed = False
        for y, grid_val in enumerate(row):
            if P(x,y) in loop_path:
                if grid_val in '|F7':
                    is_enclosed = not is_enclosed
            else:
                if is_enclosed:
                    grid[x][y] = 'I'
                    enclosed += 1
                else:
                    grid[x][y] = 'O'
    print(f'Enclosed area: {enclosed}')
    print('\n'.join([''.join(x) for x in grid]))
            

main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
