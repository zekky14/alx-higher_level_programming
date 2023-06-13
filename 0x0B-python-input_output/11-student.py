#!/usr/bin/python3
"""Defines a class Student."""

class Student:
     """Represent a student."""
    def __init__(self, first_name, last_name, age):
       """Initialize a new Student.
	Args:
	first_name (str): The first name of the student. 
	last name (str): The last name of the student. 
	age (int): The age of the student.
      """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        if attr is a list of strings, represents only those attributes
        included in the list.
        Args:
           attr (list): (optional) the attributes to represent.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student.      
        for key, value in json.items():
            setattr(self, key, value)
