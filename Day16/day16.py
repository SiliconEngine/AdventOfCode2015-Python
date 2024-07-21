#!/usr/bin/python
"""Advent of Code 2015, Day 16, Part 1 and Part 2

https://adventofcode.com/2015/day/16

Given a gift that is scanned to produce a set of personal attributes, compare
those against a list of "Aunt Sue" attributes to determine the matching one. In part
2, the rules are modified slightly based on the attribute type.

See 16.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = '16.dat'

gift = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
    'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1
}

sues = []
for line in open(fn, 'r'):
    sues.append({ k: int(n) for k, n in ((k, n) for k, n in re.findall('(\w+): (\d+)', line))})

# Part 1, find matching Aunt Sue with attributes that don't match gift
for idx, sue in enumerate(sues):
    if not any(gift[k] != n for k, n in sue.items()):
        part1 = idx+1

print(f"Part 1 is {part1}")

# Part 2, find matching Aunt Sue with modified rules.
for idx, sue in enumerate(sues):
    for k, n in sue.items():
        if k in ('cats', 'trees'):
            if gift[k] > n:
                break
        elif k in ('pomeranians', 'goldfish'):
            if gift[k] < n:
                break
        elif gift[k] != n:
            break
    else:               # Must not be the one from part 1
        if idx+1 != part1:
            part2 = idx+1

print(f"Part 2 is {part2}")
