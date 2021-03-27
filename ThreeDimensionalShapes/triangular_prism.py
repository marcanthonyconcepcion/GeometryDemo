__author__ = "Marc Concepcion"
__copyright__ = "Copyright 2021, Marc Concepcion"
__credits__ = ["Marc Concepcion"]
__maintainer__ = "Marc Concepcion"
__email__ = "marcanthonyconcepcion@gmail.com"
__status__ = "Demo"

from typing import Union
from ThreeDimensionalShapes import Prism
from TwoDimensionalShapes import Triangle


class TriangularPrism(Prism):
    def __init__(self, prism_height: Union[int,float], a: Union[int,float], b: Union[int,float], c: Union[int,float]):
        super().__init__(height=prism_height, base_shape=Triangle(b=b, c=c, a=a))
