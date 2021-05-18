#!/usr/bin/python3
"""A module for unittests for the file storage class"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


fs = FileStorage()


class TestBaseModel(unittest.TestCase):
    """A class to test FileStorage"""

    def test_filestorage_reload(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        dic = fs._FileStorage__objects
        bm1.my_number = 89
        self.assertEqual(bm1.my_number, 89)
        fs.reload()
        self.assertEqual(dic, fs._FileStorage__objects)

    def test_filestorage_save(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        self.assertNotEqual(os.path.getsize(fs._FileStorage__file_path), 0)

    def test_filestorage_new(self):
        bm1 = BaseModel()
        self.assertNotEqual(len(fs._FileStorage__objects), 0)

    def test_filestorage_all(self):
        bm1 = BaseModel()
        self.assertIsInstance(fs.all(), dict)

    def test_filestorage_objects(self):
        bm1 = BaseModel()
        self.assertIsInstance(fs._FileStorage__objects, dict)

    def test_file_exists(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        self.assertTrue(os.path.exists(fs._FileStorage__file_path))

if __name__ == '__main__':
    unittest.main()
