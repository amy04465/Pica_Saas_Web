'''
__data__ = 2018/6/22
__author__ = amy liu
'''
# coding = utf-8

# 日志类

import logging
import logging.handlers

class Logger():
    LOG_FILE = 'test.log'

    # 实例化 handler
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

    # 实例化 formatter
    formatter = logging.Formatter(fmt)
    # 为 handler 添加 formatter
    handler.setFormatter(formatter)

    # 获取名 为 test 的logger
    logger = logging.getLogger('test')
    # 为 logger 添加 handler
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    def loginfo(self, message):
        self.logger.info(message)

    def logdebug(self, message):
        self.logger.debug(message)




