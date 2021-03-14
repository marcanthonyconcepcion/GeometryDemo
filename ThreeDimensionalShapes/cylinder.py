from typing import Union
from ThreeDimensionalShapes import Prism
from TwoDimensionalShapes import Circle


class Cylinder(Prism):
    def __init__(self, height: Union[int, float], radius: Union[int, float]):
        super().__init__(base_shape=Circle(radius), height=height)
