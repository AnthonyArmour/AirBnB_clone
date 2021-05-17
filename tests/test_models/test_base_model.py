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
        self.assertIn("BaseModel", bm1.__str__())
        self.assertIn(str(bm1.id), bm1.__str__())
        self.assertIn(str(bm1.__dict__), bm1.__str__())

    def test_save_method(self):
        bm1 = BaseModel()
        original = bm1.updated_at
        bm1.save()
        new = bm1.updated_at
        self.assertNotEqual(original, new)

    def test_to_dict_method(self):
        bm1 = BaseModel()
        my_dict = bm1.to_dict()
        self.assertIn("__class__", my_dict.keys())

    def test_init_kwargs(self):
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertEqual(type(bm2), type(bm1))
        self.assertIsNot(bm2, bm1)
        self.assertEqual(bm2.id, bm1.id)
        self.assertEqual(bm2.created_at, bm1.created_at)

    if __name__ == '__main__':
        unittest.main()
