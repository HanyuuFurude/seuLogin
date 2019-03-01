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

if __name__ == '__main__':
    arg=sys.argv
    print(arg)
    res = requests.post('https://w.seu.edu.cn/index.php/index/logout', headers=headers,verify=False)
    print(res.text)