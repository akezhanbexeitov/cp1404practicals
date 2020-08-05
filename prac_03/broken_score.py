"""
CP1404 - Practical
Program to determine score status
"""


def main():
    score = int(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid")

    elif score >= 90:
        print("Excellent")

    elif score >= 50:
        print("Pass")

    elif score < 50:
        print("Bad")


if __name__ == '__main__':
    main()
