import math

class Shape:
    def __init__(self, identifier):
        self.identifier = identifier

class Rectangle(Shape):
    def __init__(self, identifier, top_left, bottom_right):
        super().__init__(identifier)
        self._top_left = top_left
        self._bottom_right = bottom_right

    @property
    def top_left(self):
        return self._top_left

    @top_left.setter
    def top_left(self, value):
        if len(value) != 2:
            raise ValueError("Требуется две координаты")
        elif value[0] > self._bottom_right[0] and value[1] < self._bottom_right[1]  :
            self._bottom_right = value
        else:
            self._top_left = value

    @property
    def bottom_right(self):
        return self._bottom_right

    @bottom_right.setter
    def bottom_right(self, value):
        if len(value) != 2:
            raise ValueError("Требуется две координаты")
        elif value[0] < self._bottom_right[0] and value[1] > self._bottom_right[1]  :
            self._top_left = value
        else:
            self._bottom_right = value

    def area(self):
        width = self._bottom_right[0] - self._top_left[0]
        height = self._top_left[1] - self._bottom_right[1]
        return width * height

class Pentagon(Shape):
    def __init__(self, identifier, center, radius):
        super().__init__(identifier)
        self._center = center
        self._radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        if len(value) == 2:
            self._center = value
        else:
            raise ValueError("Требуется две координаты")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Радиус должен быть положительным")

    def area(self):
        side = 2 * self._radius * math.sin(math.pi / 5)
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2
    
def is_include(t1, t2):
    if isinstance(t1, Rectangle) and isinstance(t2, Rectangle):
        return (t1.top_left[0] <= t2.top_left[0] and
                t1.top_left[1] >= t2.top_left[1] and
                t1.bottom_right[0] >= t2.bottom_right[0] and
                t1.bottom_right[1] <= t2.bottom_right[1])
    
    if isinstance(t1, Rectangle) and isinstance(t2, Pentagon):
        pentagon_bounds = (
            (t2.center[0] - t2.radius, t2.center[1] + t2.radius),  
            (t2.center[0] + t2.radius, t2.center[1] - t2.radius)   
        )
        return (t1.top_left[0] <= pentagon_bounds[0][0] and
                t1.top_left[1] >= pentagon_bounds[0][1] and
                t1.bottom_right[0] >= pentagon_bounds[1][0] and
                t1.bottom_right[1] <= pentagon_bounds[1][1])