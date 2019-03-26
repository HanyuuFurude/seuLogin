import requests
import re
import base64
import os
import sys
import json
import PyQt5
import logging
import Hlog

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
        'password': base64.b64encode(b'0e2a78c2'),  #input password in quotations
        'username': '213173051'  #input password in quotations
    }

def login():
    try:
        res = requests.post('https://w.seu.edu.cn/index.php/index/login', form,headers=headers,verify=False)
        resText = json.loads(res.text)
        Hlog.HlogList(resText,Hlog.info,True)
    #     logText = ''
    #     for x in resText:
    #         logText += '\n[ %s ] %s' %(x,resText[x])
    #         print('[ %s ] %s'% (x,resText[x]))
    #     logging.info(logText)
    except Exception as e:
        Hlog.Hlog(str(e),Hlog.error,True)
def logout():
    try:
        res = requests.post('https://w.seu.edu.cn/index.php/index/logout',headers=headers,verify=False)
        resText = json.loads(res.text)
        Hlog.HlogList(resText,Hlog.info,True)
        # logText = ''
        # for x in resText:
        #     logText += '\n[ %s ] %s' %(x,resText[x])
        #     print('[ %s ] %s'% (x,resText[x]))
        # logging.info(logText)
    except Exception as e:
        Hlog.Hlog(str(e),Hlog.error,True)