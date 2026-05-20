#!/usr/bin/python3
"""
This script takes a URL and an email address, sends a POST request
to the URL with the email as a parameter, and displays the body
of the response.
"""
import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
