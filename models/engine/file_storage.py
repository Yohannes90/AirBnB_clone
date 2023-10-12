#!/usr/bin/python3
"""
Storage mechanism for data or instances
"""
import json


class FileStorage:
    """Class for file storage of data

        Attributes:
            __file_path (str): path to the JSON file
            __objects (dict): store each object
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """retrieve all instances and return private attr"""
        return FileStorage.__objects

    def new(self, obj):
        """set a new object in __objects attr

            Args:
                obj: an object to add to __objects attr
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """write __objects to file for storage"""
        to_save = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(to_save)

    def reload(self):
        """load file contents into __object"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                contents = f.read()
                check = json.loads(contents)
                FileStorage.__objects = check
        except FileNotFoundError:
            pass
