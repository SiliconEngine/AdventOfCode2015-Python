#!/usr/bin/python
"""Advent of Code 2015, Day 1, Part 1 and Part 2

https://adventofcode.com/2015/day/1

Input data is a list of parenthesis representing elevator moves, with '('
going up a floor, and ')' down a floor. Part 1 calculates the final floor.
Part 2 shows the index where it first goes into the basement.

See 1.dat for full data.

Author: Tim Behrendsen
"""

fn = '1.dat'

line = open(fn, 'r').readline().strip()
floor, part2 = 0, None
for idx, c in enumerate(line):
    floor += 1 if c == '(' else -1
    if floor < 0 and part2 == None:
        part2 = idx+1

print(f"Part 1 is {floor}")
print(f"Part 2 is {part2}")
