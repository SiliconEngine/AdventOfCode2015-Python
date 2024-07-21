#!/usr/bin/python
"""Advent of Code 2015, Day 9, Part 1 and Part 2

https://adventofcode.com/2015/day/9

Classic TSP puzzle (Traveling Santa Problem). Need to find shortest (Part 1)
and longest (Part 2) routes among a set of cities. There are only eight cities,
so brute force is fast.

I also did a bitmap for the visited city list, which was overkill.

See 9.dat for full data.

Author: Tim Behrendsen
"""

import re
from collections import defaultdict

fn = 'test.dat'
fn = '9.dat'

# Generate graph of city nodes
graph = defaultdict(list)
for line in open(fn, 'r'):
    city1, city2, dist = re.findall('(\w+) to (\w+) = (\d+)', line)[0]
    graph[city1].append((city2, int(dist)))
    graph[city2].append((city1, int(dist)))

city_to_idx = {name: idx for idx, name in enumerate(graph.keys())}
shortest, longest = 999999999, 0
target = 2**len(city_to_idx)-1              # Final bitmap of all cities set

# Depth-First-Search for Traveling Salesman Problem
def dfs(graph, city, dist, visited):
    global shortest, longest

    if visited == target:
        longest = max(longest, dist)
        shortest = min(shortest, dist)
        return

    # Visit each unvisited city in turn
    for node in graph[city]:
        city_idx = city_to_idx[node[0]]
        if not (visited & (1 << city_idx)):
            dfs(graph, node[0], dist+node[1], visited | (1 << city_idx))

# Try each city as start city
for city, idx in city_to_idx.items():
    dfs(graph, city, 0, (1 << idx))

print(f"Part 1 is {shortest}")
print(f"Part 2 is {longest}")
