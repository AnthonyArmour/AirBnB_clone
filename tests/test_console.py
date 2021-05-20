#!/usr/bin/python3
"""Module for unittesting the console"""


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

    with patch('sys.stdout', new=StringIO()) as f:
        def Test_help_show(self, f):
            HBNBCommand().onecmd("help show")
