#!/usr/bin/env python3
from functools import partial, reduce

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
    checkpoints = [20, 60, 100, 140, 180, 220]
    if len(checkpoints) != len(current['checkpoints']):
        next_checkpoint = checkpoints[len(current['checkpoints'])]
        if current['cycle'] == next_checkpoint:
            current['checkpoints'].append(next_checkpoint * current['X'])
    current['X'] += next_op
    return current

tape = [change for command in list(map(parse_op, data)) for change in command]
result = reduce(accumulate, tape, {'cycle': 0, 'X': 1, 'checkpoints': []})
print(sum(result['checkpoints']))
# 13760
