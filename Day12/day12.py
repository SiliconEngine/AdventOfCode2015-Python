#!/usr/bin/python
"""Advent of Code 2015, Day 12, Part 1 and Part 2

https://adventofcode.com/2015/day/12

The input a JSON-formatted data structure. In part 1, we recursively scan the
structure and return a total of all integers. In part 2, we do the same
totaling but do not include any dictionary that contains the word 'red' as
a value.

See 12.dat for full data.

Author: Tim Behrendsen
"""

import json

fn = '12.dat'

def scan(d, ignore_red):
    if type(d) == int:
        return d
    if type(d) == list:
        return sum(scan(d2, ignore_red) for d2 in d)
    if type(d) == dict:
        if ignore_red and 'red' in d.values():
            return 0
        return sum(scan(d2, ignore_red) for d2 in d.values())

    return 0

data = json.loads(open(fn, 'r').read())
print(f"Part 1 is {scan(data, False)}")
print(f"Part 2 is {scan(data, True)}")
