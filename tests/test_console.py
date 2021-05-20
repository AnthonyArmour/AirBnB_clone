#!/usr/bin/python3
"""Module for unittesting the console"""


from io import StringIO
import io
import sys
import unittest
from unittest.mock import patch
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from console import HBNBCommand



class TestConsole(unittest.TestCase):
    """A class to test console"""

    def test_show_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help show")
                self.assertIsInstance(f.getvalue().strip(), str)
    def test_all_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help all")
                self.assertIsInstance(f.getvalue().strip(), str)
    def test_update_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help update")
                self.assertIsInstance(f.getvalue().strip(), str)
    def test_destroy_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help destroy")
                self.assertIsInstance(f.getvalue().strip(), str)
    def test_create_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help create")
                self.assertIsInstance(f.getvalue().strip(), str)

if __name__ == '__main__':
        unittest.main()
