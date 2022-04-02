"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

LIMIT_MIN = 0
LIMIT_MAX = 100
LIMIT_PASS = 50
LIMIT_EXCELLENT = 90


def main():
    no_of_scores = int(input("How many score? "))
    repeats = 0
    while repeats != no_of_scores:
        score = float(random.randint(0, 100))
        result = check_score(score)
        print(f"{score} is {result}")
        repeats += 1


def check_score(score):
    if LIMIT_MIN <= score <= LIMIT_MAX:
        if score >= LIMIT_EXCELLENT:
            result = "Excellent"
        elif score >= LIMIT_PASS:
            result = "Passable"
        else:
            result = "Bad"
    else:
        result = "Invalid score"
    return result


main()
