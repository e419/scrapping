#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Rutracker login with requests"""


import os
import requests


LOGIN_URL = 'http://login.rutracker.org/forum/login.php'

SEARCH_URL = 'http://rutracker.org/forum/tracker.php'

CREDS = {
    'login':  u'Вход',
    'login_username': os.environ.get('TRACKER_USER', 'foo'),
    'login_password': os.environ.get('TRACKER_PASSWORD', 'bar')
}

SEARCH_ITEM = {
    'nm': 'idm 2016',
}


def main():
    """ Initiate login and grab some data """
    login_request = requests.post(
        LOGIN_URL,
        data=CREDS,
        allow_redirects=True
    )
    if login_request.ok and 'bb_data' in login_request.cookies:
        print 'yey!'
        search_request = requests.post(
            SEARCH_URL,
            data=SEARCH_ITEM,
            cookies=login_request.cookies.get_dict(),
            allow_redirects=True,
        )
        print search_request.content

if __name__ == '__main__':
    main()

