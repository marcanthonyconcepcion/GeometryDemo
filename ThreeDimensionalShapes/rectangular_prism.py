from TwoDimensionalShapes import Rectangle
from ThreeDimensionalShapes import Prism

class RectangularPrism(Prism):
    def __init__(self, length, width, height):
        super().__init__(base_shape=Rectangle(length, width), height=height)
