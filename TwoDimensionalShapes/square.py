from TwoDimensionalShapes import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(length=side,width=side)
