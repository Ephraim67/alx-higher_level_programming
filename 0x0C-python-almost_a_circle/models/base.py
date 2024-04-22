#!/usr/bin/python3
"""Classes that manage id attribute in all classes to avoid duplicate"""
import os
import json


class Base:
    """
    Base class for managing id attributes in all future classes

    Attributes:
         __nb_objects (int): Private class attribute to keep track of 
         the number of objects created

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing the base instance.

        Args:
            id (int, optional): The id value to assign to the instance.
                If None, a unique id will be generated.

        Note:
            If id is not provided, the instance will be assigned a unique
            id value based on the number of objects created.

        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
