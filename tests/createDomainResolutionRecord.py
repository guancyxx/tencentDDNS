# -*- coding:utf8 -*-
from tencentAPI.domainNameResolutionRecord import recordCreate
from utils.getPublicNetworkIP import sohu_soip

if __name__ == "__main__":
    Secret_ID = "AKIDA9zd6S5gXM1VowxiNTddS67ye9Tbroqh"
    Secret_Key = "sZ5ThonfNeidZBh4LQK7rQPn2A6sUxGU"

    domain = "guancyxx.cn"
    subdomain = "test"
    record_type = "A"
    record_line = u"默认"
    value = sohu_soip()
    rs = recordCreate(Secret_ID, Secret_Key, domain, subdomain, record_type, record_line, value)
    print(rs)
