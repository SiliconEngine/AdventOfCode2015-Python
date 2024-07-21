#!/usr/bin/python
"""Advent of Code 2015, Day 3, Part 1 and Part 2

https://adventofcode.com/2015/day/3

We're given a list of N/S/E/W moves for Santa. In Part 1, we figure out how many
unique houses are visited. In Part 2, we have an additional robo-Santa and they trade
off directions.

See 3.dat for full data.

Author: Tim Behrendsen
"""

fn = '3.dat'

def run(moves, num_santas):
    seen, x, y = set([(0, 0)]), [0] * num_santas, [0] * num_santas
    for idx in range(0, len(moves), num_santas):
        for santa in range(num_santas):
            dx, dy = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[moves[idx+santa]]
            x[santa] += dx
            y[santa] += dy
            seen.add((x[santa], y[santa]))

    return len(seen)

moves = open(fn, 'r').readline().strip()
print(f"Part 1 is {run(moves, 1)}")
print(f"Part 2 is {run(moves, 2)}")

