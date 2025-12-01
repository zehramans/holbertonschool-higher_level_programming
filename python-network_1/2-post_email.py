#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
"""we need to first parse the data as a header and urlencode it
then insert it into the response"""

if len(sys.argv) < 2:
    print()

else:
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data=data) as res:
        print(res.read().decode('utf-8'))
