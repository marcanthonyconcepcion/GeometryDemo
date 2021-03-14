import math
from typing import Union
from GeometricFigures import TwoDimensionalShape


class Circle(TwoDimensionalShape):
    def __init__(self, radius: Union[int,float]):
        self.radius = radius

    def get_area(self):
        return math.pi*pow(self.radius, 2)

    def get_perimeter(self):
        return 2*math.pi*self.radius
