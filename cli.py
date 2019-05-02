import sys
import time
import connect
import Hlog
import os

if __name__ == '__main__':
    args = sys.argv
    print(args)
    if '-login' in args:
        connect.login()
        time.sleep(3)
        sys.exit()
    if '-logout' in args:
        connect.logout()
        time.sleep(3)
        sys.exit()
    if '-userName' in args:
        try:
            userName = args[args.index('-userName')+1]
        except Exception as e:
            print('no data after \'username\'')
            Hlog.Hlog(str(e),Hlog.error)
        finally:
            sys.exit()
    if '-long' in args:
        while True:
            pass
            connect.login()
            time.sleep(60*10)
            sys.exit()
    if '-password' in args:
        try:
            userName = args[args.index('-password')+1]
        except Exception as e:
            print('no password after \'-password\'')
            Hlog.Hlog(str(e),Hlog.error)
        finally:
            sys.exit()
    if '-help' in args:
        print('''
-login: 登录
-logout: 登出
-userName: 设置用户名（一卡通号）
-password: 设置密码
        ''')
    else:
        print('''您的输入有误，请检查，输入--help查看帮助文件''')


