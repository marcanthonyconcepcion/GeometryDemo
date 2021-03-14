import unittest
import math
from unittest.mock import Mock
from GeometricFigures import ThreeDimensionalShape
from ThreeDimensionalShapes import Prism
from ThreeDimensionalShapes import RectangularPrism
from ThreeDimensionalShapes import Sphere
from ThreeDimensionalShapes import Cylinder
from ThreeDimensionalShapes import TriangularPrism
from ThreeDimensionalShapes import Cube

class TestThreeDimensionalShapes(unittest.TestCase):
    def test_prism(self):
        length = 40.2343
        width = 50
        height = 60
        base_rectangle_area = length * width
        base_rectangle_perimeter = 2 * (length + width)

        mock_base_shape = Mock()
        mock_base_shape.get_area.return_value = base_rectangle_area
        mock_base_shape.get_perimeter.return_value = base_rectangle_perimeter

        expected_volume = height*base_rectangle_area
        expected_surface_area = 2*base_rectangle_area + height*base_rectangle_perimeter

        prism = Prism(height=height, base_shape=mock_base_shape)
        self.assertTrue(isinstance(prism, ThreeDimensionalShape))
        self.assertEqual(expected_volume, prism.get_volume())
        self.assertEqual(expected_surface_area, prism.get_surface_area())

    def test_rectangular_prism(self):
        length = 10
        width = 20
        height = 30.3454
        base_rectangle_area = length*width
        base_rectangle_perimeter = 2*(length + width)

        expected_volume = height*base_rectangle_area
        expected_surface_area = 2*base_rectangle_area + height*base_rectangle_perimeter

        rectangular_prism = RectangularPrism(length=length, width=width, height=height)
        self.assertTrue(isinstance(rectangular_prism, ThreeDimensionalShape))
        self.assertEqual(expected_volume, rectangular_prism.get_volume())
        self.assertEqual(expected_surface_area, rectangular_prism.get_surface_area())

        expected_volume_direct = length*width*height
        expected_surface_area_direct = 2*(length*width + length*height +  width*height)
        self.assertEqual(expected_volume_direct, rectangular_prism.get_volume())
        self.assertEqual(expected_surface_area_direct, rectangular_prism.get_surface_area())

    def test_sphere(self):
        radius = 10
        expected_volume = 4*math.pi*pow(radius,3)/3
        expected_surface_area = 4*math.pi*pow(radius,2)

        sphere = Sphere(radius=radius)
        self.assertTrue(isinstance(sphere, ThreeDimensionalShape))
        self.assertEqual(expected_volume, sphere.get_volume())
        self.assertEqual(expected_surface_area, sphere.get_surface_area())

    def test_cylinder(self):
        radius = 10.3452
        height = 30

        base_circle_area = math.pi*pow(radius, 2)
        base_circle_perimeter = 2*math.pi*radius

        expected_volume = height*base_circle_area
        expected_surface_area = 2*base_circle_area + height*base_circle_perimeter

        cylinder = Cylinder(height=height, radius=radius)
        self.assertTrue(isinstance(cylinder, ThreeDimensionalShape))
        self.assertEqual(expected_volume, cylinder.get_volume())
        self.assertEqual(expected_surface_area, cylinder.get_surface_area())

        expected_volume_direct = math.pi*pow(radius,2)*height
        expected_surface_area_direct = 2*math.pi*radius*height + 2*math.pi*pow(radius,2)
        self.assertEqual(expected_volume_direct, cylinder.get_volume())
        self.assertEqual(expected_surface_area_direct, cylinder.get_surface_area())

    def test_triangular_prism(self):
        a = 20.2345
        b = 30.2345
        c = 40.2345
        prism_height = 30

        base_triangle_perimeter = a+b+c
        base_triangle_half_perimeter = base_triangle_perimeter/2
        base_triangle_area = math.sqrt(base_triangle_half_perimeter*(base_triangle_half_perimeter-a)*
                        (base_triangle_half_perimeter-b)*(base_triangle_half_perimeter-c))

        expected_volume = prism_height*base_triangle_area
        expected_surface_area = 2*base_triangle_area + prism_height*base_triangle_perimeter

        triangular_prism = TriangularPrism(prism_height=prism_height, a=a, c=c, b=b)
        self.assertTrue(isinstance(triangular_prism, ThreeDimensionalShape))
        self.assertEqual(expected_volume, triangular_prism.get_volume())
        self.assertEqual(expected_surface_area, triangular_prism.get_surface_area())

    def test_cube(self):
        side = 10
        base_square_area = pow(side,2)
        base_square_perimeter = 4*side

        expected_volume = side*base_square_area
        expected_surface_area = 2*base_square_area + side*base_square_perimeter

        cube = Cube(side=side)
        self.assertTrue(isinstance(cube, ThreeDimensionalShape))
        self.assertEqual(expected_volume, cube.get_volume())
        self.assertEqual(expected_surface_area, cube.get_surface_area())

        expected_volume_direct = math.pow(side,3)
        expected_surface_area_direct = 6*math.pow(side, 2)
        self.assertEqual(expected_volume_direct, cube.get_volume())
        self.assertEqual(expected_surface_area_direct, cube.get_surface_area())


if __name__ == '__main__':
    unittest.main()
