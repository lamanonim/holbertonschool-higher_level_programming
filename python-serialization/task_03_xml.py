#!/usr/bin/python3
"""Module for XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to XML and saves to file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Reads XML file and returns a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
