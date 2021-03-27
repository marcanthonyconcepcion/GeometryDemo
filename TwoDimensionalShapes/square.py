__author__ = "Marc Concepcion"
__copyright__ = "Copyright 2021, Marc Concepcion"
__credits__ = ["Marc Concepcion"]
__maintainer__ = "Marc Concepcion"
__email__ = "marcanthonyconcepcion@gmail.com"
__status__ = "Demo"

from typing import Union
from TwoDimensionalShapes import Rectangle


class Square(Rectangle):
    def __init__(self, side: Union[int,float]):
        super().__init__(length=side,width=side)
