#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
print: Error code: followed by the HTTP status code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            responseText = resp.read().decode("utf-8")
            print(responseText)
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
