def main():
    color_to_hex = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE1": "#7fffd4",
               "AZURE1": "#f0ffff", "BEIGE": "#f5f5dc", "BISQUE1": "#ffe4c4", "BLACK": "#000000"}

    color = input("Color: ").upper()
    while color != "":
        if color in color_to_hex:
            print("{} is {}".format(color, color_to_hex[color]))
        else:
            print("Invalid input")
        color = input("Color: ").upper()


if __name__ == '__main__':
    main()