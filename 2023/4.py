#!/usr/bin/env python3
from collections import defaultdict
import re
from operator import mul

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

data = open("4.txt", "r").read()
lines = data.splitlines(True)
#lines = test_data.splitlines(True)

num_cards = 0
sumpts = 0
dupes = defaultdict(int)
for idx, line in enumerate(lines):
    [name, data] = line.split(": ")
    [winners, ours] = data.strip().replace(
        "  ",
        " ",
    ).split(" | ")
    print([winners, ours])
    winners = set((int(w) for w in winners.split(" ")))
    ours = set((int(o) for o in ours.split(" ")))
    num_winners = len([o for o in ours if o in winners])
    if num_winners:
        sumpts += 2**(num_winners - 1)
    for n in range(idx + 1, idx + 1 + num_winners):
        print(f"dupe {n+1}")
        dupes[n] += dupes[idx] + 1
    num_cards += dupes[idx] + 1

print(sumpts)
print(num_cards)
