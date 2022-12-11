#!/usr/bin/env python3
from functools import reduce
import math

from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=11, year=2022).splitlines()
data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n")

def make_monkey(monkey_text):
    monkey = {
        "items": [],
        "operation": lambda x: x * 19,
        "test": lambda x: (x/23) == 0,
        "true": 2,
        "false": 3,
        "inspections": 0
    }
    monkey["items"] = [int(x) for x in (monkey_text[1]
                                    .replace("Starting items:", "")
                                    .replace(",", "").split())]
    try:
        operand = int(monkey_text[2].split()[-1])
    except ValueError:
        operand = None
    operation = monkey_text[2].split()[-2]
    if operation == "*":
        if operand is not None:
            monkey["operation"] = lambda x: x * operand
        else:
            monkey["operation"] = lambda x: x * x
    elif operation == "+":
        if operand is not None:
            monkey["operation"] = lambda x: x + operand
        else:
            monkey["operation"] = lambda x: x + x

    divisor = int(monkey_text[3].split()[-1])
    monkey["test"] = lambda x: (x % divisor) == 0
    monkey["true"] = int(monkey_text[4].split()[-1])
    monkey["false"] = int(monkey_text[5].split()[-1])
    return monkey

def make_monkey_text(monkeys, next_line):
    if next_line == "":
        monkeys.append([])
    else:
        monkeys[-1].append(next_line)
    return monkeys

def simulate_round(monkeys):
    for idx, monkey in enumerate(monkeys):
        for item in monkey["items"]:
            monkey["inspections"] += 1
            worry = monkey["operation"](item)
            worry = math.floor(monkey["operation"](item) / 3)
            if monkey["test"](worry):
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)
            pass
        monkey["items"] = []  # seems right



monkeys = list(map(make_monkey, reduce(make_monkey_text, data, [[]])))
for _ in range(20):
    simulate_round(monkeys)
monkeys = reduce(lambda x,y: x*y, sorted([x["inspections"] for x in monkeys])[-2:])
print(monkeys)
