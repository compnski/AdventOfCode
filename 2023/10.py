#!/usr/bin/env python3
from collections import defaultdict
from typing import *

data = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

# data = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""

data = open("10.txt", "r").read().strip()
# data = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L"""

# data = """.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ..."""

start_char = "F"

#start_char = "7"

height = data.count("\n")
width = len(data.strip().split("\n")[0])
data = data.replace("\n", "")
print(f"Width = {width}")
print(f"Height = {height}")


def at(x, y):
    return data[width * y + x]


def pos(idx):
    return idx % width, int(idx / width)


def toidx(x, y):
    return width * y + x


#X, Y
dirs = {
    "F": ((0, 1), (1, 0)),
    "-": ((-1, 0), (1, 0)),
    "7": ((-1, 0), (0, 1)),
    "|": ((0, 1), (0, -1)),
    "L": ((0, -1), (1, 0)),
    "J": ((-1, 0), (0, -1))
}

bigdots = {
    "F": (
        (0, 0, 0),  #
        (0, 2, 1),  #
        (0, 1, 0)),  #
    "-": (
        (0, 0, 0),  #
        (1, 2, 1),  #
        (0, 0, 0)),  #
    "7": (
        (0, 0, 0),  #
        (1, 2, 0),  #
        (0, 1, 0)),  #
    "|": (
        (0, 1, 0),  #
        (0, 2, 0),  #
        (0, 1, 0)),  #
    "L": (
        (0, 1, 0),  #
        (0, 2, 1),  #
        (0, 0, 0)),  #
    "J": (
        (0, 1, 0),  #
        (1, 2, 0),  #
        (0, 0, 0)),  #
    ".": (
        (0, 0, 0),  #
        (0, 2, 0),  #
        (0, 0, 0)),  #
}

distances: Dict[int, int] = defaultdict(int)


def get_next(idx, dirlist: Optional[Tuple[Tuple[int, int], Tuple[int, int]]]):
    x, y = pos(idx)
    if dirlist is None:
        raise Exception("woah:" + str(idx))
    return [toidx(x + dx, y + dy) for [dx, dy] in dirlist]


start = data.index("S")
print(start)
first, last = get_next(start, dirs.get(start_char))
distances[start] = 0
distances[last] = 1

print([first, pos(first), last, pos(last)])

cur = first

dist = 1
prev = start
while cur != last:
    distances[cur] = dist
    dist += 1
    nexts = [n for n in get_next(cur, dirs.get(data[cur])) if n != prev]
    print([cur, data[cur], pos(cur), nexts])
    if len(nexts) != 1:
        print(nexts)
        raise Exception("bad nexts")
    prev = cur
    cur = nexts[0]

print(dist)
print(int(dist / 2 + 1))
print("")

bigmap = [[" " for _ in range(0, width * 3 + 3)]
          for _ in range(0, height * 3 + 3)]

import PIL.Image

img = PIL.Image.new("L", (width * 3 + 3, height * 3 + 3))


def update_bigmap(idx, char):
    if char == "S":
        char = start_char
    is_pipe = idx in distances
    triples = bigdots[char]
    if char != ".":
        print(char, triples)
    x, y = pos(idx)
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            wall = triples[dy + 1][dx + 1]
            if is_pipe:
                wall = min(wall, 1)
            if char != ".":
                print(idx, (3 * x + dx, 3 * y + dy), wall)
            img.putpixel((3 * x + dx, 3 * y + dy), wall * 128)
            bigmap[3 * y +
                   dy][3 * x +
                       dx] = "*" if wall == 1 else "X" if wall == 2 else " "


for idx in range(0, len(data)):
    update_bigmap(idx, data[idx])
# if idx in distances:
#       update_bigmap(idx, data[idx])
#   else:
#       update_bigmap(idx, ".")
print("")
print("")
import pickle
with open("track.pkl", "wb") as f:
    pickle.dump(distances, f)

print("\n".join("".join(r) for r in bigmap))

img.save("tmp.png")

# Need to flood fill
# Pick tile not on loop
# expand borders unless you hit something you can't cross
# cannot cross the true pipes - and | (when hit straight on)
#

# 738, too high
