#!/usr/bin/python3
"""
This is a test file for the class base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test ceses for class Base
    """
    def test_create(self):
        """
        Test the instantiation of class Base
        """
        b1 =  Base()
        self.assertEqual(b1.id, 1)

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
    
    def test_to_json_string(self):
        """
        Test the to_json_string method of the Base class
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}, {"id": 2}]), '[{"id": 1}, {"id": 2}]')
        self.assertEqual(Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()]), '[{"id": 1}, {"id": 12}]')

    def test_to_json_string(self):
            """
            Test the to_json_string method of the Base class
            """
            b1 = Base()
            b2 = Base(12)
            b3 = Base()
            self.assertEqual(Base.to_json_string(None), "[]")
            self.assertEqual(Base.to_json_string([]), "[]")
            self.assertEqual(Base.to_json_string([{"id": 1}, {"id": 2}]), '[{"id": 1}, {"id": 2}]')
            self.assertEqual(Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()]), '[{"id": 1}, {"id": 12}]')

    def test_from_json_string(self):
        """
        Test the from_json_string method of the Base class
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'), [{"id": 1}, {"id": 2}])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 12}]'), [{"id": 1}, {"id": 12}])

    def test_load_from_file(self):
        """
        Test the load_from_file method of the Base class
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        Base.save_to_file([b1, b2])
        self.assertEqual(Base.load_from_file(), [b1, b2])
        Base.save_to_file(None)
        self.assertEqual(Base.load_from_file(), [])
        Base.save_to_file([])
        self.assertEqual(Base.load_from_file(), [])
        Base.save_to_file([b1.to_dictionary(), b2.to_dictionary()])
        self.assertEqual(Base.load_from_file(), [b1, b2])

if __name__ == '__main__':
    unittest.main()