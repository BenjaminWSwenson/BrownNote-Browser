import requests


def request_html_https(url):
    if url[:7] == 'https://':
        return requests.get(url).text
    else:
        url = 'https://' + url
        return requests.get(url).text
