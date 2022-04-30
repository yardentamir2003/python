import json
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "https://blogs.tapuz.co.il/wp-json/authorpost/v1/get_get_author_listing/?count=22"
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

response = urllib.request.urlopen(req)
body = response.read().decode('utf-8')
json_dict = json.loads(body)
data = json_dict.get("data")
for item in data:
    print(item)