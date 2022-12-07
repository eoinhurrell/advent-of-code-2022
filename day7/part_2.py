#!/usr/bin/env python3
from functools import reduce
from collections import Counter

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=7, year=2022)
path = ""


def unroll_tree(item):
    global path
    if item == "$ ls":
        return None
    elif item.startswith("$ cd"):
        if item.endswith(".."):
            path = path[:path.rfind("/")]
        else:
            path = path + "/" + item.replace("$ cd ", "")
            path = path.replace("//", "/")
        return None
    item = item.split(" ")
    if item[0] == "dir":
        return None
    return (path, int(item[0]))


dir_sizes = {}
filetree = list(filter(lambda x: x is not None, map(unroll_tree, data.splitlines())))
for fpath, size in filetree:
    dir_sizes[fpath] = 0

for dir_path in dir_sizes:
    for path, size in filetree:
        if path.startswith(dir_path):
            dir_sizes[dir_path] += size

for dir_path in dir_sizes:
    print(dir_path, dir_sizes[dir_path])

target_size = 30000000 - ( 70000000 - dir_sizes["/"] )
print(sorted(filter(lambda x: x[1] >= target_size, dir_sizes.items()), key=lambda x: x[1])[0])
