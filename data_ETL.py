#! /usr/bin/env python
# -*-coding:utf-8-*-

import os, configparser

class params:
    def __init__(self, path='./config.cfg', selector='DEFAULT'):
        param = configparser.ConfigParser()
        param.read(path)
        self.param=dict()
        for i in param.items(selector):
            self.param.setdefault(i[0], i[1])

class combinator():
    def __init__():
        pass
    @classmethod
    def combin(self,path):
        pass


class extrator():
    def __init__(self):
        pass

class cleansing():
    def __init__(self):
        pass

class exporter():
    def __init__(self):
        pass


if __name__=="__main__":
    param = params()
    print()