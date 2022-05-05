import ssl
import urllib.request

from bs4 import BeautifulSoup


def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = "https://www.tapuz.co.il/"
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    response = urllib.request.urlopen(req)
    body = response.read().decode('utf-8')

    soup = BeautifulSoup(body, "html.parser")
    tags = soup('img')

    for i in range(6):
        image = tags[i]
        download_image(image['src'])


def download_image(src):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    if src.startswith("http"):
        url = src
    else:
        url = "https://www.tapuz.co.il{}".format(src)
    print(url)
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    response = urllib.request.urlopen(req)
    body = response.read()
    position = src.rfind("/")
    if "?" in src:
        questionmark_position = src.find("?")
        image_name = src[position + 1:questionmark_position]
    else:
        image_name = src[position + 1:]
    print(image_name)
    with open(image_name, "wb") as file:
        file.write(body)


main()
