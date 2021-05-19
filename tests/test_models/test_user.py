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
        self.assertNotEqual(u1.email, "")

    def test_password(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.password = "blah"
        self.assertNotEqual(u1.password, "")

    def test_first_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.first_name = "blah"
        self.assertNotEqual(u1.first_name, "")

    def test_last_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = User()
        u1.last_name = "blah"
        self.assertNotEqual(u1.last_name, "")

    if __name__ == '__main__':
        unittest.main()
