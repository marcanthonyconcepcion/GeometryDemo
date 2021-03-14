from typing import Union
from ThreeDimensionalShapes import RectangularPrism


class Cube(RectangularPrism):
    def __init__(self, side: Union[int, float]):
        super().__init__(length=side, width=side, height=side)
