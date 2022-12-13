#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=13, year=2022).splitlines()


def parse_items(line):
    if line == "":
        return None
    return eval(line) # cheeky / dangerous


def already_sorted(left, right):
    print(f"comparing {left} and {right}")
    if type(left) != type(right):  # mixed
        if type(left) == int:
            left = [left]
        elif type(right) == int:
            right = [right]

    if type(left) == type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
    else:  # lists
        decision = None
        if len(left) < len(right):
            decision =  True
        elif len(left) > len(right):
            decision = False

        for v1, v2 in zip(left, right):
            com = already_sorted(v1,v2)
            if com is None:
                continue
            else:
                return com
        return decision


def compare_packets(loc, packets):
    packet_a, packet_b = packets
    print(f"{loc}: a: {len(packet_a)}, b: {len(packet_b)}")
    for idx in range(len(packet_a)):
        try:
            if already_sorted(packet_a[idx], packet_b[idx]):
                print(f"{loc}: hit: {packet_a[idx]}, {packet_b[idx]}")
                return loc
        except IndexError:
            return 0
    if len(packet_a) < len(packet_b):
        return loc
    return 0


packets = list(filter(lambda x: x is not None, map(parse_items, data)))
answer = 0
for i, (ar1, ar2) in enumerate(zip(packets[:-1:2],packets[1::2])):  # iterate in pairs of two
    if already_sorted(ar1, ar2):
        answer += i+1
print(answer)
# 5503
