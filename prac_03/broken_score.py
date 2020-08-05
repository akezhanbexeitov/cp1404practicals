"""
CP1404 - Practical
Program to determine score status
"""

from random import randint


def main():
    score = randomize_score()
    print(get_score(score))


def get_score(score):
    if score < 0 or score > 100:
        return "Invalid"

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Pass"

    elif score < 50:
        return "Bad"


def randomize_score():
    score = randint(0, 100)
    return score


if __name__ == '__main__':
    main()
