"""
login and logout w.seu.edu.cn with Python
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request as urllib
import urllib.parse
import http.client as httplib
import sys
import time
import getpass
import json
USERNAME = 'your_username'
PASSWORD = 'your_password'
HEADERS = {
    'Content-Type': "application/json; charset=utf-8",
    'dataType': "json",
    'cache': False
}


login_header = {

    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'w.seu.edu.cn',
    'Origin': 'https://w.seu.edu.cn',
    'Referer': 'https://w.seu.edu.cn/',

    'X-Requested-With': 'XMLHttpRequest',
    'dataType': "json",
                'cache': 'false'
}
ADDRESS = "w.seu.edu.cn"
INIT_URL = "/index.php/index/init"
LOGIN_URL = "/index.php/index/login"
LOGOUT_URL = "/index.php/index/logout"


def login(username, password):
    """Login fuction based on httplib.
    Check login status, if logined then print status (IP, time, location).
    If not logined, 'POST' your login parameters to server.
    """
    conn = httplib.HTTPSConnection(ADDRESS)
    conn.request("GET", INIT_URL, headers=HEADERS)
    # get response from web server
    temp = conn.getresponse().read()
    print(temp)
    content = json.loads(temp.decode())
    # make sure if user is login
    print(content)

    if(content['info'] == "用户未登录"):

        import base64
        params = {'username': username, 'password': base64.b64encode(
            password.encode('utf-8')), 'enablemacauth': 0}
        try:

            conn.request("POST", LOGIN_URL, body=urllib.parse.urlencode(
                params), headers=login_header)
            # get response from web server

            content = conn.getresponse().read()

            # remove useless header
            content = content[3:]
            print(json.loads(content.decode()))
            conn.close()
        except:
            print("Post error!")


def logout():
    """Logout based on httplib.
    'POST' logout parameters to server.
    """
    try:
        conn = httplib.HTTPSConnection(ADDRESS)
        conn.request("POST", LOGOUT_URL, headers=HEADERS)
        conn.close()
        print("Logout Sucess!!")
    except:
        print("Post error!")


def status():
    """Print login status.
    If logined, print status (IP, time, location).
    If not logined, print 'Not login!'
    """
    try:
        conn = httplib.HTTPSConnection(ADDRESS)
        conn.request("GET", INIT_URL, headers=HEADERS)
        # get response from web server
        content = conn.getresponse().read()
        # make sure if user is login
        if b'notlogin' in content:
            print("Not login!")
            return
        # remove useless header, http header here is different from login.
        content = content[3:]
        print(json.loads(content.decode()))
    except:
        print("Get Status error!")


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print("No param is inputed. Please input params.")
        print("Usage python %s [login | logout | status | help]" % sys.argv[0])
    elif sys.argv[1] == 'login':
        try:
            # for command "python seu_weblogin.py login username password"
            INPUT_USERNAME = sys.argv[2]
            INPUT_PASSWORD = sys.argv[3]
        except IndexError:
            # if you didn't want to save username and password in this file
            # you can input username and password by standard input
            INPUT_USERNAME = USERNAME
            INPUT_PASSWORD = PASSWORD
            if 'your' in USERNAME or 'your' in PASSWORD:
                # reqire username and password from std input
                INPUT_USERNAME = input("Username:")
                # don't show my password on screen
                INPUT_PASSWORD = getpass.getpass("Password:")
        login(INPUT_USERNAME, INPUT_PASSWORD)
    elif sys.argv[1] == 'logout':
        logout()
    elif sys.argv[1] == 'status':
        status()
    else:
        print("Input param is not supported!")
        print("Usage python %s [login | logout | status | help]" % sys.argv[0])
