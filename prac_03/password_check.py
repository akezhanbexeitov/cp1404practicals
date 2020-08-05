MIN_LENGTH = 6


def main():
    password = get_password()

    change_to_asterisks(password)


def change_to_asterisks(password):
    for char in password:
        print("*", end="")


def get_password():
    password = input("Password ({} characters min): ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Password ({} characters min): ".format(MIN_LENGTH))
    return password


if __name__ == '__main__':
    main()
