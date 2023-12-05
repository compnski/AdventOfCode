#!/usr/bin/env python3
from collections import defaultdict
import re
from operator import mul
from typing import *

test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

data = open("5.txt", "r").read()
sections = data.split("\n\n")
#lines = data.splitlines(True)
#sections = test_data.split("\n\n")

print(sections)
[_, seedsStr] = sections[0].split(": ")
seeds = [int(seed) for seed in seedsStr.split(" ")]
print("seeds", seeds)


def buildSectionMap(section, destFirst=False):
    [name, data] = section.split(":")
    print(name)
    mapping = []
    for line in data.splitlines(True):
        if not len(line.strip()):
            continue
        print(line)
        [dest, source, length] = line.split(" ")
        if destFirst:
            mapping.append([int(dest), int(source), int(length)])
        else:
            mapping.append([int(source), int(dest), int(length)])
    #     for idx, s in enumerate(range(int(source), int(source) + int(length))):
    #         mapping[s] = int(dest) + idx
    mapping.sort()
    return [name.replace(" map", ""), mapping]


maps = {
    k: v
    for [k, v] in
    [buildSectionMap(section.strip()) for section in sections[1:]]
}
print("maps", maps)


def lookup(num: int, mapname: str):
    for [source, dest, length] in maps.get(mapname):
        if num >= source and num < source + length:
            return dest + num - source
    return num


mapnames = [
    "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
    "water-to-light", "light-to-temperature", "temperature-to-humidity",
    "humidity-to-location"
]
rev_mapnames = [*mapnames]
rev_mapnames.reverse()
locs = []

for seed in seeds:
    for mapname in mapnames:
        seed = lookup(seed, mapname)
    print(f"location = {seed}")
    locs.append(seed)

print(f"min loc={min(locs)}")

seed_pairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
seed_pairs.sort()
print(seed_pairs)


def lookup_pairs(pairs: List[Tuple[int, int]], mapname: str):
    out_pairs = []
    for pair in pairs:
        [seed_start, seed_length] = pair
        for [source, dest, length] in maps.get(mapname):
            if seed_start + seed_length >= source and seed_start < source + length:
                len_before_match = max(0, source - seed_start)
                len_after_match = max(0, (seed_start + seed_length) -
                                      (source + length))
                len_of_match = min(seed_start + seed_length,
                                   source + length) - max(seed_start, source)

                print({
                    "before": len_before_match,
                    "of": len_of_match,
                    "after": len_after_match,
                })

                if len_before_match:
                    out_pairs.append([seed_start, len_before_match])
                out_pairs.append([dest + seed_start - source, len_of_match])
                if len_after_match:
                    seed_start = source + length
                    seed_length = len_after_match  # seed_length - (length -
                    if seed_length == 0:
                        break
                else:
                    seed_length = 0
                    break

        if seed_length > 0:
            out_pairs.append([seed_start, seed_length])
    return out_pairs


for mapname in mapnames:
    seed_pairs = lookup_pairs(seed_pairs, mapname)
    seed_pairs.sort()
    print(mapname, seed_pairs)

seed_pairs.sort()
print(seed_pairs)

#rom multiprocessing import Pool

# rev_maps = {
#     k: v
#     for [k, v] in
#     [buildSectionMap(section.strip(), True) for section in sections[1:]]
# }
# print("revmaps", rev_maps)

# def rev_lookup(loc, mapname):
#     for [dest, source, length] in rev_maps.get(mapname):
#         if loc >= dest and loc < dest + length:
#             return source + loc - dest
#     return loc

# def check_all_seeds(seed_pair):
#     minloc = float("inf")
#     [start, count] = seed_pair
#     for seed in range(start, start + count):
#         for mapname in mapnames:
#             seed = lookup(seed, mapname)
#         if seed < minloc:
#             minloc = seed
#     return minloc

# with Pool() as pool:
#     result = pool.map(check_all_seeds, seed_pairs)

# def is_seed(n):
#     return (n >= 79 and n < (79 + 14)) or (n >= 55 and n < (55 + 13))

# def check_all_locs(locinfo):
#     [dest, source, length] = locinfo
#     for loc in range(dest, dest + length):
#         seed = loc
#         for mapname in rev_mapnames:
#             seed = lookup(seed, mapname)
#         if is_seed(seed):
#             print("seed", seed, "loc", loc)
#             return loc

# with Pool() as pool:
#     result = pool.map(check_all_locs, [*maps['humidity-to-location']])

# print(result)
# print(f"min loc={min(result)}")
