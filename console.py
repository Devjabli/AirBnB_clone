#!/usr/bin/python3

""" Defines HBnB console class that serve project CRUD method. """

import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class HBNBCommand(cmd.Cmd):
    """
        Defining a command interpreter.
        Attributes:
            prompt (str): command prompt.
    """


    prompt = "(hbnb) "

    vl_classes = {
        "BaseModel": BaseModel, 
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
        }

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
    
    def parse_arguments(self, line):
        """
        Custom argument parser to split input line into arguments.

        Args:
            line (str): input line
        """
        return line.split()

    def do_create(self, line):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        
        Args:
            line (str): input line containing the class name.
        """
        commands = self.parse_arguments(line)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.vl_classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.vl_classes[commands[0]]()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = self.parse_arguments(line)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.vl_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = self.parse_arguments(line)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.vl_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{commands[0]}.{commands[1]}"
            if key in objects:
                del objects[key]
                storage.save()
                print(f"Instance {key} deleted")
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print the string representation of all instances or a specific class.
        Usage: all [<class_name>]
        """
        commands = self.parse_arguments(line)
        objects = storage.all()

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.vl_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = self.parse_arguments(line)
        attr_base = ["id", "created_at", "updated_at"]

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.vl_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_key = f"{args[0]}.{args[1]}"
        objects = storage.all()

        if instance_key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        if args[2] not in attr_base:
            instance = objects[instance_key]
            setattr(instance, args[2], args[3])
            instance.updated_at = datetime.now()
            instance.save()

    def do_count(self, class_name):
        """Count number of instances class"""

        if class_name not in self.vl_classes:
            print(" ** class doesn't exist ** ")
            return
        length = sum(1 for key in storage.all() if key.startswith(class_name + '.'))
        print(length)

    def default(self, line):
        """
        Handling default ALL COUNT command.
        """
        if "." in line:
            class_name, method_name = line.split(".")
            method_name = method_name.split("(")[0]
            if class_name in self.vl_classes:
                if method_name == "all":
                    self.do_all(class_name)
                elif method_name == "count":
                    self.do_count(class_name)
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
