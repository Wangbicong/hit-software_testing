# -*- coding:utf-8 -*-
import requests

HOST = 'http://118.89.230.54:5000'


def patch_rifle(lock=33, stock=100, barrel=1):
    return requests.post(HOST + '/rifle', json={
        'lock': lock,
        'stock': stock,
        'barrel': barrel
    })

print patch_rifle().status_code