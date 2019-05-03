import requests
import re
import base64
import os
import sys
import json
import logging
import Hlog
import configparser

CONFIG_FILE_NAME = "account.conf"
config = configparser.ConfigParser()
config.read(CONFIG_FILE_NAME)
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s]\n  line:%(lineno)d,level:%(levelname)s,message:%(message)s\n',
    datefmt='%Y/%b/%d %H:%M:%S',
    filename='log.log',
    filemode='a'
)


class ConfigException(Exception):
    pass


def getAccount()->str:
    try:
        print(config.get("account", "username"))
        return config.get("account", "username")

    except Exception as e:
        Hlog.Hlog("读取账户名失败\t"+str(e), Hlog.error, True)
        raise ConfigException('读取用户名失败')


def getPasswordBase64()->str:
    try:
        print(config.get("account", "password"))
        return config.get("account", "password")

    except Exception as e:
        Hlog.Hlog("读取密码失败\t"+str(e), Hlog.error, True)
        raise ConfigException("读取用户名失败")


def writeAccount(account: str)->None:
    try:
        if not "account" in config.sections():
            config.add_section("account")
        config.set("account", "username", account)
        with open(CONFIG_FILE_NAME, "w+") as file:
            config.write(file)
    except Exception as e:
        Hlog.Hlog("账户名写入配置文件失败\t"+str(e), Hlog.error, True)
        raise Exception("账户名写入配置文件失败")


def writePassword(password: str)->None:
    try:
        if not "account" in config.sections():
            config.add_section("account")
        config.set("account", "password", base64.b64encode(
            bytes(password, encoding='utf8')).decode())
        with open(CONFIG_FILE_NAME, "w+") as file:
            config.write(file)
    except Exception as e:
        Hlog.Hlog("密码写入配置文件失败\t"+str(e), Hlog.error, True)
        raise Exception("密码写入配置文件失败")


def generateHeaders():
    return \
        {
            'Host': 'w.seu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 \
                                     Win64 \
                                     x64 \
                                     rv: 66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'application/json, text/javascript, */* q=0.01',
            'Accept-Language': 'zh-CN, zh \
            q = 0.8, zh-TW \
            q = 0.7, zh-HK \
            q = 0.5, en-US \
            q = 0.3, en \
            q = 0.2 ',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https: // w.seu.edu.cn /',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive'
        }


def generateForm():
    return \
        {
            'enablemacauth': '1',
            # 'password': base64.b64encode(bytes(config.get("account","password"),encoding = 'utf8')),  #input password in quotations
            # 'username': config.get("account","username")  #input password in quotations
            'password': getPasswordBase64(),
            'username': getAccount()
        }


def login()->str:
    try:
        res = requests.post('https://w.seu.edu.cn/index.php/index/login',
                            generateForm(), headers=generateHeaders(), verify=False)
        resText = json.loads(res.text)
        Hlog.HlogList(resText, Hlog.info, True)
        return resText['info']
    #     logText = ''
    #     for x in resText:
    #         logText += '\n[ %s ] %s' %(x,resText[x])
    #         print('[ %s ] %s'% (x,resText[x]))
    #     logging.info(logText)
    except Exception as e:
        Hlog.Hlog(str(e), Hlog.error, True)
        raise e


def logout()->str:
    try:
        res = requests.post('https://w.seu.edu.cn/index.php/index/logout',
                            headers=generateHeaders(), verify=True)
        resText = json.loads(res.text)
        Hlog.HlogList(resText, Hlog.info, True)
        return resText['info']
        # logText = ''
        # for x in resText:
        #     logText += '\n[ %s ] %s' %(x,resText[x])
        #     print('[ %s ] %s'% (x,resText[x]))
        # logging.info(logText)
    except Exception as e:
        Hlog.Hlog(str(e), Hlog.error, True)
        raise e

def logFile():
    try:
        with open('log.log','r') as f:
            return f.read()
    except Exception as e:
        Hlog.Hlog(str(e),Hlog.error,True)
        raise Exception('当前日志不可读或者不存在')

if __name__ == '__main__':
    writeAccount('Hanyuu')
    writePassword('Hanyuu')
