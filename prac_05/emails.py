def main():
    my_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name)).lower()
        if confirmation == "" or confirmation == "y" or confirmation == "yes":
            my_dict[name] = email
        elif confirmation == "no" or confirmation == "n":
            name = input("Name: ")
            my_dict[name] = email
        else:
            print("Invalid input. Try again")
        print(my_dict)
        email = input("Email: ")

    for k, v in my_dict.items():
        print("{} ({})".format(k, v))


def get_name_from_email(email):
    """Identify name using email"""
    at_removed_list = email.split("@")
    name = str(at_removed_list[0])
    dot_removed_list = name.split(".")
    separator = " "
    name = separator.join(dot_removed_list)
    name = name.title()
    return name


if __name__ == '__main__':
    main()