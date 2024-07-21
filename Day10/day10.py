#!/usr/bin/python
"""Advent of Code 2015, Day 10, Part 1 and Part 2

https://adventofcode.com/2015/day/10

Implement the "look and say" algorithm, where a sequence of digits is scanned.
The next sequence is formed by taking each run of the same digit and replacing
it with number of digits, followed by the digit itself.

Part 1 does 40 generations, and part 2 does 50 generations.

Author: Tim Behrendsen
"""

start = '1113122113'

def run():
    s = list(start)
    for i in range(50):
        if i == 40:
            part1 = len(s)
        new_s, it = [], iter(s)
        last_c, count = next(it), 1
        for c in it:
            if c == last_c:
                count += 1
            else:
                new_s += list(str(count)) + [last_c]
                last_c, count = c, 1

        # Will always have a leftover count
        s = new_s + list(str(count)) + [last_c]

    return part1, len(s)

print(f"Part 1, 2: {run()}")
