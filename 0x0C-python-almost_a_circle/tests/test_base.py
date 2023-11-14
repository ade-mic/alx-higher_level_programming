from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    def TestPublicAttr(self):
        model = Base()
        self.assertEqual(model.id, 1) 