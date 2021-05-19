#!/usr/bin/python3
"""A module for unittests for the user class"""


import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage


fs = FileStorage()


class TestUser(unittest.TestCase):

    """class to test User"""

    def test_email(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.email = "blah"
        self.assertIsNot(u1.email, None)

    def test_password(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.password = "blah"
        self.assertIsNot(u1.password, None)

    def test_first_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.first_name = "blah"
        self.assertIsNot(u1.first_name, None)

    def test_last_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.last_name = "blah"
        self.assertIsNot(u1.last_name, None)

if __name__ == '__main__':
    unittest.main()
