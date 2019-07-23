# -*- coding:utf8 -*-
import json
import os
import time

from apscheduler.schedulers.blocking import BlockingScheduler

from tencentAPI.domainNameResolutionRecord import recordCreate
from utils.getPublicNetworkIP import sohu_soip
from apscheduler.schedulers.background import BackgroundScheduler


def ddns_tencent():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(os.path.join(BASE_DIR, 'configrations'), "config.json")

    if not os.path.exists(path):
        quit(0)

    with open(path, 'r') as f:
        configjson = json.load(f)

    Secret_ID = configjson["Secret_ID"]
    Secret_Key = configjson["Secret_Key"]
    domains = configjson["domains"]

    value = sohu_soip()
    for domainjson in domains:
        domain = domainjson.get("name", None)
        if not domain:
            continue
        for subdomainjson in domainjson.get("subdomains", None):
            subdomain = subdomainjson.get("name", None)
            if not subdomain:
                continue
            record_type = subdomainjson.get("record_type", "A")
            record_line = subdomainjson.get("record_line", u"默认")
            rs = recordCreate(Secret_ID, Secret_Key, domain, subdomain, record_type, record_line, value)
            print(rs)


if __name__ == "__main__":
    print("开始循环解析域名")
    sched = BlockingScheduler()
    sched.add_job(ddns_tencent, "interval", seconds=5)
    sched.start()