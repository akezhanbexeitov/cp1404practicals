def main():
    #  Asks for name and writes it in name.txt
    name = input("What is your name? ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()

    #  Opens name.txt reads the name and prints it
    out_file = open("name.txt", "r")
    print("Your name is {}".format(out_file.read().strip()))
    out_file.close()

    #  Adds first 2 nums in numbers.txt
    out_file = open("numbers.txt", "r")
    number1 = int(out_file.readline())
    number2 = int(out_file.readline())
    out_file.close()
    result = number2 + number1
    print(result)

    # Adds all nums in numbers.txt
    out_file = open("numbers.txt", "r")
    total = 0
    for line in out_file:
        number = int(line)
        total += number
    out_file.close()
    print(total)


if __name__ == '__main__':
    main()
