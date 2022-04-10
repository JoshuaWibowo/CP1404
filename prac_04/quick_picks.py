"""
CP1404/CP5632 Practical
Quick picks
"""
import random

NUMBERS_IN_PICK = 6  # How many numbers in one pick
MIN_NUMBER = 1  # Minimum value in a pick
MAX_NUMBER = 45  # Maximum value in a pick

quick_pick = int(input("How many quick picks? "))
for pick in range(quick_pick):
    quick_picks = []
    for number in range(NUMBERS_IN_PICK):
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        while num in quick_picks:
            num = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_picks.append(num)
    quick_picks.sort()
    for value in quick_picks:
        print(f"{value:3}", end='')
    print()
