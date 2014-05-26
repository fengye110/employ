#!/usr/bin/env python  
#coding=utf-8  

from workitem import WorkItem
from sql import sqlobj
from sql import emptbl
import time
import logging
import pdb

class Employ(object):
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.month = time.strftime("%m")
        self.id = None
        self.workitems=[]

    def update(self):
        if(self.id == None):
            self._add()
        else:
            cmd="UPDATE `employs` SET `name`='{0}' , month='{1}', money='{2}' WHERE id='{3}'".format(self.name, self.month, self.money)
            sqlobj.runcmd(cmd)

    def set(self, name, month, money):
        if(name != None):
            self.name = name
        if(month != None):
            self.month = month
        if(money != None):
            self.money = money
        #self.update()

    def remove(self):
        pass

    def _add(self):
        # insert to table
        cmd = 'INSERT INTO {0} (id,name,month,money) VALUES (NULL,"{1}",{2},{3})'.format(emptbl,self.name, self.month, self.money)
        sqlobj.runcmd(cmd)
        # get id
        cmd ="SELECT id FROM {0} ORDER BY id DESC LIMIT  1".format(emptbl)
        ids=sqlobj.runcmd(cmd)
        if(len(ids) != 1):
            logging.error("get id after insert faild\n")
            return -1
        self.id = ids[0]
        return 0

if __name__ == '__main__':
    ep = Employ("ni")
    ep.set(None, None,20)
    ep.update()
    ep.set(None,None, 19)
    ep.update()
