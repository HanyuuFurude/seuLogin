import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s %(filename)s]\n  line:%(lineno)d,level:%(levelname)s,message:%(message)s\n',
    datefmt='%Y/%b/%d %H:%M:%S',
    filename='log.log',
    filemode='a'
)

# debug() 调试级别，一般用于记录程序运行的详细信息
debug = 0
# info() 事件级别，一般用于记录程序的运行过程
info = 1
# warning() 警告级别，，一般用于记录程序出现潜在错误的情形
warning = 2
# error() 错误级别，一般用于记录程序出现错误，但不影响整体运行
error = 3 
# critical 严重错误级别 ， 出现该错误已经影响到整体运行
critical = 4

logList = {
    debug:logging.debug,
    info:logging.info,
    warning:logging.warning,
    error:logging.error,
    critical:logging.critical
    }
def HlogList(array:list,mode:int = 0,onScreen:bool = False)->None:
    logText = ''
    for x in array:
        logText += '\n[ %s ] %s' %(x,array[x])
    logList[mode](logText)
    if onScreen is True:
        print(logText)

def Hlog(context:list,mode:int = 0,onScreen:bool = False)->None:
    logList[mode](context)
    if onScreen is True:
        print(context)