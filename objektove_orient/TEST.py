 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vypis_P(self):
        return f"({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    

    def move(self, dx, dy):
        self.p1.move(dx,dy)
        self.p2.move(dx,dy)
        self.p3.move(dx,dy)
        self.p4.move(dx,dy)

    def area(self):
        sirka_A = abs(self.p2.x - self.p1.x)
        vyska_B = abs(self.p4.y - self.p1.y)
        return sirka_A * vyska_B

    def contains_point(self, point):
        cx = [self.p1.x, self.p2.x, self.p3.x, self.p4.x]
        cy = [self.p1.y, self.p2.y, self.p3.y, self.p4.y]

        return (min(cx) <= point.x <= max(cx) and min(cy) <= point.y <= max(cy))

    def scale(self, factor):
        x_scaled = self.p1.x
        y_scaled = self.p1.y

        for p in [self.p2, self.p3, self.p4]:
            p.x = x_scaled + (p.x - x_scaled) * factor
            p.y = y_scaled + (p.y - y_scaled) * factor






p = Point(2, 3)
print(p.x, p.y)   # 2 3


r = Rectangle(
    Point(1, 2),
    Point(5, 2),
    Point(5, 6),
    Point(1, 6)
)
print(r.p1.x, r.p1.y) #1 2
print(r.p3.x, r.p3.y) #5 6


r.move(2, -1)
print(r.p1.x, r.p1.y) #3 1
print(r.p4.x, r.p4.y) #3 5

print(r.area()) #16


inside = Point(4, 3) 
outside = Point(10, 10) 
print(r.contains_point(inside)) #True
print(r.contains_point(outside)) #False


r = Rectangle(
    Point(1, 1),
    Point(3, 1),
    Point(3, 2),
    Point(1, 2)
)
r.move(1, 1)
r.scale(3)
print(r.area()) #18




