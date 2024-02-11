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
    def __init__(self, identifier, *args):
        super().__init__(identifier)
        if len(args) != 5 or not all(len(dot) == 2 for dot in args):
            raise ValueError("Для каждой вершины требуется две координаты и всего 5 вершин")
        self._dots = list(args)

        

    @property
    def dots(self):
        return self._dots

    def set_dot(self, index, value):
        if len(value) == 2:
            self._dots[index] = value
        else:
            raise ValueError("Требуется две координаты")
    def get_dot(self, index):
        return self._dots[index]
    def buttom_right(self):
        return max(self.dots, key=lambda dot: dot[0])[0]  , min(self.dots, key=lambda dot: dot[1])[1] 
    def top_left(self):
        return min(self.dots, key=lambda dot: dot[0])[0] , max(self.dots, key=lambda dot: dot[1])[1]
    
def is_include(t1, t2):
    if isinstance(t1, Rectangle) and isinstance(t2, Rectangle):
        return (t1.top_left[0] <= t2.top_left[0] and
                t1.top_left[1] >= t2.top_left[1] and
                t1.bottom_right[0] >= t2.bottom_right[0] and
                t1.bottom_right[1] <= t2.bottom_right[1]) 
    
    if isinstance(t1, Rectangle) and isinstance(t2, Pentagon):
        return (t1.top_left[0] <= t2.top_left[0] and
                t1.top_left[1] >= t2.top_left[1] and
                t1.bottom_right[0] >= t2.bottom_right[0] and
                t1.bottom_right[1] <= t2.bottom_right[1])
    if isinstance(t1, Pentagon) and isinstance(t2, Pentagon):
        return (t1.top_left[0] <= t2.top_left[0] and
                t1.top_left[1] >= t2.top_left[1] and
                t1.bottom_right[0] >= t2.bottom_right[0] and
                t1.bottom_right[1] <= t2.bottom_right[1])
    return False

def is_intersect(t1, t2):
    if isinstance(t1, Rectangle) and isinstance(t2, Rectangle):
        return not (t1.bottom_right[0] < t2.top_left[0] or  
                    t1.top_left[0] > t2.bottom_right[0] or  
                    t1.bottom_right[1] > t2.top_left[1] or  
                    t1.top_left[1] < t2.bottom_right[1]) 
    
    if isinstance(t1, Rectangle) and isinstance(t2, Pentagon):
        return not (t1.bottom_right[0] < t2.top_left[0] or  
                    t1.top_left[0] > t2.bottom_right[0] or  
                    t1.bottom_right[1] > t2.top_left[1] or  
                    t1.top_left[1] < t2.bottom_right[1]) 
    if isinstance(t1, Pentagon) and isinstance(t2, Pentagon):
        return not (t1.bottom_right[0] < t2.top_left[0] or  
                    t1.top_left[0] > t2.bottom_right[0] or  
                    t1.bottom_right[1] > t2.top_left[1] or  
                    t1.top_left[1] < t2.bottom_right[1]) 
    return False
polygos = []
a = int(input("Введите количетство фигур : "))
try:
    for _ in range(a):
        i = [int(f) for f in input("Введите точки : ").split()]
        if(len(i)==4):
            r =  Rectangle(_,(i[0],i[1]),(i[2],i[3]))
        elif(len(i)==10):
            r =  Pentagon(_,(i[0],i[1]),(i[2],i[3]),(i[4],i[5]),(i[6],i[7]),(i[8],i[9]))
        polygos.append(r)
        a = input("Какие фигуры сравнить? ")        

    i = [int(f) for f in a.split()]
    print(f"Фигура {i[0]} пересекает {i[1]} {is_intersect(polygos[i[0]-1],polygos[i[1]-1])}")
    print(f"Фигура {i[0]} включает {i[1]} {is_include(polygos[i[0]-1],polygos[i[1]-1])}")
except ValueError as error:
    print(error)