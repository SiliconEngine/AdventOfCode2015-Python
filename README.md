# Advent of Code 2015 solutions written in Python.
## Author: Tim Behrendsen

Link: https://adventofcode.com/2015/

Advent of Code is a series of puzzles over 25 days, each with a part 1 and
part 2. The difficulty roughly rises each day, with the later puzzles often
requiring some tricky algorithms to solve.

For these solutions, the various days are in separate directories, with one 
program doing each part. Day 25, as traditional, is only a single part.

### Advent of Code 2015, Day 1, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/1

Input data is a list of parenthesis representing elevator moves, with '('
going up a floor, and ')' down a floor. Part 1 calculates the final floor.
Part 2 shows the index where it first goes into the basement.

### Advent of Code 2015, Day 2, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/2

In part 1, need to calculate the amount wrapping paper needed for a list of box
dimensions, which is the total surface area + the smallest side for extra. In
part 2, we calculate the amount of ribbon needed, which is the smallest perimeter
of the box, plus an amount equal to the volume. The smallest perimeter is 2x the
two smallest sides.

### Advent of Code 2015, Day 3, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/3

We're given a list of N/S/E/W moves for Santa. In Part 1, we figure out how many
unique houses are visited. In Part 2, we have an additional robo-Santa and they trade
off directions.

### Advent of Code 2015, Day 4, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/4

Scan a series of MD5 hashes. For Part 1, identify the index of the
hash that starts with five zeroes. For Part 2, it's six zeroes.

### Advent of Code 2015, Day 5, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/5

Santa has a list of strings that need to evaluated whether they're nice or not.
Part 1 gives us a list of rules, while Part 2 gives us a list of different rules.
Total up the number of nice strings in each part.

### Advent of Code 2015, Day 6, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/6

We have a grid of Christmas lights 1000x1000. The input is a list of
light commands to execute. Part 1 calculates the total number of lights
on at the end. Part 2 changes the commands to increase or decrease the
brightness, and we calculate the total brightness.

### Advent of Code 2015, Day 7, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/7

We're given a list of "wires" that perform logical operations with each other. When one
wire is assigned a value, we need to propagate the change to the other affected wires.
Part 1 displays the value in wire 'a' after calculation. Part 2 feeds that value back
into the assignment for 'b' and runs it again.

This problem is similar to a spreadsheet recalculation algorithm, where you have a lot
of dependent formulas.

### Advent of Code 2015, Day 8, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/8

We're given a list of strings with embedded escape sequences (\\, \", \x00). In Part 1,
calculate the difference between the raw length and the in-memory length after taking
into account the escapes. In Part 2, calculate the length of a new string with escapes
added, and display the difference from the raw length.

### Advent of Code 2015, Day 9, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/9

Classic TSP puzzle (Traveling Santa Problem). Need to find shortest (Part 1)
and longest (Part 2) routes among a set of cities. There are only eight cities,
so brute force is fast.

I also did a bitmap for the visited city list, which was overkill.

### Advent of Code 2015, Day 10, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/10

Implement the "look and say" algorithm, where a sequence of digits is scanned.
The next sequence is formed by taking each run of the same digit and replacing
it with number of digits, followed by the digit itself.

Part 1 does 40 generations, and part 2 does 50 generations.

### Advent of Code 2015, Day 11, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/11

Implements a "new password" algorithm, which it takes the old password and
increments by one letter value (azx -> azy -> azz -> baa -> etc). Then new
password must meet certain rules:

1) Must contain a straight incrementing sequence like ('abc')

2) Cannot contain letters 'i', 'o' or 'l'

3) Must have two non-overlapping pairs of the same letter.

Part 1 gets the next in the sequence, and Part 2 gets the one after that.

### Advent of Code 2015, Day 12, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/12

The input a JSON-formatted data structure. In part 1, we recursively scan the
structure and return a total of all integers. In part 2, we do the same
totaling but do not include any dictionary that contains the word 'red' as
a value.

### Advent of Code 2015, Day 13, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/13

We want to place people in a circular table. We're given "happiness scores" that
describe how happy someone is to sit next to each person. Part 1 finds the maximum
happiness score for a permutation. Part 2 adds another person ("self") to the list
and finds that solution.

Doesn't use the itertool permutation function. Instead uses uses a yield from a
recursive function that generates the permutation.

### Advent of Code 2015, Day 14, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/14

We're given a list of reindeer, along with their speeds and rest times.
Part 1 calculates the reindeer that goes the furthest in a time interval.
Part 2 assigns 1 point in each second to the reindeer(s) that are ahead
at that second, and calculates the most points.

### Advent of Code 2015, Day 15, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/15

We're given a list of cookie ingredients, along with various attributes. The
total amount of ingredients must total 100 and we want to optimize the attributes.
Part 1 optimizes the ingredients, without the calories. Part 2 optimizes the
ingredients and requires the total calories to be 500.

### Advent of Code 2015, Day 16, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/16

Given a gift that is scanned to produce a set of personal attributes, compare
those against a list of "Aunt Sue" attributes to determine the matching one. In part
2, the rules are modified slightly based on the attribute type.

### Advent of Code 2015, Day 17, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/17

Given a list of container sizes, part 1 calculates the number of combinations
that can hold exactly 150 liters in total. Part 2 calculates the minimum number
of containers needed, and how many combinations have that total.

### Advent of Code 2015, Day 18, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/18

Simulates Game of Life. Part 1 adds up the number of cells that are on after
100 generations. Part 2 does the same, except forces the corners to always be on.

### Advent of Code 2015, Day 19, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/19

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

### Advent of Code 2015, Day 20, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/20

Elves delivers a number of presents to houses equal to 10 times their "elf numbers", if
the house number is divisible by the elf number. In part 1, we want to know the lowest
house number that exceeds the target number of presents. In part 2, an elf delivers a
factor of 11 presents, but only for the first 50 houses.

My first approach of calculating each house amount was too slow and it was much faster
to just keep a big array. I empirically figured out what range was needed.

### Advent of Code 2015, Day 21, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/21

We're given some rules for an RPG game, along with costs for different
resources. Part 1 calculates the least amount of gold we have to spend to
win the game. Part 2 calculates most gold we could spend and still lose.

### Advent of Code 2015, Day 22, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/22

We're given some rules for a magic-based RPG game, along with costs for different
resources. Part 1 calculates the least amount of mana we have to spend to win the
game. Part 2 calculates least mana, with an additional rule.

It uses a depth-first-search, with pruning to eliminate branches that go beyond
the best search found.

### Advent of Code 2015, Day 23, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/23

Simulates a simple CPU, which runs a given program and displays the result in
register 'b'. Part 2 changes the input of register 'a' to produce a different
value.

### Advent of Code 2015, Day 24, Part 1 and Part 2

Link: https://adventofcode.com/2015/day/24

Santa needs to divide the weights of his presents equally, and also needs the
least number in one compartment for legroom. Calculate the least number of
presents that also will divide equally. For those sets, we want to pick the
set with the lowest product of the weights. Part 1 divides into a set of 3,
and part 2 divides into a set of 4.

### Advent of Code 2015, Day 25

Link: https://adventofcode.com/2015/day/25

Given a generated sequence of numbers that is filled onto a grid in a certain
pattern, figure out what number is generated at a set of grid coordinates.

