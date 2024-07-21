#!/usr/bin/python
"""Advent of Code 2015, Day 4, Part 1 and Part 2

https://adventofcode.com/2015/day/4

Scan a series of MD5 hashes. For Part 1, identify the index of the
hash that starts with five zeroes. For Part 2, it's six zeroes.

Author: Tim Behrendsen
"""

from hashlib import md5
from itertools import count

key = 'bgvyzdsv'

target1, target2, part1, part2 = '0' * 5, '0' * 6, None, None
for i in count(0):
    h = md5((key + str(i)).encode('utf-8')).hexdigest()
    if part1 == None and h.startswith(target1):
        part1 = i
    if part2 == None and h.startswith(target2):
        part2 = i
    if part1 != None and part2 != None:
        break

print(f"Part 1 is {part1}")
print(f"Part 2 is {part2}")
