#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=6, year=2022)

print([len(set(data[idx-14:idx])) for idx, _ in enumerate(data) if idx >=14].index(14) + 14)
