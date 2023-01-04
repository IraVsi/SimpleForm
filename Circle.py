from math import pi

#  peab olema 2 tühi rida
class Circle:

    def __init__(self, radius):
        """ Loo klass koos raadiusega """
        # print('Objekt created')
        self.radius = radius

    def get_radius(self):
        # print('Return radius')
        # Not needed method
        return self.radius

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        # pi + pow(self.radius, 2) # import pow
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius
