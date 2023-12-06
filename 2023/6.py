#!/usr/bin/env python3
from collections import defaultdict
import re
from operator import mul
from typing import *
from functools import reduce

test_data = [*zip([7, 15, 30], [9, 40, 200])]
test_data = [*zip([71530], [940200])]

data = [*zip([40, 81, 77, 72], [219, 1012, 1365, 1089])]
data = [*zip([40817772], [219101213651089])]

#data = test_data


def calc_distance(raceT, chargeT):
    return (raceT - chargeT) * chargeT


wins = defaultdict(int)
for race_idx, race in enumerate(data):
    [time, distance] = race
    prevd = 0
    for t in range(1, time):
        d = calc_distance(time, t)
        if d > distance:
            wins[race_idx] += 1
        # if d < prevd:
        #     print("going down", [d, prevd])
        #     break
        prevd = d

print(reduce(lambda acc, n: acc * n, wins.values()))
