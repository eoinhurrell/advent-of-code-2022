#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=4, year=2022)

def any_overlap(first, second):
    return not second.isdisjoint(first)

def make_set(text_range):
    start, end = text_range.split("-")
    sections = set(range(int(start),int(end)+1))
    return sections

def parse_sections(line):
    elves = line.split(",")
    return any_overlap(*list(map(make_set, elves)))

print(sum([parse_sections(line) for line in data.splitlines()]))
