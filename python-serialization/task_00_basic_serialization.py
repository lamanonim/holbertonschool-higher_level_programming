#!/usr/bin/python3
"""Module for basic serialization."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes data and saves to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes data from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
