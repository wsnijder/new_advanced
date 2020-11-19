class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflect_x(self):
        negative_y = self.x, self.y * -1
        return negative_y

print(Point(3, 5).reflect_x())



