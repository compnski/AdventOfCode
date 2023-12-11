#!/usr/bin/env python3
from collections import defaultdict
from typing import *
import PIL.Image

# NOTE: First process the image by using a flood-fill from all edges.
# First do white on the edge, then black.
# Then fill in any on the edges that didn't flood properly.

# Then run this, it counts the white pixels

img = PIL.Image.open("tmp.png")
print(sum(img.point(lambda pix: 1 if pix > 250 else 0).getdata()))

# def pos(idx):
#     return idx % width, int(idx / width)

# def toidx(x, y):
#     return width * y + x

# img = PIL.Image.open("out.png")

# width = int(img.width / 3) - 1
# height = int(img.height / 3)
# print(f"Width = {width}, Height = {height}")

# import pickle

# distances: Dict[int, int] = defaultdict(int)

# with open("track.pkl", "rb") as f:
#     distances = pickle.load(f)
# print(len(distances))
# imgdata = img.getdata()

# inside = 0
# for idx in range(0, (height) * (width)):
#     x, y = pos(idx)
#     if idx in distances:
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#                 img.putpixel((x * 3 + dx, y * 3 + dy), 200)
#     elif img.getpixel((x * 3 - 1, y * 3 - 1)) == 0 or img.getpixel(
#         (x * 3 + 1, y * 3 + 1)) == 0:
#         print("inside", (x, y), pos(toidx(x * 3, y * 3)), toidx(x * 3, y * 3))
#         inside += 1
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#                 img.putpixel((x * 3 + dx, y * 3 + dy), 100)

# print(inside)
# #print([*])

# print(img.mode)
# img.save("newout.png")
