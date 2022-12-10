#!/usr/bin/env python3
from functools import reduce

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=10, year=2022).splitlines()


def parse_op(instruction):
    if instruction == "noop":
        return [0]
    return [0, int(instruction.replace("addx ", ""))]


def accumulate(current, next_op):
    current['cycle'] += 1
    current['X'] += next_op
    line_offset = (current['cycle'] % 40)
    chunks = [current['X'] - 1, current['X'], current['X'] + 1]
    for point in chunks:
        if line_offset == point:
            current['monitor'][current['cycle']] = '#'
    return current


def print_monitor(monitor):
    # a hack, 0 should be #
    monitor[0] = '#'
    monitor_width = 40
    line = []
    for idx, char in enumerate(monitor):
        if idx % monitor_width == 0 and idx != 0:
            print("".join(line))
            line = []
        line.append(char)
    print("".join(line))

tape = [change for command in list(map(parse_op, data)) for change in command]
result = reduce(accumulate, tape, {'cycle': 0, 'X': 1, 'monitor': ['.'] * (40 * 6)})
print_monitor(result['monitor'])
# RFKZCPEF
