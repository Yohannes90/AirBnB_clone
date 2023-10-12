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

    def do_all(self, line):
        """print all instances available
            
            Args:
                line: class of objects to print
        """
        ob_inst_list = []
        if len(line) < 1:
            for v in storage.all().values():
                ob_inst_list.append(str(v))
            print(ob_inst_list)
        elif line not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            for v in storage.all().values():
                if line in v.values():
                    tmp_ob = eval(v["__class__"])()
                    ob_inst_list.append(str(tmp_ob))
            print(ob_inst_list)


if __name__ == '__main__':
    HBNBCommand.prompt = "(hbnb)"
    HBNBCommand().cmdloop()
