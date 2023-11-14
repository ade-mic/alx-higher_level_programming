import unittest
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
    
    def test_getter(self):
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

    def test_setter(self):
        r1 = Rectangle(10, 2)
        r2 =  Rectangle(10, 2, 2, 4, 12)
        r1.width = 8
        self.assertEqual(r1.width, 8)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 4)
        r2.x = 8
        self.assertEqual(8, r2.x)
        r2.y = 8
        self.assertEqual(8, r2.y)


if __name__ == '__main__':
    unittest.main()