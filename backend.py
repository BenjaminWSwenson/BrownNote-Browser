import requests


def request_html_https(url):
    if url[:3] == 'http':
        return requests.get(url).text
    else:
        url_http = 'http://' + url
        url_https = 'https://' + url

        try:
            r = requests.get(url_https).text
        except:
            try:
                r = requests.get(url_http).text
            except:
                r = "Error: Page not Found"
    return r
