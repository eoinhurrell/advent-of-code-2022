#!/usr/bin/env python3
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=2, year=2022)

codes = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": 6,  # opponent's score for the match
    "Y": 3,
    "Z": 0
}
choice_scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

game_scores = {
    "Rock": {"Rock": 3, "Paper": 0, "Scissors": 6},
    "Paper": {"Rock": 6, "Paper": 3, "Scissors": 0},
    "Scissors": {"Rock": 0, "Paper": 6, "Scissors": 3},
}

def resolve_game(them, you):
    return game_scores[you][them] + choice_scores[you]

def get_your_move(them, end):
    location = list(game_scores[them].values()).index(end)
    return list(game_scores[them].keys())[location]

total_score = 0
for line in data.splitlines():
    them, end = map(lambda x: codes[x], line.split(" "))
    you = get_your_move(them, end)
    total_score += resolve_game(them, you)
    print(line, them, you)
print(total_score)
