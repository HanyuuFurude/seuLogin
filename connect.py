import requests
import re
import base64
import os
import sys
import json
import PyQt5
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s %(filename)s]\n  line:%(lineno)d,level:%(levelname)s,message:%(message)s\n',
    datefmt='%Y/%b/%d %H:%M:%S',
    filename='log.log',
    filemode='a'
)

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

def login():
    arg=sys.argv
    print(arg)
    res = requests.post('https://w.seu.edu.cn/index.php/index/login', form,headers=headers,verify=False)
    resText = json.loads(res.text)
    # print('res\tvalue\n________________') # 丑死了，不要表头了
    logText = ''
    for x in resText:
        logText += '\n[ %s ] %s' %(x,resText[x])
        print('[ %s ] %s'% (x,resText[x]))
    logging.info(logText)