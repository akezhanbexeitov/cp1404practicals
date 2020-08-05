def main():
    for i in range(1, 21, 2):  # only odd numbers from 1 to 20
        print(i, end=" ")
    print()

    for i in range(0, 101, 10):  # count in 10s from 0 to 100
        print(i, end=" ")
    print()

    for i in range(20, 0, -1):  # count down from 20 to 1
        print(i, end=" ")
    print()

    number_of_stars = int(input("Number of stars: "))  # n stars depending on the user's number
    for i in range(0, number_of_stars):
        print("*", end="")
    print()

    stars = 1  # n lines of increasing stars depending on user's number
    for i in range(0, number_of_stars, 1):
        print("*" * stars)
        stars += 1


if __name__ == '__main__':
    main()
