import urllib.request # urllib 패키지의 request 모듈을 import

response = urllib.request.urlopen('http://www.google.com')
print(response.status)
print(response)
print(response.read())

import urllib.request as r
response = r.urlopen('http://www.google.com')
print(response.status)

from urllib.request import Request, urlopen
req = Request('http://www.google.com')
response = urlopen(req)
print(response.status)