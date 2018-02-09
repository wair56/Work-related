#! /usr/bin/env python
# -*-coding:utf-8-*-

import os, configparser, codecs


class params:
    @classmethod
    def getparam(self, path='.\config.cfg', selector='DEFAULT'):
        param = configparser.ConfigParser()
        param.read(path)
        self.param = dict()
        for i in param.items(selector):
            self.param.setdefault(i[0], i[1])
        return self.param


class combinator():
    @classmethod
    def combine(self, path='.\input'):
        for i in os.listdir(path):
                
        


# class changes():


class extrator():
    def __init__(self):
        pass


class cleansing():
    def __init__(self):
        pass


class exporter():
    filename = {
        "abnormalFile.txt": "异常.txt",
        "customerFile.txt": "客户信息.txt",
        "financefile.txt": "缴款信息.txt",
        "orderfile.txt ": " 运单信息.txt",
        "payfile.txt ": " 支付信息.txt",
        "routefile.txt ": "路径文件.txt",
        "tradereceivefile.txt ": "账户信息.txt",
        "transitfile.txt ": " 运输信息.txt"
    }

    def __init__(self):
        pass


if __name__ == "__main__":
    combinator.combine()