from typing import Union
from TwoDimensionalShapes import Rectangle
from ThreeDimensionalShapes import Prism


class RectangularPrism(Prism):
    def __init__(self, length: Union[int,float], width: Union[int,float], height: Union[int,float]):
        super().__init__(base_shape=Rectangle(length, width), height=height)
