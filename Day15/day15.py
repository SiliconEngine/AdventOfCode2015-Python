#!/usr/bin/python
"""Advent of Code 2015, Day 15, Part 1 and Part 2

https://adventofcode.com/2015/day/15

We're given a list of cookie ingredients, along with various attributes. The
total amount of ingredients must total 100 and we want to optimize the attributes.
Part 1 optimizes the ingredients, without the calories. Part 2 optimizes the
ingredients and requires the total calories to be 500.

See 15.dat for full data.

Author: Tim Behrendsen
"""

import re
from types import SimpleNamespace as Data

fn = '15.dat'

# Generate amount combinations
def gen_amts(ings, amts=[]):
    if len(amts) == len(ings):
        yield amts
    else:
        # If last ingredient, it has to be the amount to total 100.
        cur_total = sum(amts, 0)
        start_amt = 0 if len(amts) < len(ings)-1 else 100-cur_total
        for amt in range(start_amt, 101-cur_total):
            yield from gen_amts(ings, amts + [amt])

# Calculate score+calories of an amount combination
def calc_score(ings, amts):
    cap, dur, flav, txr, cal = 0, 0, 0, 0, 0
    for i in range(len(ings)):
        cap += ings[i].cap * amts[i]
        dur += ings[i].dur * amts[i]
        flav += ings[i].flav * amts[i]
        txr += ings[i].txr * amts[i]
        cal += ings[i].cal * amts[i]

    return max(cap, 0) * max(dur, 0) * max(flav, 0) * max(txr, 0), cal

# Read ingredients
ings = [ ]
for name, attrs in (line.split(': ') for line in open(fn, 'r')):
    cap, dur, flav, txr, cal = map(int, re.findall('[-0-9]+', attrs))
    ings.append(Data(name=name, cap=cap, dur=dur, flav=flav, txr=txr, cal=cal))

# For each ingredient combination, calculate score
best_part1, best_part2 = 0, 0
for amts in gen_amts(ings):
    score, cal = calc_score(ings, amts)
    best_part1 = max(best_part1, score)
    if cal == 500:
        best_part2 = max(best_part2, score)

print(f"Part 1: {best_part1}")
print(f"Part 2: {best_part2}")
