#!/usr/bin/python
"""Advent of Code 2015, Day 24, Part 1 and Part 2

https://adventofcode.com/2015/day/24

Santa needs to divide the weights of his presents equally, and also needs the
least number in one compartment for legroom. Calculate the least number of
presents that also will divide equally. For those sets, we want to pick the
set with the lowest product of the weights. Part 1 divides into a set of 3,
and part 2 divides into a set of 4.

See 24.dat for full data.

Author: Tim Behrendsen
"""

from itertools import combinations
from functools import reduce

fn = '24.dat'

def calc(weights, groups):
    target = sum(weights) // groups
    # Count up and generate combinations for each smallest group until we
    # find the smallest that can total to the target weight.
    for min_count in range(1, len(weights)):
        found = [c for c in combinations(weights, min_count) if sum(c) == target]
        if found:
            return min(reduce(lambda a, b: a * b, c) for c in found)

weights = [ int(line.strip()) for line in open(fn, 'r') ]
print(f"Part 1 is {calc(weights, 3)}")
print(f"Part 2 is {calc(weights, 4)}")
