#!/usr/bin/env python3
from typing import *
import numpy as np

data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

data = open("13.txt").read()

patterns = data.strip().replace("#", "1").replace(".", "0").split("\n\n")


def find_mirror(pattern):
    print()
    lines = pattern.split("\n")
    rsum = 0
    counts = 0
    col_nums = [
        int("".join(row), base=2)
        for row in np.array([[*s] for s in lines]).transpose()
    ]

    if (r := find_reflection(col_nums)) is not None:
        rsum += r
        counts += 1

    row_nums = [int(line, base=2) for line in lines]
    if (r := find_reflection(row_nums)) is not None:
        rsum += r * 100
        counts += 1
    if counts > 1:
        print()
        print(pattern)
        print(row_nums)
        print(col_nums)
        raise Exception("double reflection")
    if rsum:
        return rsum


def find_reflection(nums):
    doubles = [[idx + 0.5, x] for idx, x in enumerate(nums)
               if idx < len(nums) - 1 and x == nums[idx + 1]]
    print(doubles)
    for double_idx, _ in doubles:
        fail = False
        print(nums)
        print("double_idx", double_idx, 'nums', len(nums))
        distance_before = double_idx - 0.5
        distance_after = len(nums) - (double_idx + 0.5) - 1
        overlap = min(distance_before, distance_after)

        old_lower_bound = int(
            max(0, ((double_idx - 0.5) - (len(nums) - (double_idx + 1.5)))))

        old_upper_bound = int(
            min(
                len(nums) - 1,
                (len(nums) - (double_idx + 0.5)) + double_idx + 0.5))

        print("old", [old_lower_bound, old_upper_bound])
        lower_bound, upper_bound = int(double_idx - overlap -
                                       0.5), int(double_idx + overlap + 0.5)

        print([lower_bound, upper_bound, int(upper_bound / 2)])
        print(overlap,
              [double_idx - overlap - 0.5, double_idx + overlap + 0.5])

        for n in range(lower_bound, lower_bound + int(overlap)):
            if nums[n] != nums[upper_bound - (n - lower_bound)]:
                fail = True
                print("FAIL", n)
                break
        print("zz", int(double_idx + 0.5))
        if not fail:
            print("RET")
            return int(double_idx + 0.5)

    return None


p = [find_mirror(pattern) for pattern in patterns]
print(p)
print(sum(n for n in p if n is not None))

# Part 2, check if anyone is a power of 2 away from making a new match?
