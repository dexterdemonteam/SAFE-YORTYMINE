import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0 Safari/537.36"
)

_COOKIES = {}


def set_cookies(cookie_str):
    global _COOKIES
    _COOKIES = {}
    if not cookie_str:
        return
    for pair in cookie_str.split(";"):
        if "=" in pair:
            k, v = pair.strip().split("=", 1)
            _COOKIES[k] = v


def get(url, timeout=10, allow_redirects=True):
    headers = {"User-Agent": UA, "Accept": "*/*"}
    return requests.get(
        url,
        headers=headers,
        cookies=_COOKIES,
        timeout=timeout,
        verify=False,
        allow_redirects=allow_redirects,
    )


def head(url, timeout=10):
    headers = {"User-Agent": UA}
    return requests.head(
        url,
        headers=headers,
        cookies=_COOKIES,
        timeout=timeout,
        verify=False,
        allow_redirects=True,
    )
