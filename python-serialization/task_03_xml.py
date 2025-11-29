#!/usr/bin/python3
import xml.etree.ElementTree as ET
"""dict daxilindeki elementleri xmle cevirme ve ya tersine"""


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    """bir dene parent"""
    for k, v in dictionary.items():
        child = ET.SubElement(root, k)
        child.text = str(v)
    """birinci xmle subelement kimi  keyni elave et sonra ona valuenu"""
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for i in root:
        result[i.tag] = child.text

    return result
