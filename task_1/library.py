import math

class Shape:
    def square(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, firstSide, secondSide, thirdSide):
        self._firstSide = firstSide
        self._secondSide = secondSide
        self._thirdSide = thirdSide

    def square(self):
        semiPerimeter = (self._firstSide + self._secondSide + self._thirdSide) / 2
        return (semiPerimeter * (semiPerimeter - self._firstSide) * (semiPerimeter - self._secondSide) * (semiPerimeter - self._thirdSide)) ** 0.5

    def is_right(self):
        return ((self._firstSide ** 2 + self._secondSide ** 2) == self._thirdSide ** 2) or \
               ((self._thirdSide ** 2 + self._secondSide ** 2) == self._firstSide ** 2) or \
               ((self._firstSide ** 2 + self._thirdSide ** 2) == self._secondSide ** 2)
