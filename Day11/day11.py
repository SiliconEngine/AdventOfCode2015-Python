#!/usr/bin/python
"""Advent of Code 2015, Day 11, Part 1 and Part 2

https://adventofcode.com/2015/day/11

Implements a "new password" algorithm, which it takes the old password and
increments by one letter value (azx -> azy -> azz -> baa -> etc). Then new
password must meet certain rules:

1) Must contain a straight incrementing sequence like ('abc')

2) Cannot contain letters 'i', 'o' or 'l'

3) Must have two non-overlapping pairs of the same letter.

Part 1 gets the next in the sequence, and Part 2 gets the one after that.

Author: Tim Behrendsen
"""

pwd = 'hxbxwxba'

def get_next(pwd):
    pwd_n = [ ord(c) for c in pwd ]         # Convert to list of ASCII values
    while True:
        # Increment the password
        for i in range(len(pwd_n)-1, -1, -1):
            pwd_n[i] += 1
            if pwd_n[i] <= ord('z'):
                break
            pwd_n[i] = ord('a')

        # Check for a straight sequence of at least 3 ('abc')
        if not any(pwd_n[i] == pwd_n[i+1]-1 == pwd_n[i+2]-2 for i in range(len(pwd_n)-2)):
            continue

        # Check if contains 'i', 'o' or 'l'
        if any(c in (ord('i'), ord('o'), ord('l')) for c in pwd_n):
            continue

        # Check for at least two non-overlapping pairs
        pairs, i = 0, 0
        while i < len(pwd_n)-1:
            if pwd_n[i] == pwd_n[i+1]:
                pairs += 1
                i += 1                      # Prevent overlap
            i += 1
        if pairs >= 2:
            break

    return ''.join(chr(c) for c in pwd_n)

pwd1 = get_next(pwd)
print(f"Part 1 is {pwd1}")
print(f"Part 2 is {get_next(pwd1)}")
