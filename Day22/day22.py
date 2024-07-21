#!/usr/bin/python
"""Advent of Code 2015, Day 22, Part 1 and Part 2

https://adventofcode.com/2015/day/22

We're given some rules for a magic-based RPG game, along with costs for different
resources. Part 1 calculates the least amount of mana we have to spend to win the
game. Part 2 calculates least mana, with an additional rule.

It uses a depth-first-search, with pruning to eliminate branches that go beyond
the best search found.

See 22.dat for full data.

Author: Tim Behrendsen
"""

import re
from copy import deepcopy
fn = '22.dat'

# Spells, with different effects.
spell_list = [
    { 'name': 'missile', 'cost': 53, 'damage': 4, 'armor': 0, 'heal': 0, 'mana': 0, 'time': 1 },
    { 'name': 'drain', 'cost': 73, 'damage': 2, 'armor': 0, 'heal': 2, 'mana': 0, 'time': 1 },
    { 'name': 'shield', 'cost': 113, 'damage': 0, 'armor': 7, 'heal': 0, 'mana': 0, 'time': 6 },
    { 'name': 'poison', 'cost': 173, 'damage': 3, 'armor': 0, 'heal': 0, 'mana': 0, 'time': 6 },
    { 'name': 'recharge', 'cost': 229, 'damage': 0, 'armor': 0, 'heal': 0, 'mana': 101, 'time': 5 },
]

# Play the game and return mana used to win.
def play(start_boss, hard_mode=False):
    # Process active effects, and return current armor value.
    def do_effects(player, boss):
        # Check for spells in progress
        active = player['active']
        cur_armor = 0
        for idx, spell in enumerate(spell_list):
            if active[idx]:
                boss['hp'] -= spell['damage']
                player['hp'] += spell['heal']
                player['mana'] += spell['mana']
                cur_armor += spell['armor']
                active[idx] -= 1

        return cur_armor

    start_player = { 'hp': 50, 'mana': 500, 'total': 0, 'active': [ 0, 0, 0, 0, 0 ] }
    q = [ ('player', start_boss.copy(), deepcopy(start_player)) ]
    best = 9999999

    while q:
        turn, boss, player = q.pop()
        if player['total'] > best:
            continue                # Already worse than best, prune this branch

        if turn == 'player':
            if hard_mode:           # Part 2 "hard difficulty"
                player['hp'] -= 1
                if player['hp'] <= 0:
                    continue

            # Process spell effects
            do_effects(player, boss)

            # See if boss is dead
            if boss['hp'] <= 0:
                best = min(player['total'], best)
                continue

            # Add combinations of next spell to cast to queue
            active = player['active']
            cur_q_len = len(q)
            for idx, spell in enumerate(spell_list):
                if active[idx] == 0 and player['mana'] >= spell['cost']:
                    p = deepcopy(player)
                    p['mana'] -= spell['cost']
                    p['total'] += spell['cost']
                    p['active'][idx] = spell['time']
                    q.append(('boss', boss.copy(), p))

            if len(q) == cur_q_len:
                continue                # No spell cast, player loses

        else:           # Boss's turn
            # Process spell effects
            cur_armor = do_effects(player, boss)

            # See if boss is dead
            if boss['hp'] <= 0:
                best = min(player['total'], best)
                continue

            # Deal damage to player
            player['hp'] -= max(1, boss['damage'] - cur_armor)
            if player['hp'] <= 0:
                continue

            # Queue next turn
            q.append(('player', boss.copy(), deepcopy(player)))

    return best

hp, damage = map(int, (re.findall('\d+', line)[0] for line in open(fn, 'r')))
boss = { 'hp': hp, 'damage': damage }

print(f"Part 1 is {play(boss, hard_mode=False)}")
print(f"Part 2 is {play(boss, hard_mode=True)}")
