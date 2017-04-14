# -*- coding:utf-8 -*-
import requests

# HOST = 'http://127.0.0.1:5000'

HOST = 'http://118.89.230.54:8080'


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
    print _check_user('wbcd3332', 'wbc').status_code
    print _get_rifles('root').content
    print _get_rifles('wbcd').content
    print _patch_rifle('wbc').content
    _post_rifle('wbcd')