#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=4, year=2022)

def fully_contains(first, second):
    return second.issuperset(first) or first.issuperset(second)

def make_set(text_range):
    start, end = text_range.split("-")
    sections = set(range(int(start),int(end)+1))
    return sections

def parse_sections(line):
    elves = line.split(",")
    return fully_contains(*list(map(make_set, elves)))

print(sum([parse_sections(line) for line in data.splitlines()]))
