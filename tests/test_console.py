#!/usr/bin/python3
"""Module for unittesting the console"""


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
    """class for unittesting console"""

    @patch('sys.stdout', new_callable=io.StringIO)
    def Test_help_show(self, mock_stdout):
        HBNBCommand.do_quit("quit")
        self.assertNotEqual(mock_stdout.getvalue(), "Fail")

if __name__ == '__main__':
        unittest.main()
