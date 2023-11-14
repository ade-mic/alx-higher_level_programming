#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
    def TestClassInit(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
    
    def TestGetters(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def TestGetters(self):
        r1 = Rectangle(10, 2)
        r2 =  Rectangle(10, 2, 2, 4, 12)
        self.assertEqual(r1.width(8), r1.width)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r2.x(8), r1.x)
        self.assertEqual(r2.y(8), r1.y)


if __name__ == '__main__':
    unittest.main()