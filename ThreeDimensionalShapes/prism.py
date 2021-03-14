from GeometricFigures import ThreeDimensionalShape


class Prism(ThreeDimensionalShape):
    def __init__(self, height, base_shape):
        self.height = height
        self.base_shape = base_shape

    def get_volume(self):
        return self.height * self.base_shape.get_area()

    def get_surface_area(self):
        return 2 * self.base_shape.get_area() + self.height * self.base_shape.get_perimeter()
