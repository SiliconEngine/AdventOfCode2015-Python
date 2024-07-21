#!/usr/bin/python
"""Advent of Code 2015, Day 23, Part 1 and Part 2

https://adventofcode.com/2015/day/23

Simulates a simple CPU, which runs a given program and displays the result in
register 'b'. Part 2 changes the input of register 'a' to produce a different
value.

See 23.dat for full data.

Author: Tim Behrendsen
"""

fn = '23.dat'

class CPU:
    def __init__(self, program):
        self.program = program
        self.regs = { 'a': 0, 'b': 0 }

    def run(self):
        pc = 0
        while pc < len(self.program):
            op, parms = self.program[pc][0], self.program[pc][1:3]
            if op == 'hlf':
                self.regs[parms[0]] //= 2
            elif op == 'tpl':
                self.regs[parms[0]] *= 3
            elif op == 'inc':
                self.regs[parms[0]] += 1
            elif op == 'jmp':
                pc += int(parms[0])-1
            elif op == 'jie':
                if (self.regs[parms[0]] % 2) == 0:
                    pc += int(parms[1])-1
            elif op == 'jio':
                if self.regs[parms[0]] == 1:
                    pc += int(parms[1])-1
            pc += 1

prog = [ line.strip().replace(',', '').split(' ') for line in open(fn, 'r') ]
cpu = CPU(prog)
cpu.run()
print(f"Part 1 is {cpu.regs['b']}")

cpu = CPU(prog)
cpu.regs['a'] = 1
cpu.run()
print(f"Part 2 is {cpu.regs['b']}")
