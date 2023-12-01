#!/usr/bin/python3
"""
post request to server
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    payload = urllib.parse.urlencode(payload)
    payload = payload.encode('ascii')
    req = urllib.request.Request(url, payload)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
