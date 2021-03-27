__author__ = "Marc Concepcion"
__copyright__ = "Copyright 2021, Marc Concepcion"
__credits__ = ["Marc Concepcion"]
__maintainer__ = "Marc Concepcion"
__email__ = "marcanthonyconcepcion@gmail.com"
__status__ = "Demo"

import math
from typing import Union
from GeometricFigures import ThreeDimensionalShape


class Sphere(ThreeDimensionalShape):
    def __init__(self, radius: Union[int,float]):
        self.radius = radius

    def get_volume(self):
        return 4*math.pi*pow(self.radius,3)/3

    def get_surface_area(self):
        return 4*math.pi*pow(self.radius,2)
