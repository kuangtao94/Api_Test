import os
import logging
import datetime

def FilePath(filePath=None,fileName=None):
    """文件的路径封装"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),filePath,fileName)


def writeBookID(content):
    """写入BookID -->取出的ID为整型需强制转换为str类型"""
    # print("文件写入的时间:",datetime.datetime.now())
    with open(FilePath(filePath='data',fileName='bookID.md'),'w') as fp:
        fp.write(str(content))

def readBookID():
    """读取BookID"""
    # print("文件读取时间:",datetime.datetime.now())
    with open(FilePath(filePath='data',fileName='bookID.md')) as fp:
        return fp.read()

def log(log_content):
    '''日志定义级别'''
    # 定义文件
    logFile = logging.FileHandler(FilePath('log','logInfo.md'), 'a',encoding='utf-8')
    # log格式
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
    logFile.setFormatter(fmt)

    # 定义日志
    logger1 = logging.Logger('logTest', level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)
    logFile.close()

# print(FilePath('data','data.yaml'))