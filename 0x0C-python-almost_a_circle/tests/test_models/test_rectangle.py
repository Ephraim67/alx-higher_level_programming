#!/usr/bin/python3
#test_rectangle.py
#Brennan D Baraban <375@holbertonschool.com>

"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 262
    TestRectangle_y - line 334
    TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
    TestRectangle_update_args - line 538
    TestRectangle_update_kwargs - line 676
    TestRectangle_to_dictionary - line 788
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaise(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_constructor_custom(self):
        """test initialization with custom value"""
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 100)

    def test_width_setter(self):
        """test changing initial width"""
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_height_setter(self):
        """test changing initial height"""
        rect = Rectangle(5, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_x_setter(self):
        """test changing initial x"""
        rect = Rectangle(5, 10)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_y_setter(self):
        """test changing initial y"""
        rect = Rectangle(5, 10)
        rect.y = 4
        self.assertEqual(rect.y, 4)

    def test_invalid_width_type(self):
        """testing for an invalid type"""
        with self.assertRaises(TypeError):
            Rectangle("betty", 5)

    def test_invalid_width_value(self):
        """testing for values <= 0"""
        with self.assertRaises(ValueError):
            Rectangle(-5, 3)

    def test_invalid_height_type(self):
        """test for inavlid width type"""
        with self.assertRaises(TypeError):
            Rectangle(5, "betty")

    def test_invalid_height_value(self):
        """testing for invalid width value"""
        with self.assertRaises(ValueError):
            Rectangle(5, -5)

    def test_invalid_x_type(self):
        """test for invalid x type"""
        with self.assertRaises(TypeError):
            Rectangle(5, 5, "betty")

    def test_invalid_x_value(self):
        """test for a negative x value"""
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -5)

    def test_invalid_y_type(self):
        """test for non int y value"""
        with self.assertRaises(TypeError):
            Rectangle(5, 5, 5, "betty")

    def test_invalid_y_value(self):
        """test for negative y value"""
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 5, -5)

    def test_area(self):
        """test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str_representation(self):
        """test the sring representation of a rectangle instance"""
        rect = Rectangle(5, 10, 2, 3, 100)
        expected_str = "[Rectangle] (100) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_str_represntation_default(self):
        """test string representaion with default values"""
        rect = Rectangle(5, 10)
        expected_str = "[Rectangle] (15) 0/0 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def setUp(self):
        """Redirect stdout to capture printed output"""
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        """Restore stdout after each test"""
        sys.stdout = sys.__stdout__

    def test_display(self):
        """Test the display method"""
        rect = Rectangle(3, 2)
        rect.display()
        expected_output = "###\n###\n\n"
        self.assertEqual(self.stdout.getvalue(), expected_output)

    def test_display_with_position(self):
        """Test the display method with position"""
        rect = Rectangle(3, 2, 2, 1)
        rect.display()
        expected_output = "\n  ###\n  ###\n\n"
        self.assertEqual(self.stdout.getvalue(), expected_output)

    def test_update_with_args(self):
        """Test updating attributes with arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_update_with_fewer_args(self):
        """Test updating with fewer arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_with_more_args(self):
        """Test updating with more arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50, 60, 70)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_update_with_no_args(self):
        """Test updating with no arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update()
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_with_kwargs(self):
        """test method with key worded arguments"""
        rect = Rectangle(1, 2, 3, 5, 6)
        rect.update(id=2, width=25, height=35, x=45, y=55)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 25)
        self.assertEqual(rect.height, 35)
        self.assertEqual(rect.x, 45)
        self.assertEqual(rect.y, 55)


if __name__ == "__main__":
    unittest.main()

