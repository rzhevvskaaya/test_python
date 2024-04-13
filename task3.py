import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_another_point(self, another_point):
        return math.sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


# Пример использования программы
point1 = Point(2, 3)
point2 = Point(-2, 10)
print(point1.distance_to_another_point(point2))
print(point1.get_coordinates())
point2.set_coordinates(1, 9)
print(point2.get_coordinates())
