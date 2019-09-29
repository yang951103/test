# -*- coding: utf-8 -*-
import requests
import pprint
import json

localhost = 'http://127.0.0.1:8000/'


def get(url, api='', para={}):
    url += api
    return requests.get(url, para)


def post(url, api='', para={}):
    url += api
    return requests.post(url, para, auth=('ys', 'asdf'))


# res = post(localhost, 'snippets.json', {'code': 'as = 1'}).text
# pprint.pprint(json.loads(res))

res = get(localhost, 'snippets.json', {
    'created_after': '2019-09-26',
    'created_before': '2019-09-26',
}).text
pprint.pprint(json.loads(res))
