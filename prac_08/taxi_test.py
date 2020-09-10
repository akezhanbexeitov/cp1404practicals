from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = Taxi("Prius 1", 100)

    taxi.start_fare()
    taxi.drive(40)
    taxi.get_fare()
    print(taxi)

    print()

    taxi.start_fare()
    taxi.drive(100)
    taxi.get_fare()
    print(taxi)

    luxury_taxi = SilverServiceTaxi("Lexus LX570", 200, 2)

    luxury_taxi.start_fare()
    luxury_taxi.drive(30)
    luxury_taxi.get_fare()
    print(luxury_taxi)


if __name__ == '__main__':
    main()