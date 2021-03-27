__author__ = "Marc Concepcion"
__copyright__ = "Copyright 2021, Marc Concepcion"
__credits__ = ["Marc Concepcion"]
__maintainer__ = "Marc Concepcion"
__email__ = "marcanthonyconcepcion@gmail.com"
__status__ = "Demo"

from typing import Union
from TwoDimensionalShapes import Rectangle
from ThreeDimensionalShapes import Prism


class RectangularPrism(Prism):
    def __init__(self, length: Union[int,float], width: Union[int,float], height: Union[int,float]):
        super().__init__(base_shape=Rectangle(length, width), height=height)
