#!/usr/bin/python3
"""A module containing the HBNB cmd interpretor"""


import cmd
import string, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """A class:
        The class creates a console for updating the storage engine
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print("syntax: EOF")
        print("-- termintaes the HBNBCommand loop")

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- termintaes the HBNBCommand loop")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
