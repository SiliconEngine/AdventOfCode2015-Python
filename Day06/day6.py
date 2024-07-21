#!/usr/bin/python
"""Advent of Code 2015, Day 6, Part 1 and Part 2

https://adventofcode.com/2015/day/6

We have a grid of Christmas lights 1000x1000. The input is a list of
light commands to execute. Part 1 calculates the total number of lights
on at the end. Part 2 changes the commands to increase or decrease the
brightness, and we calculate the total brightness.

See 6.dat for full data.

Author: Tim Behrendsen
"""

import re
fn = '6.dat'

def part1(cmds):
    grid = [ [False] * 1000 for y in range(1000) ]
    for cmd in cmds:
        p = list(map(int, re.findall(r'\d+', cmd)))
        if cmd.startswith('to'):    # toggle
            for y in range(p[1], p[3]+1):
                for x in range(p[0], p[2]+1):
                    grid[y][x] = not grid[y][x]
        else:
            n = True if cmd.startswith('turn on') else False
            for y in range(p[1], p[3]+1):
                grid[y][p[0]:p[2]+1] = [n] * (p[2]-p[0]+1)

    return sum(grid[y][x] for y in range(1000) for x in range(1000))

def part2(cmds):
    grid = [ [0] * 1000 for y in range(1000) ]
    for cmd in cmds:
        p = list(map(int, re.findall(r'\d+', cmd)))
        n = 2 if cmd[:2] == 'to' else 1 if cmd[:7] == 'turn on' else -1
        for y in range(p[1], p[3]+1):
            for x in range(p[0], p[2]+1):
                grid[y][x] = max(0, grid[y][x]+n)

    return sum(grid[y][x] for y in range(1000) for x in range(1000))

cmds = [ line.strip() for line in open(fn, 'r') ]
print(f"Part 1 is {part1(cmds)}")
print(f"Part 2 is {part2(cmds)}")
