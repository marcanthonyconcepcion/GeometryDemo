from typing import Union
from TwoDimensionalShapes import Rectangle


class Square(Rectangle):
    def __init__(self, side: Union[int,float]):
        super().__init__(length=side,width=side)
