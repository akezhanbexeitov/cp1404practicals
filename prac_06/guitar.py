
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2020 - self.year
        return age

    def is_vintage(self):
        if 2020 - self.year >= 50:
            return "(vintage)"
        else:
            return ""

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return "{} ({}) : ${:,.2f} added.".format(self.name, self.year, self.cost)