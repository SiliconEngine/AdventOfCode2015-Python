#!/usr/bin/python
"""Advent of Code 2015, Day 7, Part 1 and Part 2

https://adventofcode.com/2015/day/7

We're given a list of "wires" that perform logical operations with each other. When one
wire is assigned a value, we need to propagate the change to the other affected wires.
Part 1 displays the value in wire 'a' after calculation. Part 2 feeds that value back
into the assignment for 'b' and runs it again.

This problem is similar to a spreadsheet recalculation algorithm, where you have a lot
of dependent formulas.

See 7.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'test.dat'
fn = '7.dat'

# Execute a command, and return destination wire
def do_cmd(wires, cmd):
    get = lambda arg: int(arg) if arg.isnumeric() else wires[arg]

    if cmd[1] == '->':       wires[cmd[-1]] = get(cmd[0])
    elif cmd[1] == 'AND':    wires[cmd[-1]] = get(cmd[0]) & get(cmd[2])
    elif cmd[1] == 'OR':     wires[cmd[-1]] = get(cmd[0]) | get(cmd[2])
    elif cmd[1] == 'LSHIFT': wires[cmd[-1]] = get(cmd[0]) << get(cmd[2])
    elif cmd[1] == 'RSHIFT': wires[cmd[-1]] = get(cmd[0]) >> get(cmd[2])
    elif cmd[0] == 'NOT':    wires[cmd[-1]] = (~ get(cmd[1])) & 0xffff
    return cmd[-1]

# Do assignments, propagating to wires affected and needing recalculation
def run(assigns, links):
    wires = defaultdict(int)
    for a in assigns:
        wire, n = a[2], int(a[0])
        wires[wire] = n

        q = [ wire ]                # Queue of wires needing recalculation
        while q:
            wire = q.pop(0)
            for cmd in links[wire]:
                dest = do_cmd(wires, cmd)
                # If wire already there, remove it from the queue and put it to the back
                if dest in q:
                    q.remove(dest)
                q.append(dest)

    return wires['a']

# Read commands
cmds = [ list(line.strip().split()) for line in open(fn, 'r') ]

# Create two lists: 1) List of numeric assignments, and 2) links to what wires
# are affected when one is changed.
assigns = [ ]
links = defaultdict(list)
for cmd in cmds:
    if cmd[1] == '->':
        if cmd[0].isnumeric():
            assigns.append(cmd)
        else:
            links[cmd[0]].append(cmd)
    elif cmd[0] == 'NOT':
        links[cmd[1]].append(cmd)
    else:       # One of the other two-argument commands
        links[cmd[0]].append(cmd)
        links[cmd[2]].append(cmd)

part1 = run(assigns, links)
print(f"Part 1: {part1}")

assigns[0][0] = part1
print(f"Part 2: {run(assigns, links)}")
