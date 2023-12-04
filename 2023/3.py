#!/usr/bin/env python3
import re
from operator import mul

test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

#lines = data.splitlines(True)
#lines = test_data.splitlines(True)
#line = lines[0]

data = test_data
data = open("3.txt", "r").read()

num_cols = len(data.split("\n")[0]) + 1
print("width: ", num_cols)


def posToXY(pos):
    y = int(pos / num_cols)
    x = pos % num_cols
    return x, y


parts = [*re.finditer("([^0-9.\n]+)", data)]
print(*[p.span() for p in parts])
partByPos = {}
for part in parts:
    x, y = posToXY(part.span()[0])
    partByPos[f"{x},{y}"] = part.group()


def nextToPart(x, y):
    for xoff in range(-1, 2):
        for yoff in range(-1, 2):
            key = f"{x+xoff},{y+yoff}"
            maybePart = partByPos.get(key, None)
            if maybePart:
                return key, maybePart
    return [None, None]


maybeGears = {}
partsum = 0
print(partByPos)
matches = [*re.finditer("([0-9]+)", data)]
for match in matches:
    found = False
    [start, end] = match.span()
    partNum = int(match.group())
    x_start, y = posToXY(start)
    x_end = x_start + end - start
    for x in range(x_start, x_end):
        [partKey, maybePart] = nextToPart(x, y)
        if maybePart:
            print("Found part", partKey, maybePart, partNum)
            if maybePart == "*":
                if not partKey in maybeGears:
                    maybeGears[partKey] = []
                maybeGears[partKey].append(partNum)
            partsum += partNum
            found = True
            break
    if found:
        continue
print(f"sum = {partsum}")

print(
    sum(
        mul(*maybeGear) for maybeGear in maybeGears.values()
        if len(maybeGear) == 2))

#print(match.group(), "y", y, "x", [*range(x_start, x_end)])
