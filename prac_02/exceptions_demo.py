"""
CP1404/CP5632 - Practical
Answer the following questions:
Q1: ValueError will occur when a user will try to key in anything else except whole number
Q2: ZeroDivisionError will occur when a user will try to key in 0 in denominator
Q3: I think the only way to avoid the possibility of a ZeroDivisionError is to put tips for users
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator (not 0): "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


if __name__ == '__main__':
    main()
