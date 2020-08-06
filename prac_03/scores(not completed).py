"""
CP1404 - Practical
Program to determine score status
"""

from random import randint


def main():
    number_of_scores = int(input("Enter number of scores: "))
    score = randomize_score(number_of_scores)
    print(score)

def get_score(score):
    if score < 0 or score > 100:
        return "Invalid"

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Pass"

    elif score < 50:
        return "Bad"

    
def randomize_score(number_of_scores):
    for i in range(0, number_of_scores):
        score = randint(0, 100)
        return score



if __name__ == '__main__':
    main()
