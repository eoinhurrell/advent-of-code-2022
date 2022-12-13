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
    else:
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


def bubble_sort(items):
    n = len(items)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if already_sorted(items[j + 1], items[j]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


packets = list(filter(lambda x: x is not None, map(parse_items, data)))
decoder_keys =[[[2]], [[6]]]
packets.extend(decoder_keys)

packets = bubble_sort(packets)
key_idxes = []
for decoder in decoder_keys:
    for idx, item in enumerate(packets):
        if str(decoder) == str(item):
            key_idxes.append(idx+1)
print(key_idxes[0] * key_idxes[1])
