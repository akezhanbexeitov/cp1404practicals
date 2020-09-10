from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    price_per_km = 1.23
    flagfall = 4.50
    price = 0

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km *= float(fanciness)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${}. Total price is ${}".format(super().__str__(),
                                                                    self.flagfall,
                                                                    self.price)

    def get_fare(self):
        self.price += super().get_fare() + self.flagfall
        return super().get_fare()

    def start_fare(self):
        return super().start_fare()

    def drive(self, distance):
        return super().drive(distance)