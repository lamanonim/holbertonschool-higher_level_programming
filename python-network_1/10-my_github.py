#!/usr/bin/python3
"""
This script takes GitHub credentials and uses the GitHub API
to display the user's id using Basic Authentication.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get(
        'https://api.github.com/user',
        auth=(username, token)
    )
    print(response.json().get('id'))
