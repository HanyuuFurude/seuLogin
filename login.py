import requests
import re
import base64
import os
import sys
headers = \
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) \
        Gecko/20100101 Firefox/64.0'
    }
form = \
    {
        'enablemacauth': 0,
        'password': base64.b64encode(b''),  #input password in quotations
        'username': ''  #input password in quotations
    }

if __name__ == '__main__':
    arg=sys.argv
    print(arg)
    res = requests.post('https://w.seu.edu.cn/index.php/index/login', form,headers=headers,verify=False)
    print(res.text)