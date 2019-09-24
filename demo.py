# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com
from ilogger import logger

# 默认级别为 INFO
logger.debug('this is debug message')
logger.info('this is info message')

# 设置 logger 级别
logger.setLevel(logger.DEBUG)

logger.debug('this is debug message')
logger.info('this is info message')
logger.warning('this is warning message')
logger.warn('this is warning message')
logger.error('this is error message')
logger.critical('this is critical message')

# 设置 logger 格式
logger.setFormatter(fmt='[%(asctime)s]%(levelname)7s[%(filename)s:%(lineno)s]: %(message)s')

logger.debug('this is debug message')
logger.info('this is info message')
