#!/usr/bin/python
"""Advent of Code 2015, Day 2, Part 1 and Part 2

https://adventofcode.com/2015/day/2

In part 1, need to calculate the amount wrapping paper needed for a list of box
dimensions, which is the total surface area + the smallest side for extra. In
part 2, we calculate the amount of ribbon needed, which is the smallest perimeter
of the box, plus an amount equal to the volume. The smallest perimeter is 2x the
two smallest sides.

See 2.dat for full data.

Author: Tim Behrendsen
"""

fn = '2.dat'

boxes = [ sorted(map(int, line.strip().split('x'))) for line in open(fn, 'r') ]

paper, ribbon = 0, 0
for b in boxes:
    sides = (b[0] * b[1], b[1] * b[2], b[0] * b[2])
    paper += sum(sides) * 2 + min(sides)
    ribbon += (b[0] + b[1]) * 2 + b[0] * b[1] * b[2]

print(f"Part 1 is {paper}")
print(f"Part 2 is {ribbon}")
