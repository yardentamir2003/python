import json
import ssl
import urllib
import urllib.request


def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = "http://api.weatherapi.com/v1/current.json?key=49a7cc862231419489a144556220605&q=Israel&aqi=no"
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
    current = json_dict["current"]
    location = json_dict["location"]
    temptature = current["temp_c"]
    location_name = location["name"]
    print("the temprature in {} is {} degrees.".format(location_name, temptature))


main()