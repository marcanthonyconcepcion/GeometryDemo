__author__ = "Marc Concepcion"
__copyright__ = "Copyright 2021, Marc Concepcion"
__credits__ = ["Marc Concepcion"]
__maintainer__ = "Marc Concepcion"
__email__ = "marcanthonyconcepcion@gmail.com"
__status__ = "Demo"

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
