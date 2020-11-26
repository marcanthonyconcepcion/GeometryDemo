from ThreeDimensionalShapes import Prism
from TwoDimensionalShapes import Circle

class Cylinder(Prism):
    def __init__(self, height, radius):
        super().__init__(base_shape=Circle(radius), height=height)
