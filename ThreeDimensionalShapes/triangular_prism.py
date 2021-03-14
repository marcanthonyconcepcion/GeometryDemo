from ThreeDimensionalShapes import Prism
from TwoDimensionalShapes import Triangle


class TriangularPrism(Prism):
    def __init__(self, prism_height, a, b, c):
        super().__init__(height=prism_height, base_shape=Triangle(b=b, c=c, a=a))
