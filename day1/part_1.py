#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=1, year=2022)
energetic_elf = 0
current_elf = 0

max_elf_energy = 0
current_elf_energy = 0

for line in data.splitlines():
    if line == "":
        if current_elf_energy > max_elf_energy:
            max_elf_energy = current_elf_energy
            energetic_elf = current_elf
        current_elf += 1
        current_elf_energy = 0
    else:
        current_elf_energy += int(line)
if current_elf_energy > max_elf_energy:
    max_elf_energy = current_elf_energy
    energetic_elf = current_elf
current_elf += 1
current_elf_energy = 0

print(energetic_elf, max_elf_energy)
