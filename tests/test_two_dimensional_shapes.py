import unittest
import math
from TwoDimensionalShapes import Rectangle
from TwoDimensionalShapes import Circle
from TwoDimensionalShapes import Triangle
from TwoDimensionalShapes import Square

class TestTwoDimensionalShapes(unittest.TestCase):
    def test_rectangle(self):
        length = 10
        width = 20

        expected_area = length*width
        expected_perimeter = 2*length + 2*width

        rectangle = Rectangle(length=length, width=width)
        self.assertEqual(expected_area, rectangle.get_area())
        self.assertEqual(expected_perimeter, rectangle.get_perimeter())

    def test_circle(self):
        radius = 10

        expected_perimeter = 2*math.pi*radius
        expected_area = math.pi*pow(radius,2)

        circle = Circle(radius=radius)
        self.assertEqual(expected_area, circle.get_area())
        self.assertEqual(expected_perimeter, circle.get_perimeter())

    def test_triangle(self):
        first_side = 70
        second_side = 100
        third_side = 50

        half_perimeter = (first_side + second_side + third_side)/2
        expected_area = math.sqrt(half_perimeter*(half_perimeter-first_side)*(half_perimeter-second_side)*(half_perimeter-third_side))
        expected_perimeter = first_side + second_side + third_side

        triangle = Triangle(a=first_side, b=second_side, c=third_side)
        self.assertEqual(expected_area, triangle.get_area())
        self.assertEqual(expected_perimeter, triangle.get_perimeter())

    def test_invalid_triangle(self):
        first_side = 10
        second_side = 20
        third_side = 30
        with self.assertRaises(Exception):
            Triangle(a=first_side, b=second_side, c=third_side)

    def test_square(self):
        side = 10

        expected_area = math.pow(side, 2)
        expected_perimeter = 4*side

        square = Square(side=side)
        self.assertEqual(expected_area, square.get_area())
        self.assertEqual(expected_perimeter, square.get_perimeter())

if __name__ == '__main__':
    unittest.main()
