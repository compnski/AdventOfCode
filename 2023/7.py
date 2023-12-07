#!/usr/bin/env python3
import re
import functools

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

data = test_data
data = open("7.txt").read().strip()
lines = data.split("\n")

hand_bids = [line.split(" ") for line in lines]

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards.reverse()
print(cards)


def rank(card):
    return cards.index(card)


# def handbid_to_key(hand_bid):
#     hand = [*hand_bid[0]]
#     hand.sort()
#     handStr = "".join(hand)
#     print(handStr)
#     for n in range(4, -1, -1):
#         pat = f"(\w)\\1{{{n}}}"
#         print(pat)
#         if re.search(pat, handStr):
#             key = rank(hand_bid[0][0]) + (10 * (n + 1))
#             print(n, handStr, key)
#             return key


def hand_kind(hand_bid):
    hand = [*hand_bid[0]]
    hand.sort()
    handStr = "".join(hand)
    for n in range(4, -1, -1):
        pat = f"(\w)\\1{{{n}}}"
        if m := re.search(pat, handStr):
            matchedletter = m.group()[0]
            if n == 2 or n == 1:
                if re.search(f"([^{matchedletter}])\\1", handStr):
                    return n + 1.5  # fullhouse / two pair
            return n + 1


# 246758041
# 246438593
#64833338


def hand_score(hand_bid):
    return sum(
        pow(13, (4 - n)) * rank(card) for n, card in enumerate(hand_bid[0]))


def cmp_handbid(a, b):
    kind_a, kind_b = hand_kind(a), hand_kind(b)
    if kind_a != kind_b:
        return kind_a - kind_b
    return hand_score(a) - hand_score(b)


hand_bids.sort(key=functools.cmp_to_key(cmp_handbid))

for hand_bid in hand_bids:
    print(hand_bid, hand_kind(hand_bid), hand_score(hand_bid))

scores = [
    int(bid) * (rank + 1) for [rank, [hand, bid]] in enumerate(hand_bids)
]
print(len(scores))
print(scores)
print(sum(scores))
