#!/usr/bin/python
"""Advent of Code 2015, Day 5, Part 1 and Part 2

https://adventofcode.com/2015/day/5

Santa has a list of strings that need to evaluated whether they're nice or not.
Part 1 gives us a list of rules, while Part 2 gives us a list of different rules.
Total up the number of nice strings in each part.

See 5.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = '5.dat'

# Part 1 nice checker
def is_nice1(s):
    # 1) Must not contain ab, cd, pq, xy
    # 2) Must have at least three vowels
    # 3) Must have a repeated letter.
    return 1 if not re.search(r'ab|cd|pq|xy', s) and \
        len(re.findall(r'[aeiou]', s)) >= 3 and \
        re.search(r'(\w)\1', s) else 0

# Part 2 nice checker
def is_nice2(s):
    # 1) A pair of characters must also exist elsewhere in the string
    # 2) Must have a pattern of letter1/letter2/letter1
    return 1 if re.search(r'(\w\w).*\1', s) and re.search(r'(\w)\w\1', s) else 0

lines = [line.strip() for line in open(fn, 'r')]
print(f"Part 1 is {sum(is_nice1(s) for s in lines)}")
print(f"Part 2 is {sum(is_nice2(s) for s in lines)}")
