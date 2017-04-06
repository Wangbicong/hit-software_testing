# -*- coding:utf-8 -*-
import requests

HOST = 'http://localhost:5000'


def patch_rifle(lock=1, stock=1, barrel=1):
    return requests.post(HOST + '/rifle', json={
        'lock': lock,
        'stock': stock,
        'barrel': barrel
    })

patch_rifle()