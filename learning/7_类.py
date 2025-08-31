point.draw()
point.move()
point.get_distance(1, 2)

class Point:
    def draw(self):
        print("draw")

point = Point()
print(type(point))
print(isinstance(point, int))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.x)
point.draw(point)