# -*- coding:utf8 -*-
import base64
import hashlib
import hmac
import time
import random

import requests

def recordCreate(SecretID, SecretKey, domain, subDomain, recordType, recordLine, value, ttl=None, mx=None):
    api_domain = "cns.api.qcloud.com"

    api_path = "/v2/index.php"

    data = {
        "Action": "RecordCreate",
        "Region": "ap-shanghai",
        "SecretId": SecretID,
        "Timestamp": int(time.time()),
        "Nonce": random.randint(0, 999999),
        "SignatureMethod": "HmacSHA256",
        "domain": domain,
        "subDomain": subDomain,
        "recordType": recordType,
        "recordLine": recordLine,
        "value": value,
    }

    if ttl:
        data["ttl"] = ttl

    if mx:
        data["mx"] = mx

    if recordType == "MX" and not mx:
        data["mx"] = random.randint(0, 50)

    # 加密
    sorted_data = [(k, data[k]) for k in sorted(data.keys())]
    print(u"排序：", sorted_data)

    merge_data = "&".join([str(k) + "=" + str(v) for (k, v) in sorted_data])
    print(u"拼接", merge_data)

    merge_str = "GET" + api_domain + api_path + "?" + merge_data
    print(u"拼接签名原文", merge_str)

    j = hmac.new(SecretKey.encode("utf-8"), msg=merge_str.encode("utf-8"), digestmod=hashlib.sha256)
    print(j.digest())
    print(base64.b64encode(j.digest()))
    signature = str(base64.b64encode(j.digest())).strip('b').strip('\'')
    print(signature)

    data["Signature"] = signature

    rs = requests.get(url="https://" + api_domain + api_path, params=data)
    print(rs.url)
    print(rs, rs.text)

    return rs.json()
