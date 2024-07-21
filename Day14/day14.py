#!/usr/bin/python
"""Advent of Code 2015, Day 14, Part 1 and Part 2

https://adventofcode.com/2015/day/14

We're given a list of reindeer, along with their speeds and rest times.
Part 1 calculates the reindeer that goes the furthest in a time interval.
Part 2 assigns 1 point in each second to the reindeer(s) that are ahead
at that second, and calculates the most points.

See 14.dat for full data.

Author: Tim Behrendsen
"""

import re
from types import SimpleNamespace as Data

fn = '14.dat'
total_time = 2503

def run(reindeer):
    work = []
    for r in reindeer.values():
        work.append(Data(state='fly', time_left=r.fly_t, dist=0, pts=0, r=r))

    time_left = total_time
    while time_left > 0:
        # Part 1 can be done with more efficent method of next state change
        #t = min(w.time_left for w in work)
        #t = min(time_left, t)

        # If part 2, need to do by 1 step, but also works for part 1
        t = 1
        time_left -= t

        for w in work:
            w.time_left -= t
            if w.state == 'fly':
                w.dist += t * w.r.fly_v
            if w.time_left == 0:
                w.state = 'rest' if w.state == 'fly' else 'fly'
                w.time_left = w.r.rest_t if w.state == 'rest' else w.r.fly_t

        # Part 2 point calculation
        lead_dist = max(w.dist for w in work)
        for w in work:
            if w.dist == lead_dist:
                w.pts += 1

    return max(w.dist for w in work), max(w.pts for w in work)

reindeer = {}
for line in open(fn, 'r'):
    name, fly_v, fly_t, rest_t = re.findall('(\w+).*?(\d+).*?(\d+).*?(\d+)', line)[0]
    reindeer[name] = Data(fly_v=int(fly_v), fly_t=int(fly_t),  rest_t=int(rest_t))

part1, part2 = run(reindeer)
print(f"Part 1 is {part1}")
print(f"Part 2 is {part2}")
