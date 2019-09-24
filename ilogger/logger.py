#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : ilogger.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/9/13 19:52
import logging
import sys

default_fmt = '[%(asctime)s]%(levelname)7s: %(message)s'


def _stream_handler():
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(default_fmt)
    handler.setFormatter(formatter)
    return handler


_logger = logging.getLogger(__name__)
_logger.addHandler(_stream_handler())
_logger.setLevel(logging.INFO)


class Logger:
    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    WARN = logging.WARN
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    @classmethod
    def setLevel(cls, level):
        return _logger.setLevel(level)

    @classmethod
    def setFormatter(cls, fmt=default_fmt, datefmt=None, style='%'):
        _handler = _logger.handlers[0]
        _handler.setFormatter(logging.Formatter(fmt, datefmt, style))

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def info(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def warn(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def error(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        pass


setattr(Logger, 'debug', _logger.debug)
setattr(Logger, 'info', _logger.info)
setattr(Logger, 'warn', _logger.warn)
setattr(Logger, 'warning', _logger.warning)
setattr(Logger, 'error', _logger.error)
setattr(Logger, 'critical', _logger.critical)
