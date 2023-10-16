#!/usr/bin/python3
"""
Entry point for console application
"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class to run console and execute given commands

        Attributes:
            __all_classes (tuple): all available obj classes to use in commands
    """

    __all_classes = ("BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review")

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
        elif line not in HBNBCommand.__all_classes:
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
        elif args[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif obj_key not in storage.all().keys():
            print("** no instance found **")
        else:
            ob_dict = storage.all()[obj_key]
            old_inst = eval(f"{args[0]}(**ob_dict)")
            print(str(old_inst))

    def do_destroy(self, line):
        """Delete an instance of an object

            Args:
                line: arguments to delete
        """
        args = line.split(' ')
        obj_key = ".".join(args[:2])
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__all_classes:
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
        elif args[0] not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        else:
            class_only_objs = [str(eval(f"{v['__class__']}(**v)"))
                               for v in storage.all().values()
                               if v["__class__"] == args[0]]
            print(f"{class_only_objs}")

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
        elif args[0] not in HBNBCommand.__all_classes:
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
            obj_dict[args[2]] = new_attr_val
            storage.save()

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

    def do_BaseModel(self, line):
        """apart of dot notation commands

            Args:
                line: args to command starting at .
        """
        args = line.split(' ')
        p_cmd = args[0][1:-1]
        p_cmd = p_cmd.split('(')
        if args[0] == ".all()":
            HBNBCommand.all_cls_cmd("BaseModel")
        elif args[0] == ".count()":
            HBNBCommand.count_cls_cmd("BaseModel")
        elif p_cmd[0] == "show":
            HBNBCommand.show_cls_cmd("BaseModel", p_cmd)
        elif p_cmd[0] == "destroy":
            HBNBCommand.destroy_cls_cmd("BaseModel", p_cmd)
        elif p_cmd[0] == "update":
            HBNBCommand.update_cls_cmd("BaseModel", args)

    def do_User(self, line):
        """apart of dot notation commands

            Args:
                line: args to command starting at .
        """
        args = line.split(' ')
        p_cmd = args[0][1:-1]
        p_cmd = p_cmd.split('(')
        if args[0] == ".all()":
            HBNBCommand.all_cls_cmd("User")
        elif args[0] == ".count()":
            HBNBCommand.count_cls_cmd("User")
        elif p_cmd[0] == "show":
            HBNBCommand.show_cls_cmd("User", p_cmd)
        elif p_cmd[0] == "destroy":
            HBNBCommand.destroy_cls_cmd("User", p_cmd)
        elif p_cmd[0] == "update":
            HBNBCommand.update_cls_cmd("User", args)

    def do_Amenity(self, line):
        """apart of dot notation commands

            Args:
                line: args to command starting at .
        """
        args = line.split(' ')
        p_cmd = args[0][1:-1]
        p_cmd = p_cmd.split('(')
        if args[0] == ".all()":
            HBNBCommand.all_cls_cmd("Amenity")
        elif args[0] == ".count()":
            HBNBCommand.count_cls_cmd("Amenity")
        elif p_cmd[0] == "show":
            HBNBCommand.show_cls_cmd("Amenity", p_cmd)
        elif p_cmd[0] == "destroy":
            HBNBCommand.destroy_cls_cmd("Amenity", p_cmd)
        elif p_cmd[0] == "update":
            HBNBCommand.update_cls_cmd("Amenity", args)

    def do_City(self, line):
        """apart of dot notation commands

            Args:
                line: args to command starting at .
        """
        args = line.split(' ')
        p_cmd = args[0][1:]
        p_cmd = p_cmd.split('(')
        if args[0] == ".all()":
            HBNBCommand.all_cls_cmd("City")
        elif args[0] == ".count()":
            HBNBCommand.count_cls_cmd("City")
        elif p_cmd[0] == "show":
            HBNBCommand.show_cls_cmd("City", p_cmd)
        elif p_cmd[0] == "destroy":
            HBNBCommand.destroy_cls_cmd("City", p_cmd)
        elif p_cmd[0] == "update":
            HBNBCommand.update_cls_cmd("City", args)

    def do_Place(self, line):
        """apart of dot notation commands

            Args:
                line: args to command starting at .
        """
        args = line.split(' ')
        p_cmd = args[0][1:]
        p_cmd = p_cmd.split('(')
        if args[0] == ".all()":
            HBNBCommand.all_cls_cmd("Place")
        elif args[0] == ".count()":
            HBNBCommand.count_cls_cmd("Place")
        elif p_cmd[0] == "show":
            HBNBCommand.show_cls_cmd("Place", p_cmd)
        elif p_cmd[0] == "destroy":
            HBNBCommand.destroy_cls_cmd("Place", p_cmd)
        elif p_cmd[0] == "update":
            HBNBCommand.update_cls_cmd("Place", args)

    def do_State(self, line):
        """apart of dot notation commands

            Args:
                line: args to command starting at .
        """
        args = line.split(' ')
        p_cmd = args[0][1:]
        p_cmd = p_cmd.split('(')
        if args[0] == ".all()":
            HBNBCommand.all_cls_cmd("State")
        elif args[0] == ".count()":
            HBNBCommand.count_cls_cmd("State")
        elif p_cmd[0] == "show":
            HBNBCommand.show_cls_cmd("State", p_cmd)
        elif p_cmd[0] == "destroy":
            HBNBCommand.destroy_cls_cmd("State", p_cmd)
        elif p_cmd[0] == "update":
            HBNBCommand.update_cls_cmd("State", args)

    def do_Review(self, line):
        """apart of dot notation commands

            Args:
                line: args to command starting at .
        """
        args = line.split(' ')
        p_cmd = args[0][1:]
        p_cmd = p_cmd.split('(')
        if args[0] == ".all()":
            HBNBCommand.all_cls_cmd("Review")
        elif args[0] == ".count()":
            HBNBCommand.count_cls_cmd("Review")
        elif p_cmd[0] == "show":
            HBNBCommand.show_cls_cmd("Review", p_cmd)
        elif p_cmd[0] == "destroy":
            HBNBCommand.destroy_cls_cmd("Review", p_cmd)
        elif p_cmd[0] == "update":
            HBNBCommand.update_cls_cmd("Review", args)

    @staticmethod
    def all_cls_cmd(name):
        """print list of all saved objects of class name

            Args:
                name: name of class to find
        """
        objs = storage.all()
        obj_list = [str(eval(f"{v['__class__']}(**v)"))
                    for v in objs.values()
                    if v["__class__"] == name]
        print(obj_list)

    @staticmethod
    def count_cls_cmd(name):
        """count how many instances of a class are saved

            Args:
                name: name of class to count
        """
        num = 0
        objs = storage.all()
        for v in objs.values():
            if v["__class__"] == name:
                num += 1
        print(num)

    @staticmethod
    def show_cls_cmd(name, args):
        """the show command with dot notation

            Args:
                name: calling class name
                args: the id of instance
        """
        key = ''
        if len(args) >= 2:
            key = name + '.' + args[1]

        if len(args) < 2:
            print("** instance id missing **")
        elif key not in storage.all().keys():
            print("** no instance found **")
        else:
            ob_dict = storage.all()[key]
            old_inst = eval(f"{name}(**ob_dict)")
            print(str(old_inst))

    @staticmethod
    def destroy_cls_cmd(name, args):
        """the destroy command with dot notation

            Args:
                name: calling class name
                args: list of args or id
        """
        key = ''
        if len(args) >= 2:
            key = name + '.' + args[1]

        if len(args) < 2:
            print("** instance id missing **")
        elif key not in storage.all().keys():
            print("** no instance found **")
        else:
            objs = storage.all()
            del objs[key]
            storage.save()

    @staticmethod
    def update_cls_cmd(name, args):
        """update class cmd with dot notation

            Args:
                name: name of class to run cmd on
                args: args to cmd for class
        """
        p_cmd = args[0].split('(')
        args[0] = p_cmd[1]
        args = [i.strip(',') for i in args]
        if len(args) >= 3:
            args[2] = args[2][:-1]

        if len(args) < 1:
            print("** no instance found **")
        elif len(args) < 2:
            print("** attribute name missing **")
        elif len(args) < 3:
            print("** value missing **")
        else:
            key = ".".join((name, args[0]))
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                inst = storage.all()[key]
                val = HBNBCommand.to_cast(args[2])
                inst[args[1]] = val
                storage.save()


HBNBCommand.prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
