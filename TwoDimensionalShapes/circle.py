__author__ = "Marc Concepcion"
__copyright__ = "Copyright 2021, Marc Concepcion"
__credits__ = ["Marc Concepcion"]
__maintainer__ = "Marc Concepcion"
__email__ = "marcanthonyconcepcion@gmail.com"
__status__ = "Demo"

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
