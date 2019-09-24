# -*- coding:utf-8 -*-  
# __auth__ = mocobk
# email: mailmzb@qq.com

import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="ilogger",
    version="0.0.2",
    author="mocobk",
    author_email="mocobk@163.com",
    description="超简单的日志模块，导入即用",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mocobk/ilogger",
    packages=['ilogger'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)