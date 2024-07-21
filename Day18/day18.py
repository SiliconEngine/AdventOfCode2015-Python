#!/usr/bin/python
"""Advent of Code 2015, Day 18, Part 1 and Part 2

https://adventofcode.com/2015/day/18

Simulates Game of Life. Part 1 adds up the number of cells that are on after
100 generations. Part 2 does the same, except forces the corners to always be on.

See 18.dat for full data.

Author: Tim Behrendsen
"""

fn = '18.dat'
num_cycles = 100

grid = [ list(line.strip()) for line in open(fn, 'r') ]
num_x, num_y = len(grid[0]), len(grid)
stuck_list = []

get = lambda g, x, y: g[y][x] == '#' if 0 <= x < num_x and 0 <= y < num_y else False

def next_cell(g, x, y):
    c = g[y][x]
    count = get(g, x+1, y) + get(g, x-1, y) + get(g, x, y+1) + get(g, x+1, y+1) + \
        get(g, x-1, y+1) + get(g, x, y-1) + get(g, x+1, y-1) + get(g, x-1, y-1)
    if c == '#' and count in (2, 3):
        return '#'
    if c == '.' and count == 3:
        return '#'
    return '.'

def run(grid_start):
    grid = [ row.copy() for row in grid_start ]

    for i in range(num_cycles):
        for x, y in stuck_list:
            grid[y][x] = '#'
        grid = [ [ next_cell(grid, x, y) for x in range(num_x) ] for y in range(num_y) ]

    for x, y in stuck_list:
        grid[y][x] = '#'
    return sum(c == '#' for row in grid for c in row)

print(f"Part 1 is {run(grid)}")
stuck_list = ((0, 0), (0, num_y-1), (num_x-1, 0), (num_x-1, num_y-1))
print(f"Part 2 is {run(grid)}")
