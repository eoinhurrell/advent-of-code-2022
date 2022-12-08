#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=8, year=2022)

def viewing_distance(row, tree):
    distances = [x >= tree for x in row]
    try:
        return distances.index(True) + 1
    except ValueError:
        return len(distances)

def check_tree(row, row_idx, tree):
    if row_idx == 0 or row_idx == (len(row) - 1):
        return True
    return viewing_distance(reversed(row[:row_idx]), tree) * viewing_distance(row[row_idx + 1:], tree)

def check_row(row):
    return [int(check_tree(row, row_idx, tree)) for row_idx, tree in enumerate(row)]

trees = list(map(lambda x: [int(z) for z in list(x)], data.splitlines()))
visible_vertical = list(map(check_row, trees))

trees = list(map(list, zip(*trees)))[::-1]
visible_horizontal = list(map(check_row, trees))

# rotate 270 degrees
visible_horizontal = list(zip(*list(zip(*list(zip(*visible_horizontal))[::-1]))[::-1]))[::-1]

print(max(list(map(lambda x: max([x * y for x,y in zip(*x)]), zip(visible_vertical, visible_horizontal)))))
# 314820
