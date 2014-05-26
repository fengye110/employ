#!/usr/bin/env python  
#coding=utf-8  

from workitem import WorkItem

class Employ(object):
    def __init__(self, name):
        self.name = name
        self.woritems = []

    def lookup(cls, name):

