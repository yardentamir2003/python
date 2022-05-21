import json
import ssl
import urllib
import urllib.request


def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = "https://goquotes-api.herokuapp.com/api/v1/random?count=10"
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
    quotes = json_dict["quotes"]
    for item in quotes:
        print(item["text"])


main()
