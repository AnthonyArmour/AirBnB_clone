#!/usr/bin/python3
"""A module for unittests for the base model class"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A class to test BaseModel"""

    def test_id_assignment(self):
        bm1 = BaseModel()
        self.assertNotEqual(bm1.id, "")

    def test_created_at_exists(self):
        bm1 = BaseModel()
        self.assertIsInstance(type(bm1.created_at), type(datetime))

    def test_updated_at_exists(self):
        bm1 = BaseModel()
        self.assertIsInstance(type(bm1.updated_at), type(datetime))

    def test_str_output(self):
        bm1 = BaseModel()
        self.assertNotEqual(bm1.__str__(), "")

    def test_save_method(self):
        bm1 = BaseModel()
        original = bm1.updated_at
        new = bm1.save()
        self.assertNotEqual(original, new)

    def test_to_dict_method(self):
        bm1 = BaseModel()
        my_dict = bm1.to_dict()
        self.assertIn("__class__", my_dict.keys())

if __name__ == '__main__':
    unittest.main()
