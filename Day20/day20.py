#!/usr/bin/python
"""Advent of Code 2015, Day 20, Part 1 and Part 2

https://adventofcode.com/2015/day/20

Elves delivers a number of presents to houses equal to 10 times their "elf numbers", if
the house number is divisible by the elf number. In part 1, we want to know the lowest
house number that exceeds the target number of presents. In part 2, an elf delivers a
factor of 11 presents, but only for the first 50 houses.

My first approach of calculating each house amount was too slow and it was much faster
to just keep a big array. I empirically figured out what range was needed.

Author: Tim Behrendsen
"""

target = 29000000

def part1():
    a = [0] * 700001
    for elf in range(1, 700001):
        for i in range(elf, 700001, elf):
            a[i] += elf * 10
            if a[i] >= target:
                return i

def part2():
    a = [0] * 800001
    for elf in range(1, 800001):
        count = 0
        for i in range(elf, 800001, elf):
            a[i] += elf * 11
            if a[i] >= target:
                return i
            if (count := count+1) == 50:
                break

print(f"Part 1 is {part1()}")
print(f"Part 2 is {part2()}")
