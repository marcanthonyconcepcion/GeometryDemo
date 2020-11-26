import math
from GeometricFigures import ThreeDimensionalShape

class Sphere(ThreeDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def get_volume(self):
        return 4*math.pi*pow(self.radius,3)/3

    def get_surface_area(self):
        return 4*math.pi*pow(self.radius,2)
