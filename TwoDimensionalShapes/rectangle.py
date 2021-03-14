from typing import Union
from GeometricFigures import TwoDimensionalShape


class Rectangle(TwoDimensionalShape):
    def __init__(self, length: Union[int,float], width: Union[int,float]):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2*self.length + 2*self.width
