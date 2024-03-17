#!/usr/bin/python3
""" To define FileStorage class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represents abstracted storage engine

    Attributes:
        __file_path (str):name of file to save objects to
        __objects (dict):dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return -> dictionary of instantiated objects in __objects

        If cls is specified, return -> dictionary of objects
        Otherwise, return -> _objects dictionary
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dct = {}
            for ka, vi in self.__objects.items():
                if type(vi) == cls:
                    cls_dct[ka] = vi
            return cls_dct
        return self.__objects

    def new(self, obj):
        """To set __objects obj with the key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """To serialize __objects to JSON file __file_path."""
        odct = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as fl:
            json.dump(odct, fl)

    def reload(self):
        """To deserialize JSON file __file_path to __objects, if exist"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as fl:
                for o in json.load(fl).values():
                    nm = o["__class__"]
                    del o["__class__"]
                    self.new(eval(nm)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """To delete given objct from __objects, if exist"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """To call reload method"""
        self.reload()
