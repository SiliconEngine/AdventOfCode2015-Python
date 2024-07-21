#!/usr/bin/python
"""Advent of Code 2015, Day 13, Part 1 and Part 2

https://adventofcode.com/2015/day/13

We want to place people in a circular table. We're given "happiness scores" that
describe how happy someone is to sit next to each person. Part 1 finds the maximum
happiness score for a permutation. Part 2 adds another person ("self") to the list
and finds that solution.

Doesn't use the itertool permutation function. Instead uses uses a yield from a
recursive function that generates the permutation.

See 13.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = '13.dat'

# Recursively generate all permutations and yield each one
def gen_perms(remaining, current=[]):
    if len(remaining) == 0:
        yield current
    else:
        for i in range(len(remaining)):
            new_c = current + [remaining[i]]
            (new_r := remaining.copy()).pop(i)
            yield from gen_perms(new_r, new_c)

# Run all permutations and figure out best total score
def run(graph):
    people = list(set(c[0] for c in graph.keys()))
    best_score = -999999
    for perm in gen_perms(people):
        score = 0
        for i in range(len(perm)):
            a, b = perm[i], perm[(i+1) % len(perm)]
            score += graph[a + b] + graph[b + a]
        best_score = max(best_score, score)

    return best_score

# Read in data and construct graph for each permutations. Each name
# in the input data has a unique first letter, so just used that.
graph = { }
for line in open(fn, 'r'):
    m = re.findall('(\w).*(gain|lose) (\d+).*to (\w)', line)[0]
    graph[m[0] + m[3]] = int(m[2]) if m[1] == 'gain' else -int(m[2])

print(f"Part 1 is {run(graph)}")

# For Part 2, add in new "self" person
for p in set(c[0] for c in graph.keys()):
    graph[p + 'S'], graph['S' + p] = 0, 0

print(f"Part 2 is {run(graph)}")
