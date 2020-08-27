
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar)
print("Gibson L-5 CES get_age() - Expected 98. Got {}".format(guitar.get_age()))
print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(guitar.is_vintage()))


