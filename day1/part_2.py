#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=1, year=2022)
elves = []

current_elf = 0
current_elf_energy = 0

for line in data.splitlines():
    if line == "":
        elves.append({'elf': current_elf,
                      'energy': current_elf_energy})
        current_elf += 1
        current_elf_energy = 0
    else:
        current_elf_energy += int(line)

elves.sort(key=lambda x: x['energy'])
print(sum([x['energy'] for x in elves[-3:]]))
