#!/usr/bin/env python3
from dataclasses import dataclass
from typing import *
import re

data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

data = open("8.txt", "r").read().strip()


@dataclass
class Node:
    id: str
    right: str
    left: str

    @property
    def L(self):
        return nodes.get(self.left)

    @property
    def R(self):
        return nodes.get(self.right)


nodes: Dict[str, Node] = {}

[moves, graph] = data.split("\n\n")

for entry in graph.split("\n"):
    [id, left, right] = re.sub("[^\w ]", "", entry).split()
    nodes[id] = Node(id=id, left=left, right=right)

print(nodes)

loop_freqs = {}


def path_gen(pathidx, start):
    cur = nodes[start]
    move_count = 0
    last_loop = 0
    while True:  #cur.id != "ZZZ":
        if cur.id.endswith("Z"):
            print(pathidx, start, " ", cur.id, "   ", move_count,
                  move_count - last_loop)
            loop_freqs[pathidx] = move_count - last_loop
            last_loop = move_count
        move = moves[move_count % len(moves)]
        move_count += 1
        cur = getattr(cur, move)
        yield cur.id


start_paths = [id for id in nodes.keys() if id.endswith("A")]
print("Path count", len(start_paths))
gens = [path_gen(idx, start) for idx, start in enumerate(start_paths)]

move_count = 0
while True:
    move_count += 1
    if len([id for id in (next(g) for g in gens)
            if not id.endswith("Z")]) == 0:
        break
    if len(loop_freqs) == len(start_paths):
        break

print(move_count)
print(loop_freqs)
import math

print(math.lcm(*loop_freqs.values()))
