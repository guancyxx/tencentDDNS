import re

import requests


def sohu_soip(url="http://txt.go.sohu.com/ip/soip"):
    rs = requests.get(url)
    text = rs.text
    print(text)
    ip = re.findall(r'\d+.\d+.\d+.\d+', text)
    print(ip[0])
    return ip[0]
