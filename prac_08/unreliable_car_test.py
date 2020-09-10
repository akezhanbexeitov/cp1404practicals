from prac_08.unreliable_car import UnreliableCar


def main():
    old_car = UnreliableCar("Lada Kalina", 120, 60.0)
    print(old_car.drive(40))


if __name__ == '__main__':
    main()