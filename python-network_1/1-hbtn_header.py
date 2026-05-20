#!/usr/bin/python3
"""This script takes a URL, sends a request, and displays the X-Request-Id header value."""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
