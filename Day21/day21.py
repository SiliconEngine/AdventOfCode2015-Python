#!/usr/bin/python
"""Advent of Code 2015, Day 21, Part 1 and Part 2

https://adventofcode.com/2015/day/21

We're given some rules for an RPG game, along with costs for different
resources. Part 1 calculates the least amount of gold we have to spend to
win the game. Part 2 calculates most gold we could spend and still lose.

See 21.dat for full data.

Author: Tim Behrendsen
"""

import re
fn = '21.dat'

weapons_list = [
    { 'name': 'dagger', 'cost': 8, 'damage': 4, 'armor': 0 },
    { 'name': 'shortsword', 'cost': 10, 'damage': 5, 'armor': 0 },
    { 'name': 'warhammer', 'cost': 25, 'damage': 6, 'armor': 0 },
    { 'name': 'longsword', 'cost': 40, 'damage': 7, 'armor': 0 },
    { 'name': 'greataxe', 'cost': 74, 'damage': 8, 'armor': 0 },
]

armor_list = [
    { 'name': 'leather', 'cost': 13, 'damage': 0, 'armor': 1 },
    { 'name': 'chainmail', 'cost': 31, 'damage': 0, 'armor': 2 },
    { 'name': 'splintmail', 'cost': 53, 'damage': 0, 'armor': 3 },
    { 'name': 'bandedmail', 'cost': 75, 'damage': 0, 'armor': 4 },
    { 'name': 'platemail', 'cost': 102, 'damage': 0, 'armor': 5 },
]

ring_list = [
    { 'name': 'damage1', 'cost': 25, 'damage': 1, 'armor': 0 },
    { 'name': 'damage2', 'cost': 50, 'damage': 2, 'armor': 0 },
    { 'name': 'damage3', 'cost': 100, 'damage': 3, 'armor': 0 },
    { 'name': 'defense1', 'cost': 20, 'damage': 0, 'armor': 1 },
    { 'name': 'defense2', 'cost': 40, 'damage': 0, 'armor': 2 },
    { 'name': 'defense3', 'cost': 80, 'damage': 0, 'armor': 3 },
]

null_item = { 'name': 'null', 'cost': 0, 'damage': 0, 'armor': 0 }

# Play the game and return who wins
def play(boss, player):
    players = [ player.copy(), boss.copy() ]
    while True:
        for i in range(2):
            p, other = players[i], players[1-i]
            other['hp'] -= max(1, p['damage'] - other['armor'])
            if other['hp'] <= 0:
                return 'player' if i == 0 else 'boss'

# Generate combinations of valid weapons, armor and rings
def gen_combos():
    for w in weapons_list:
        for a_idx in range(-1, len(armor_list)):
            a = null_item if a_idx < 0 else armor_list[a_idx]
            yield (w, a, null_item, null_item)
            for r1_idx in range(len(ring_list)):
                r1 = ring_list[r1_idx]
                yield (w, a, r1, null_item)
                for r2_idx in range(r1_idx+1, len(ring_list)):
                    yield (w, a, r1, ring_list[r2_idx])

# Read in boss data
hp, damage, armor = map(int, (re.findall('\d+', line)[0] for line in open(fn, 'r')))
boss = { 'hp': hp, 'damage': damage, 'armor': armor }

# Play games with various combinations
least, most = 999, 0
for combo in gen_combos():
    cost = sum(c['cost'] for c in combo)
    armor = sum(c['armor'] for c in combo)
    damage = sum(c['damage'] for c in combo)
    if play(boss, {'damage': damage, 'armor': armor, 'hp': 100}) == 'player':
        least = min(least, cost)
    else:
        most = max(most, cost)

print(f"Part 1 is {least}")
print(f"Part 2 is {most}")
