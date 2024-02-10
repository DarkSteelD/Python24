import math
class Shape:
    def __init__(self, identifier):
        self.identifier = identifier
class Rectangle(Shape):
    def __init__(self, identifier, top_left, bottom_right):
        super().__init__(identifier)
        self.top_left = top_left
        self.bottom_right = bottom_right

    def area(self):
        width = self.bottom_right[0] - self.top_left[0]
        height = self.top_left[1] - self.bottom_right[1]
        return width * height

class Pentagon(Shape):
    def __init__(self, identifier, center, radius):
        super().__init__(identifier)
        self.center = center
        self.radius = radius
    def area(self):
        side = 2 * self.radius * math.sin(math.pi / 5)
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2
