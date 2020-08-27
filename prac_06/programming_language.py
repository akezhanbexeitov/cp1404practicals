
class ProgrammingLanguage:
    def __init__(self, name="",typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.reflection:
            return self.name

    def __str__(self):
        return "{}, {} Typing, Reflection={}, first appeared in {}".format(self.name, self.typing, self.reflection, self.year)
