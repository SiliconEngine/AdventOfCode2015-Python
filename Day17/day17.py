#!/usr/bin/python
"""Advent of Code 2015, Day 17, Part 1 and Part 2

https://adventofcode.com/2015/day/17

Given a list of container sizes, part 1 calculates the number of combinations
that can hold exactly 150 liters in total. Part 2 calculates the minimum number
of containers needed, and how many combinations have that total.

See 17.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = '17.dat'
caps = [ int(n) for n in (line.strip() for line in open(fn, 'r')) ]

# Recursively generate all combos and yield each one
def gen_combos(caps, cur_idx=0, cur_sum=0, current_list=[]):
    for i in range(cur_idx, len(caps)):
        new_sum = cur_sum + caps[i]
        if new_sum == 150:
            yield current_list + [caps[i]]
        elif new_sum < 150:
            yield from gen_combos(caps, i+1, new_sum, current_list + [caps[i]])

# Generate all combinations and track the number at different lengths
len_count = defaultdict(int)
for combo in gen_combos(caps):
    len_count[len(combo)] += 1

print(f"Part 1 is {sum(v for v in len_count.values())}")
print(f"Part 2 is {len_count[min(k for k in len_count.keys())]}")
