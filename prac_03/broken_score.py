"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

LIMIT_MIN = 0
LIMIT_MAX = 100
LIMIT_PASS = 50
LIMIT_EXCELLENT = 90


def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)


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
