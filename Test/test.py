import ssl
import urllib.request

context = ssl._create_unverified_context()

url = 'https://www.naver.com'
html = urllib.request.urlopen(url, context=context)
print(html.read())

