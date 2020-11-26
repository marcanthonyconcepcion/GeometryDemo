Marc Concepcion's Geometry Demo codes to demonstrate Test-Driven Development in Python

This is a simple Python code that contains classes that represent the geometric measurement properties of some well-known two-dimensional and three-dimensional shapes.

This demo generically classifies the shapes into:
1. Two-Dimensional Shapes
2. Three-Dimensional Shapes

For each of the Two-Dimensional Shape, its area and perimenter properties are defined.
For each of the Three-Dimensional Shape, its surface area and volume are defined.

Here are the two-dimensional shapes decribed by the project:
1. Circle*
2. Rectangle
3. Square
4. Triangle

* Please take note that I treat the circumference of a circle as its "perimeter" based from this statement from Wikipedia:
"The perimeter of a circle or ellipse is called its circumference."
Source: https://en.wikipedia.org/wiki/Perimeter

Here are the three-dimensional shapes described by the project:
1. Prism
1.1. Cube
1.2. Rectangular Prism
1.3. Triangular Prism
1.4. Cylinder**
2. Sphere

** Please take note that I treat Cylinder as a Prism based from this statement from Wikipedia:
"A solid circular cylinder can be seen as the limiting case of a n-gonal prism where n approaches infinity."
Source: https://en.wikipedia.org/wiki/Cylinder#Prisms

The objective of this project is to perform test-driven development to define each shape into production.
The test methods of the following test classes are created first before creating each of the shape classes for production.
1.	Test Three Dimensional Shapes
	1.1.	test_rectangular_prism() to create and test Rectangular Prism class and to further test Prism class.
	1.2.	test_sphere() to create and test Sphere class.
	1.3.	test_cylinder() to create and test Cylinder class and to further test Prism class.
	1.4.	test_triangular_prism() to create and test Triangular Prism class and to further test Prism base class.
	1.5.	test_cube() to create and test Cube class and to further test Prism base class.
2.	Test Two Dimensional Shapes
	2.1.	test_rectangle() to create and test Rectangle class.
	2.2.	test_circle() to create and test Circle class.
	2.3.	test_triangle() to create and test Triangle class.
	2.4.	test_invalid_triangle() to test if the measurement of the three sides would make a valid Triangle.
	2.5.	test_square() to create and test Square class.

While performing test driven development, here are some of the test-driven class design milestones:
1.	Two-dimensional shape are generically defined as an interface with contract methods get_area() and get_perimeter() for classes Circle, Square, Triangle and Rectangle to implement.
The interface enforces the IS-A relationship:
-	Circle is a Two-Dimensional Shape.
-	Square is a Two-Dimensional Shape.
-	Triangle is a Two-Dimensional Shape.
- Rectangle is a Two-Dimensional Shape.

2.	Three-dimensional shape are generically defined as an interface with contract methods get_volume() and get_surface_area() for classes Rectangular Prism, Triangular Prism, Cylinder, Cube and Sphere to implement.
The interface enforces these IS-A relationships:
-	Sphere is a Three-Dimensional Shape.
-	Cylinder is a Three-Dimensional Shape.
-	Cube is a Three-Dimensional Shape.
-	Rectangular Prism is a Three-Dimensional Shape.
-	Triangular Prism is a Three-Dimensional Shape.

3. Base class Prism is created where Cylinder, Rectangular Prism, Triangular Prism and Cube are its derived classes.
3.1. Each of these prisms (Cylinder, Rectangular Prism, Triangular Prism and Cube) can have its properties computed as such:
-	Volume = Height x Base Area
-	Surface Area = 2 x Base Area + Height x Base Perimeter
3.2. Therefore, the Prism has defined get_volume() and get_suface_area() methods which its derived class shall inherit from and use.
3.3. Thus, the Base Class Prism further defines these IS-A relationships:
-	Sphere is a Three-Dimensional Shape.
-	Prism is a Three-Dimensional Shape.
-	Cylinder is a Prism which is a Three-Dimensional Shape.
-	Cube is a Rectangular Prism which is a Prism which is a Three-Dimensional Shape.
-	Rectangular Prism is a Prism which is a Three-Dimensional Shape.
-	Triangular Prism is a Prism which is a Three-Dimensional Shape.

To run the two test classes, please pip install and run unittest Python module.
For more inquiries, please feel free to e-mail me at marcanthonyconcepcion@gmail.com.

Thank you.
