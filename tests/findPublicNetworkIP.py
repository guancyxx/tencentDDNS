# -*- coding:utf8 -*-

"""
获取公网IP地址

思路：访问某些提供IP地址查询的网站，拿到访问结果，正则解析之

同类网址：

http://pv.sohu.com/cityjson?ie=utf-8  （ie参数功能为设置编码，这个相对更好用一点）

"""

import requests
import re

from utils.getPublicNetworkIP import sohu_soip

if __name__ == "__main__":
    print(sohu_soip())
