#!/usr/bin/python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError) as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            pickle.load(f)

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
