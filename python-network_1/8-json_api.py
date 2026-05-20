#!/usr/bin/python3
"""
This script takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
