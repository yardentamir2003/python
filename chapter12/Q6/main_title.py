from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "https://www.walla.co.il/"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# print the main title
tags = soup('h2')
print(tags[0])


