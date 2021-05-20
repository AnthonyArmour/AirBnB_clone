#!/usr/bin/python3
"""Module for unittesting the console"""


from io import StringIO
import sys
import unittest
from unittest.mock import patch
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from console import HBNBCommand


help_str = ("\nDocumented commands (type help <topic>):\n"
            "========================================\n"
            "EOF  all  create  destroy  help  quit  show  update\n\n")
help_all = ("syntax: all 'class name'\n"
            "-- prints the string representation of all instances by input class name\n")

fs = FileStorage()


class TestConsole(unittest.TestCase):
    """A class to test console"""

    def test_help(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue(), help_str)

    def test_emptyline(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

    def test_quit(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")

    def test_basemodel(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            bm_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(bm_id[:-1]))
            bm = f.getvalue()
        self.assertIn(bm_id[:-1], bm)
        HBNBCommand().onecmd("update BaseModel {} first_name 'John'".format(bm_id[:-1]))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("'John'", f.getvalue())
        HBNBCommand().onecmd("destroy BaseModel {}".format(bm_id[:-1]))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(bm_id[:-1]))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

if __name__ == '__main__':
        unittest.main()
