#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=3, year=2022)

def letters_to_priority(common):
    def letter_to_priority(letter):
        if letter == letter.lower():
            return ord(letter) - 96
        return ord(letter) - (64 - 26)
    return sum(map(letter_to_priority, common))

def find_common_letter(compartments):
    common = set(compartments[0])
    for compart in compartments[1:]:
        common = common.intersection(set(compart))
    return list(common)

def split_compartments(rucksack):
    halfway = int(len(rucksack)/2)
    return [rucksack[:halfway], rucksack[halfway:]]

rucksacks = [line for line in data.splitlines()]
compartments = map(split_compartments, rucksacks)
letters = map(find_common_letter, compartments)
priorities = map(letters_to_priority, letters)
answer = sum(priorities)
print(answer)
