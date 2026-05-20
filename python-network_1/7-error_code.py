#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL and displays
the body of the response. If the HTTP status code is >= 400,
prints Error code followed by the status code.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
