#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zhihu import client

myclient = client.ZhihuClient()
myclient.login_with_cookies('cookies.json')
print(myclient.me()._name)

