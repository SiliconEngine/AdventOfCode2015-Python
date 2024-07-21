#!/usr/bin/python
"""Advent of Code 2015, Day 19, Part 1 and Part 2

https://adventofcode.com/2015/day/19

We're given a list of string translations and a long string. For Part 1, the goals is
to figure out the number of unique strings constructed from applying a translation
one at a time, possibly in different parts of the string.

For Part 2, we have to start with string 'e' and figure out the least number of
translations to reach the final string. For this part, it the general case of doing
a BFS search is impractically slow, but the puzzle is constructed such that the
solution can be found by taking the string and applying transformations backwards
until we get the 'e' and counting. There's only one actual solution. It's still
impractically slow to do the general case, but it turns out that randomly shuffling
the order of the transformations and then applying what you can will get to the
solution. The data was constructed to make this approach workable, but won't work in
the general case.

See 19.dat for full data.

Author: Tim Behrendsen
"""

from random import shuffle

fn = '19.dat'

repl_list = []
with open(fn, 'r') as file:
    for line in file:
        line = line.strip()
        if line == '':
            break
        repl_list.append(line.split(' => '))

    med = next(file).strip()

def part1():
    uniq = set()
    for f, t in repl_list:
        i = 0
        while True:
            i = med.find(f, i)
            if i < 0:
                break
            uniq.add(med[:i] + t + med[i+len(f):])
            i += 1

    return len(uniq)

def part2():
    while True:
        # Put transformation in random order
        shuffle(repl_list)

        # Keep applying until either get the "e" or no more transforms
        # can be done. On average, things are solved in around 10 tries.
        work, count, dead_end = med, 0, False
        while work != 'e' and not dead_end:
            dead_end = True
            for r in repl_list:
                if r[1] in work:
                    count += work.count(r[1])
                    work = work.replace(r[1], r[0])
                    dead_end = False

        if work == 'e':
            return count

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
