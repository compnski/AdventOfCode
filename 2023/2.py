#!/usr/bin/env python3
#!/usr/bin/env python3
import re

data = open("2.txt", "r").read()

test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

lines = data.splitlines(True)
#lines = test_data.splitlines(True)


def parseRound(round: str):
    ret = {}
    for pull in round.split(", "):
        [count, color] = pull.split(" ")
        ret[color] = int(count)
    return ret


def maxDict(dictlist):
    ret = {}
    for d in dictlist:
        for [key, value] in d.items():
            ret[key] = max(ret.get(key, float('-inf')), value)
    return ret


def minDict(dictlist):
    ret = {}
    for d in dictlist:
        for [key, value] in d.items():
            ret[key] = min(ret.get(key, float('inf')), value)
    return ret


def isLessThanEqTo(a, b):
    for [key, value] in a.items():
        if b[key] > value:
            return False
    return True


def setPower(d):
    return d['red'] * d['blue'] * d['green']


actualCount = {'red': 12, 'blue': 14, 'green': 13}

sum = 0
powerSum = 0
for line in lines:
    [id, game] = line.strip().split(": ")

    rounds = [parseRound(r) for r in game.split("; ")]
    maxes = maxDict(rounds)
    mins = minDict(rounds)
    power = setPower(maxes)
    print(id, power, mins)
    powerSum += power
    if isLessThanEqTo(actualCount, maxes):
        intId = int(id[5:])
        sum += intId
print(sum)
print(powerSum)
