from typing import Union
from GeometricFigures import ThreeDimensionalShape
from GeometricFigures import TwoDimensionalShape


class Prism(ThreeDimensionalShape):
    def __init__(self, height: Union[int, float], base_shape: TwoDimensionalShape):
        self.height = height
        self.base_shape = base_shape

    def get_volume(self):
        return self.height * self.base_shape.get_area()

    def get_surface_area(self):
        return 2 * self.base_shape.get_area() + self.height * self.base_shape.get_perimeter()
