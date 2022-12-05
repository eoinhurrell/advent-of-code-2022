#!/usr/bin/env python3
from functools import partial, reduce

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=5, year=2022)


def process_layout_line(line):
    return line.replace("    ", " ").split(" ")


def process_move_line(line):
    return list(map(int, filter(lambda x: x != '', (line.replace("move", "")
                                          .replace("from", "")
                                          .replace("to", "")
                                          .split(" ")))))


def add_to_stacks(items):
    stacks = [[] for _ in range(9)]
    for idx, item in enumerate(items):
        if item != '':
            stacks[idx].append(item.replace("[", "").replace("]", ""))
    return stacks


def merge_rows(first_row, second_row):
    for idx in range(len(first_row)):
        first_row[idx].extend(second_row[idx])
    return first_row


def move_stacks(stacks, amount, source, destination):
    for _ in range(amount):
        stacks[destination-1].extend(stacks[source-1].pop())


stacks = list(map(lambda x: list(reversed(x)),
                  reduce(merge_rows,
                     map(add_to_stacks,
                         map(process_layout_line,
                             filter(lambda x: x.startswith("["),
                                    data.splitlines()))))))

execute_moves = partial(move_stacks, stacks)

list(map(lambda x: execute_moves(*x),
         map(process_move_line,
                 filter(lambda x: x.startswith("move"), data.splitlines())
             )))

print("".join(list(map(lambda x: x[-1], stacks))))
