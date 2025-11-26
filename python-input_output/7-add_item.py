#!/usr/bin/python3
"""elementleri python listine ordan filea"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"
"""deyrem ki ya existing listi ac yoxdusa yarat"""
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []
"""burda da deyrem ki cli argumentlerini yapisdir"""
my_list.extend(sys.argv[1:])
"""filei tezden yadda saxla"""
save_to_json_file(my_list, filename)
