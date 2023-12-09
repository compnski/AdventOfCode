#!/usr/bin/env python3

from dataclasses import dataclass
from typing import *
import re

data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

data = open("9.txt").read().strip()
lines = data.split("\n")


def predict_next(steps: List[int]):
    all_diffs: List[List[int]] = [steps]
    cur = steps
    while True:
        diffs = [b - a for a, b in zip(cur, cur[1:])]
        if diffs.count(0) == len(diffs):
            # all zero, done!
            break
        cur = diffs
        all_diffs.append(diffs)
    print(all_diffs)
    last = 0
    first = 0
    for idx in range(len(all_diffs) - 1, -1, -1):
        all_diffs[idx][-1] += last
        last = all_diffs[idx][-1]
        all_diffs[idx][0] -= first
        first = all_diffs[idx][0]

    return [first, last]


sum_last = 0
sum_first = 0
for line in lines:
    steps = [int(s) for s in line.split(" ")]
    [first_val, last_val] = predict_next(steps)
    sum_last += last_val
    sum_first += first_val
    print(first_val, last_val)

print("sum_last", sum_last)

print("sum_first", sum_first)
