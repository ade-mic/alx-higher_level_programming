import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangleAtrr(unittest.TestCase):
    def test_set_width(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.width = 'two'
        with self.assertRaises(ValueError):
            r.width = -1
        with self.assertRaises(ValueError):
            r.width = 0
        r.width = 4
        self.assertEqual(r.width, 4)
    
    def test_set_height(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.height = 'four'
        with self.assertRaises(ValueError):
            r.height = 0
            r.height = -1
        r.height = 5
        self.assertEqual(r.height, 5)
    
    def test_set_x(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.x = 'six'
        with self.assertRaises(ValueError):
            r.x = -6
        r.x = 0
        self.assertEqual(r.x, 0)
        r.x = 6
        self.assertEqual(r.x, 6)

    def test_set_y(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.y = 'six'
        with self.assertRaises(ValueError):
            r.y = -6
        r.y = 0
        self.assertEqual(r.y, 0)
        r.y = 6
        self.assertEqual(r.y, 6)
    
    def test_set_area(self):
        r = Rectangle(2, 4)
        r_area = r.area()
        self.assertEqual(r_area, 8)
        r2 = Rectangle(2, 10)
        r2_area = r2.area()
        self.assertEqual(r2_area, 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        r3_area = r3.area()
        self.assertEqual(r3_area, 56)
    
    def test_display(self):
        r = Rectangle(2, 3)
        expected_output = '##\n##\n##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display() 
            self.assertEqual(buffer.getvalue(), expected_output)
    
    