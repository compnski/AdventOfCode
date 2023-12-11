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

offset_x = []
offset_y = []
row_offset = 0
col_offset = 0
OFFSET_AMOUNT = 999999

for idx in range(0, rows.shape[0]):
    has_galaxy = np.sum(rows[idx] == "#") > 0
    if not has_galaxy:
        row_offset += OFFSET_AMOUNT
    offset_x.append(idx + row_offset)

for idx in range(0, rows.shape[1]):
    has_galaxy = np.sum(rows[:, idx] == "#") > 0
    if not has_galaxy:
        col_offset += OFFSET_AMOUNT
    offset_y.append(idx + col_offset)
print(row_offset, col_offset)

print(offset_x, offset_y)

#[(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]


def fix_space_time(x, y):
    return (offset_x[x], offset_y[y])


galaxies = [fix_space_time(x, y) for x, y in zip(*np.where(rows == "#"))]
print(galaxies)
#print(rows.shape)
#print(np.array2string(rows, separator="", formatter={"all": lambda x: x}))


def manhattan(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)


sum_dist = 0

for idx, galaxy in enumerate(galaxies):
    for other_galaxy in galaxies[idx + 1:]:
        dist = manhattan(galaxy, other_galaxy)
        #print(galaxy, other_galaxy, dist)
        sum_dist += dist

print(f"sum_dist = {sum_dist}")
