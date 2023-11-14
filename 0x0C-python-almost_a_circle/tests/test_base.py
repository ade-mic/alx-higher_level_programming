import unittest
from models.base import Base
class TestBase(unittest.TestCase):
    def test_id_assignment_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_id_assignment_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_assignment_mixed(self):
        obj1 = Base(id=10)
        obj3 = Base(id=20)
        self.assertEqual(obj1.id, 10)
        self.assertEqual(obj3.id, 20)

if __name__ == '__main__':
    unittest.main()