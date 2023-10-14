#!/usr/bin/python3
"""
Entry point for console application
"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
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
        elif line not in ["BaseModel", "User"]:
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
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif obj_key not in storage.all().keys():
            print("** no instance found **")
        else:
            ob_dict = storage.all()[obj_key]
            old_inst = eval(f"{args[0]}(**ob_dict)")
            print(str(old_inst))

    def do_delete(self, line):
        """Delete an instance of an object

            Args:
                line: arguments to delete (requires classname and object id)
        """
        args = line.split(' ')
        obj_key = ".".join(args[:2])
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif obj_key not in storage.all().keys():
            print("** no instance found **")
        else:
            all_obj = storage.all()
            del all_obj[obj_key]
            storage.save()

    def do_all(self, line):
        """print all instances available

            Args:
                line: class of objects to print or nothing to print all objects
        """
        args = line.split(' ')
        if len(line) == 0:
            all_objs = [str(eval(f"{v['__class__']}(**v)"))
                        for v in storage.all().values()]
            print(f"{all_objs}")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            class_only_objs = [str(eval(f"{v['__class__']}(**v)"))
                               for v in storage.all().values()
                               if v["__class__"] == args[0]]
            print(f"{class_only_objs}")

    """@staticmethod
    def to_cast(attr_val):
        cast new attribute value correctly

            Args:
                attr_val: the value to cast (str, int, float)

        if attr_val[0] == '"' and attr_val[-1] == '"':
            return str(attr_val)
        if '.' in attr_val:
            return float(attr_val)
        return int(attr_val)"""

    def do_update(self, line):
        """update an instance attribute or add new attribute

            Args:
                line: class and id of inst to upd then attr name and attr val

            Usage: update <class name> <id> <attr name> '<attr value>'
        """
        args = line.split(' ')
        obj_key = ".".join(args[:2])
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif obj_key not in storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_dict = storage.all()[obj_key]
            new_attr_val = HBNBCommand.to_cast(args[3])
            new_attr_key = args[2]
            obj_dict.update((new_attr_key, new_attr_val))

    @staticmethod
    def to_cast(attr_val):
        """cast new attr value correctly

            Args:
                attr_val: value to cast
        """
        if attr_val[0] == '"' and attr_val[-1] == '"':
            attr_val = attr_val.strip('"')
            return str(attr_val)
        if '.' in attr_val:
            return float(attr_val)
        return int(attr_val)


HBNBCommand.prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
