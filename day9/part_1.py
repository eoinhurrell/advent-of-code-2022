#!/usr/bin/env python3
from functools import partial, reduce

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=9, year=2022).splitlines()


def build_movements(move):
    move = move.split()
    movements = []
    match move[0]:
        case "U":
            for _ in range(int(move[1])):
                movements.append([1, 0])
        case "D":
            for _ in range(int(move[1])):
                movements.append([-1, 0])
        case "L":
            for _ in range(int(move[1])):
                movements.append([0, -1])
        case "R":
            for _ in range(int(move[1])):
                movements.append([0, 1])
    return movements


def move_towards(head, tail):
    x_dist = head[0] - tail[0]
    y_dist = head[1] - tail[1]
    if abs(x_dist) == 2:
        tail[0] += 1 if x_dist > 0 else -1
        if abs(y_dist) == 1:
            tail[1] += y_dist
    if abs(y_dist) == 2:
        tail[1] += 1 if y_dist > 0 else -1
        if abs(x_dist) == 1:
            tail[0] += x_dist
    return tail


def update_positions(rope, movement):
    head = rope[-1][0].copy()
    tail = rope[-1][1].copy()
    head[0] += movement[0]
    head[1] += movement[1]

    tail = move_towards(head, tail)
    rope.append([head, tail])
    return rope


rope = [[0,0], [0,0]] # head, tail
move_head = partial(update_positions, rope)

commands = [move for command in list(map(build_movements, data)) for move in command]
positions = list(reduce(update_positions, commands , [rope]))
unique_positions = set(map(lambda x: ",".join([str(y) for y in x[1]]), positions))
print(len(unique_positions))
# 6098
