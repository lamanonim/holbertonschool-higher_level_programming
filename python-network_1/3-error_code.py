#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL and displays
the body of the response decoded in utf-8.
Manages urllib.error.HTTPError exceptions and prints the error code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
