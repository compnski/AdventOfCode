#!/usr/bin/env python3
import numpy as np

data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
data = open("11.txt").read().strip()
rows = np.array([[*s] for s in data.split("\n")])
print(rows.shape)

event_rows = []
event_cols = []
for idx in range(rows.shape[0] - 1, -1, -1):
    has_galaxy = np.sum(rows[idx] == "#") > 0
    if not has_galaxy:
        event_rows.append(idx)
        rows = np.insert(rows, idx + 1, ["."] * rows.shape[1], axis=0)
        print("insert!", rows.shape[1], ["."] * rows.shape[1])

for idx in range(rows.shape[1] - 1, -1, -1):
    has_galaxy = np.sum(rows[:, idx] == "#") > 0
    if not has_galaxy:
        event_cols.append(idx)
        rows = np.insert(rows, idx + 1, ["."] * rows.shape[0], axis=1)
        print("insert!", rows.shape[0], ["."] * rows.shape[0])

print(rows.shape)
print(np.array2string(rows, separator="", formatter={"all": lambda x: x}))


def manhattan(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)


sum_dist = 0
galaxies = [*zip(*np.where(rows == "#"))]
for idx, galaxy in enumerate(galaxies):
    for other_galaxy in galaxies[idx + 1:]:
        dist = manhattan(galaxy, other_galaxy)
        print(galaxy, other_galaxy, dist)
        sum_dist += dist

print(f"sum_dist = {sum_dist}")
