# -*- coding:utf-8 -*-
import requests

HOST = 'http://127.0.0.1:5000'


def _add_user(username, password):
    return requests.post(HOST + '/login', json={
        'username': username,
        'password': password,
        'flag': 1
    })


def _check_user(username, password):
    return requests.post(HOST + '/login', json={
        'username': username,
        'password': password,
        'flag': 0
    })


def _get_rifles(username):
    return requests.get(HOST+'/rifles/'+username)


def _patch_rifle(username, lock=1, stock=1, barrel=1):
    return requests.patch(HOST+'/rifle/'+username, json={
        'lock': lock,
        'stock': stock,
        'barrel': barrel
    })


def _post_rifle(username):
    return requests.post(HOST+'/rifle/'+username)

if __name__ == '__main__':
    _add_user('wbcd', 'wbc')
    print _get_rifles('wbc').content
    print _get_rifles('wbcd').content
    _patch_rifle('wbcd')
    _post_rifle('wbcd')