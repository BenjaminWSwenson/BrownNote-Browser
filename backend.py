import requests
from requests.exceptions import ConnectionError


def request_html_https(url):

    if url[:3] == 'http':
        pass
    else:
        url = 'https://'+ url

    try:
        r = requests.get(url)
        # r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
        return err
    finally:
        return r
