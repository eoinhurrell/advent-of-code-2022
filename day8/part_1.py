#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=8, year=2022)

def is_visible(row, tree):
    return sum([x >= tree for x in row]) == 0

def check_tree(row, row_idx, tree):
    if row_idx == 0 or row_idx == (len(row) - 1):
        return True
    return is_visible(row[:row_idx], tree) or is_visible(row[row_idx + 1:], tree)

def check_row(row):
    return [int(check_tree(row, row_idx, tree)) for row_idx, tree in enumerate(row)]

trees = list(map(lambda x: [int(z) for z in list(x)], data.splitlines()))
visible_vertical = list(map(check_row, trees))

trees = list(map(list, zip(*trees)))[::-1]
visible_horizontal = list(map(check_row, trees))

# rotate 270 degrees (I need to refresh on list transposition)
visible_horizontal = list(zip(*list(zip(*list(zip(*visible_horizontal))[::-1]))[::-1]))[::-1]

print(sum(list(map(lambda x: sum([x or y for x,y in zip(*x)]), zip(visible_vertical, visible_horizontal)))))
# 1789
