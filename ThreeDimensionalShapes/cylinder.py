__author__ = "Marc Concepcion"
__copyright__ = "Copyright 2021, Marc Concepcion"
__credits__ = ["Marc Concepcion"]
__maintainer__ = "Marc Concepcion"
__email__ = "marcanthonyconcepcion@gmail.com"
__status__ = "Demo"

from typing import Union
from ThreeDimensionalShapes import Prism
from TwoDimensionalShapes import Circle


class Cylinder(Prism):
    def __init__(self, height: Union[int, float], radius: Union[int, float]):
        super().__init__(base_shape=Circle(radius), height=height)
