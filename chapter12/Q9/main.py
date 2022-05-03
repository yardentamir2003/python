import ssl
import urllib.request
import json
from datetime import datetime, timezone


def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = "http://worldtimeapi.org/api/timezone/Asia/Jerusalem"
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    response = urllib.request.urlopen(req)
    body = response.read().decode('utf-8')
    my_json = json.loads(body)
    server_time_utc = my_json["utc_datetime"]
    server_time_utc = datetime.fromisoformat(server_time_utc)
    local_time_utc = datetime.now(timezone.utc)
    diff = server_time_utc - local_time_utc
    print(diff.total_seconds())

main()