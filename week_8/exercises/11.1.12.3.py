class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        slopexy = (self.y-0) / (self.x-0)
        return slopexy

print(Point(4,10).slope_from_origin())