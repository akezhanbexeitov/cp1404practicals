MIN_LENGTH = 6


def main():
    password = input("Password ({} characters min): ".format(MIN_LENGTH))

    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Password ({} characters min): ".format(MIN_LENGTH))

    for char in password:
        print("*", end="")


if __name__ == '__main__':
    main()
