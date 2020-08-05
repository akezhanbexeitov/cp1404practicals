"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to the total.
"""


def main():
    number_of_items = int(input("Number of items: "))

    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total = 0
    for i in range(0, number_of_items):
        price = float(input("Price of an item: $"))
        total += price

    if total > 100:
        total = total - (total * 0.1)
        print("Total price for {} items is ${:.2f}".format(number_of_items, total))

    else:
        print("Total price for {} items is ${:.2f}".format(number_of_items, total))


if __name__ == '__main__':
    main()
