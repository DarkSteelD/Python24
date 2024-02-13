import math
import  
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

    def dots():
        return self._top_left ,  self._bottom_right , (self._top_left[0], self._bottom_right[1]), ( self._bottom_right[0], self._top_left[1])
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
        first_dots = list(itertools.combinations(t1.dots, 2))
        second_dots = list(itertools.combinations(t1.dots, 2))
        Flag = False
        for a in first_dots:
            for b in second_dots:
                Flag = Flag or is_intersecting(a,b)
        return Flag

                
    if isinstance(t1, Pentagon) and isinstance(t2, Pentagon):
        first_dots = list(itertools.combinations(t1.dots, 2))
        second_dots = list(itertools.combinations(t1.dots, 2))
        Flag = False
        for a in first_dots:
            for b in second_dots:
                Flag = Flag or is_intersecting(a,b)
        return Flag
    return False

def is_intersecting(a,b):
    x1, y1 = a[0]
    x2, y2 = a[1]
    x3, y3 = b[0]
    x4, y4 = b[1]
    g = ()
    if x2 == x1:
        f = (0,x1)
    else:
        alpha = (y2 - y1) / (x2 - x1)
        betha = y1 - a * x1
        f = (alpha,betha)
    if x3 == x4:
        h = (0,x3)
    else:
        alpha = (y4 - y3) / (x4 - x3)
        betha = y3 - a * x3
        h = (alpha,betha)
        #Дальше ищем точку пересечения
    if  h[0]-f[0]==0:
        return False
    else:
        x = -(h[1]-f[1])/(h[0]-f[0])
        y = x*h[0] + h[1]
        g =(x,y)
    return x1 <= x <= x2 and x3 <= x <= x4 and y1 <= y <= y2 and y3 <= y <= y4
    
    
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