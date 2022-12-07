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


def sum_size(dir_sizes, next_file):
    path = next_file[0].split("/")
    for idx in range(len(path)):
        dir_sizes["/".join(path[:idx])] += next_file[1]
    dir_sizes[next_file[0]] += next_file[1]
    return dir_sizes


print(sum(map(lambda x: x[1], filter(lambda x: x[1] < 100000, (reduce(sum_size, filter(lambda x: x is not None, map(unroll_tree, data.splitlines())), Counter())).items()))))
