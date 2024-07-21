#!/usr/bin/python
"""Advent of Code 2015, Day 25

https://adventofcode.com/2015/day/25

Given a generated sequence of numbers that is filled onto a grid in a certain
pattern, figure out what number is generated at a set of grid coordinates.

See 25.dat for full data.

Author: Tim Behrendsen
"""

import re
fn = '25.dat'

# Generate coordinate sequence
def seq():
    r, c = 0, 1
    while True:
        r += 1
        work_r, work_c = r, c
        while work_r >= 1:
            yield work_r, work_c
            work_r -= 1
            work_c += 1

# Find the value of row, col
def find(row, col):
    s = seq()
    cur_n, c = 20151125, next(s)
    while True:
        c, cur_n = next(s), (cur_n * 252533) % 33554393
        if c == (row, col):
            return cur_n

row, col = map(int, re.findall('\d+', open(fn, 'r').readline().strip()))
print(f"Answer is {find(row, col)}")
