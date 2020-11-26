from ThreeDimensionalShapes import RectangularPrism

class Cube(RectangularPrism):
    def __init__(self, side):
        super().__init__(length=side, width=side, height=side)
