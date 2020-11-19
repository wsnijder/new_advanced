class Point:
    """
    Point class represents and manipiulates x, y coordinates.
    """
    def __init__(self, x=0, y=0): # when you give coordinates it performs, otherwise (0,0)
        """Create a new point at the origin"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)  #Make it look like a coordinate

    def distance_from_origin(self): #using Pythagoras = wortel x kwadraat + y kwadraat
        distance = (self.x * self.x + self.y * self.y) ** 0.5
        return distance
