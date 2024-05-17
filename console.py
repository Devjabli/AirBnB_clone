#!/usr/bin/python3
"""
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        """
        return True
    
    
    def help_quit(self, line):
        """
        """
        print("Quit command to exit the programm")

    def do_EOF(self, line):
        """
        """
        print()
        return True
    
    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()