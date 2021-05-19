#!/usr/bin/python3
"""A module for unittests for the user class"""



import unittest
import os
from models.user.py import User
from models.engine.file_storage import FileStorage


fs = FileStorage()


class TestUser(unittest.TestCase):
    """class to test User"""

    def test_email(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.email = "blah"
        self.assertIsInstance(u1.email, str)

    def test_password(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.password = "blah"
        self.assertIsInstance(u1.password, str)

    def test_first_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.first_name = "blah"
        self.assertIsInstance(u1.first_name, str)

    def test_last_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.last_name = "blah"
        self.assertIsInstance(u1.last_name, str)

    if __name__ == '__main__':
        unittest.main()
