#!/usr/bin/python
"""Advent of Code 2015, Day 8, Part 1 and Part 2

https://adventofcode.com/2015/day/8

We're given a list of strings with embedded escape sequences (\\, \", \x00). In Part 1,
calculate the difference between the raw length and the in-memory length after taking
into account the escapes. In Part 2, calculate the length of a new string with escapes
added, and display the difference from the raw length.

See 8.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = '8.dat'
hexchars = '0123456789abcdef'

lines = [line.strip() for line in open(fn, 'r')]

code_total, mem_total = 0, 0
for line in lines:
    code_total += len(line)
    idx = 1
    while idx < len(line)-1:
        mem_total += 1
        if line[idx] == '\\':
            if line[idx+1] == '\\' or line[idx+1] == '"':
                idx += 1
            elif line[idx+1] == 'x' and line[idx+2] in hexchars and line[idx+3] in hexchars:
                idx += 3
        idx += 1

print(f"Part 1: {code_total - mem_total}")

# Part 2 simple loop
new_total = len(lines) * 2      # For outer quotes
for line in lines:
    for c in line:
        new_total += 2 if c in ('\\', '"') else 1

# Part 2 one liner just for laughs
new_total = 2*len(lines) + sum(2 if c in ('\\', '"') else 1 for line in lines for c in line)

print(f"Part 2: {new_total - code_total}")
