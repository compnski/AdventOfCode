#!/usr/bin/env python3
import re

data = open("1.txt", "r").read()

test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

nums = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]


def numToInt(s: str):
    if s.isnumeric():
        return s
    return nums.index(s)


sum = 0
lines = data.splitlines(True)
for line in lines:
    print(line)
    m = re.match(
        "^.*?([0-9]|one|two|three|four|five|six|seven|eight|nine|zero).*([0-9]|one|two|three|four|five|six|seven|eight|nine|zero).*$",
        line)
    if m:
        print(111)
        print(m.groups())
        s = "".join(str(numToInt(n)) for n in m.groups())
        print("s", s)
        sum += int(s)
    else:
        m = re.search(
            "([0-9]|one|two|three|four|five|six|seven|eight|nine|zero)", line)
        if m:
            s = int("".join(str(numToInt(n)) for n in m.groups()) * 2)
            print(s)
            sum += s

print(sum)
