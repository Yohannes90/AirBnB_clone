#!/usr/bin/python3
"""
The base module class which other classes will inherit from
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class to inherit from
    """

    def __init__(self, *args, **kwargs):
        """Initializes the object with id, creat_at, updated_at"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k in ["created_at", "updated_at"]:
                    self.__dict__[k] = datetime.strptime(v,
                            "%Y-%m-%dT%H:%M:%S.%f")
                    continue
                self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of object instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Update updated_at time of instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """dictionary representation of instance with class key added

            Return:
                turns datetime objects into strings and adds classname
        """
        keys = self.__dict__.keys()
        ob_inst = dict()
        ob_inst["__class__"] = self.__class__.__name__
        for k in keys:
            if k in ["updated_at", "created_at"]:
                ob_inst[k] = self.__dict__[k].isoformat()
                continue
            ob_inst[k] = self.__dict__[k]
        return ob_inst
