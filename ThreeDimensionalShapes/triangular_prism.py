from typing import Union
from ThreeDimensionalShapes import Prism
from TwoDimensionalShapes import Triangle


class TriangularPrism(Prism):
    def __init__(self, prism_height: Union[int,float], a: Union[int,float], b: Union[int,float], c: Union[int,float]):
        super().__init__(height=prism_height, base_shape=Triangle(b=b, c=c, a=a))
