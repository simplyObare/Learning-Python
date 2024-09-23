import math

class Shapes:
    def area(self):
        pass

    def parimeter(self):
        pass


class Circle(Shapes):
    def __int__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def parimeter(self):
        return 2 * math.pi * self.radius