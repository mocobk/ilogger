# ilogger
超简单的日志模块，导入即用

### 如何使用它?

```shell
>>> pip install ilogger
```


```python

from ilogger import logger

# 直接使用，默认级别为 INFO
logger.debug('this is debug message')
logger.info('this is info message')
```

    [2019-09-24 19:54:23,544]   INFO: this is info message

```python

from ilogger import logger

# 设置 logger 级别
logger.setLevel(logger.DEBUG)

logger.debug('this is debug message')
logger.info('this is info message')
logger.warning('this is warning message')
logger.warn('this is warning message')
logger.error('this is error message')
logger.critical('this is critical message')
```
    [2019-09-24 19:54:23,544]  DEBUG: this is debug message
    [2019-09-24 19:54:23,544]   INFO: this is info message
    [2019-09-24 19:54:23,544]WARNING: this is warning message
    [2019-09-24 19:54:23,544]WARNING: this is warning message
    [2019-09-24 19:54:23,544]  ERROR: this is error message
    [2019-09-24 19:54:23,544]CRITICAL: this is critical message


```python

from ilogger import logger

# 设置 logger 格式
logger.setFormatter(fmt='[%(asctime)s]%(levelname)7s[%(filename)s:%(lineno)s]: %(message)s')

logger.debug('this is debug message')
logger.info('this is info message')
```

    [2019-09-24 19:54:23,544]  DEBUG[demo.py:21]: this is debug message
    [2019-09-24 19:54:23,544]   INFO[demo.py:22]: this is info message



