#!/usr/bin/python3
"""dict representations again"""


class Student:
    """attrs nedi
   deyir ki normalda s = Student("Zehra", "salam", 122) bele
   birsey verirsen hamsini cixardir amma indi sene bele verilecek
   s.to_json(["first_name", "age"]) burda ancaq hansilari istiyirse onu ver
   hamsini tezden qaytarma"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """birinci bunu yaziriq ki list oldugunu yoxlasin"""
        if not isinstance(attrs, list):
            return self.__dict__.copy()
        """listin icindeki elementler hamisi strdirmi"""
        if not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__.copy()
        """ve ancaq istediklerini return ele"""
        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
