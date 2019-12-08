#!/usr/bin/python3

import io
from collections import defaultdict

def iterate(graph, start_object, end_object):
    # Vertex to visit, current path
    queue = [(start_object, [start_object])]
    checked = set()

    while queue:
        (vertex, path) = queue.pop(0)
        checked.add(vertex)
        for next in graph[vertex] - checked:
            if next == end_object:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def load_input():
    lines = [l.strip() for l in open('day6-input.txt').readlines()]

    graph = defaultdict(set)
    for line in lines:
        before, after = line.split(')')
        graph[before].add(after)
        graph[after].add(before)

    path = iterate(graph, "YOU", "SAN")
    print(path)
    print(len(path) - 3)


if __name__ == "__main__":
    load_input()
    pass
