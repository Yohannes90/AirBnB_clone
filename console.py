#!/usr/bin/python3
"""
Entry point for console application
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class to run console and execute given commands"""

    def do_quit(self, line):
        """command to quit the console"""
        return True

    def do_EOF(self, line):
        """Command to handle EOF or ctrl + d, same as quit"""
        return True

    def emptyline(self):
        """prevent previous command execution, print prompt"""
        pass

    def do_create(self, line):
        """Create an instance of an object

            Args:
                line: argument to command, should be instance class name
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            ob = eval(line)()
            print(f"{ob.id}")
            ob.save()

    def do_show(self, line):
        """show the requested object

            Args:
                line: the class name and id of requested object instance
        """
        args = line.split(' ')
        obj_key = ".".join(args[:2])
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif obj_key not in storage.all().keys():
            print("** no instance found **")
        else:
            print(f"object key in dict: {obj_key}, string repr: {str(storage.all()[obj_key])}")

    def do_all(self, line):
        """print all instances available
            
            Args:
                line: class of objects to print
        """
        ob_inst_list = []
        if len(line) < 1:
            print("all reps here")
        elif line not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            print("selected class only")


if __name__ == '__main__':
    HBNBCommand.prompt = "(hbnb)"
    HBNBCommand().cmdloop()
