#!/usr/bin/env python3
from dataclasses import dataclass
from typing import *
import re
import tqdm

# #.#.### 1,1,3
# .#...#....###. 1,1,3
# .#.###.#.###### 1,3,1,6
# ####.#...#... 4,1,1
# #....######..#####. 1,6,5
# .###.##....# 3,2,1

data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

data = open("12.txt").read()

operational = "."
damaged = "#"
unknown = "?"


def replace_first_unknown(springs: str, replace_with: str) -> str:
    return springs.replace("?", replace_with, 1)


patterns = {}


def get_pattern(checksums):
    key = ",".join(str(c) for c in checksums)
    if key in patterns:
        return patterns[key]

    pattern = "^[.?]*?" + "[.?]+?".join([f"([#?]{{{n}}})"
                                         for n in checksums]) + "[.?]*?$"
    p = re.compile(pattern)
    patterns[key] = p
    return p


def solve_all_arrangements(springs, checksums):
    p = get_pattern(checksums)
    print(springs, checksums, p)
    return solve_recurse(springs, p, checksums, sum(checksums), 0,
                         springs.count(damaged), springs.count(unknown))
    # print("\n".join(n.id + " " + ",".join(str(n) for n in checksums)
    #                 for n in nodes.values() if n.id.count(unknown) == 0))
    #return len([n for n in nodes if n.count(unknown) == 0])

    # Create nodes, as pattern is locked in, strip leading chars?


def solve_recurse(springs, pattern, checksums, sum_checksums, leaf_count,
                  broken_count, unknown_count):
    if broken_count + unknown_count < sum_checksums:
        return leaf_count
    m = pattern.match(springs)
    if not m:
        return leaf_count

    try:
        first_unknown = springs.index(unknown)
    except:
        return leaf_count + 1

    remove_count = 0
    remove_from = 0
    if m.lastindex is not None:
        for idx in range(1, m.lastindex + 1):
            if m.end(idx) < first_unknown and m.group(idx).count(unknown) == 0:
                remove_count = idx
                remove_from = max(m.end(idx), springs.index(operational))
            else:
                break
    if remove_count > 0:
        #print(remove_count, remove_from)
        checksums = checksums[remove_count:]
        sum_checksums = sum(checksums)
        springs = springs[remove_from:]
        #print(">>   ", springs, checksums)
        pattern = get_pattern(checksums)

    left = replace_first_unknown(springs, operational)
    right = replace_first_unknown(springs, damaged)
    return solve_recurse(left, pattern, checksums, sum_checksums, leaf_count,
                         broken_count, unknown_count - 1) + solve_recurse(
                             right, pattern, checksums, sum_checksums,
                             leaf_count, broken_count + 1, unknown_count - 1)


from multiprocessing import Pool

sum_num_arrangements = 0

lines = data.strip().split("\n")


def solve(line: str):
    [springs, _checksums] = line.split(" ")
    springs, _checksums = unknown.join([springs] * 5), ",".join([_checksums] *
                                                                5)
    checksums = [int(s) for s in _checksums.split(",")]

    num_arrangements = solve_all_arrangements(springs, checksums)
    print(f"num_arrangements = {num_arrangements}")
    return num_arrangements


with Pool() as pool:

    result = list(
        tqdm.tqdm(pool.imap_unordered(solve, lines), total=len(lines)))
print(result)
print(f"sum_num_arrangements = {sum(result)}")
