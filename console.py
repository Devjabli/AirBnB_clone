#!/usr/bin/python3

"""
Defines HBnB console class that serve project CRUD method.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Defining a command interpreter.
    Attributes:
        prompt (str): command prompt.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, line):
        """
        Quit commant exit the programm

        Args:
            line (str): input line
        """
        return True

    def do_EOF(self, line): # pylint: disable=invalid-name
        """
        EOF signal to exit the program.

        Args:
            line (str): input line
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
