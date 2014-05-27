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

        # check if name in db
        cmd='SELECT id,name FROM {0}  WHERE name="{1}" LIMIT 1'.format(emptbl, self.name)
        pdb.set_trace()
        #cmd="SELECT id,name FROM {0}  WHERE name like '%{1}%' ".format(emptbl, name)
        ids=sqlobj.runcmd(cmd)
        if(len(ids) == 1):
            self.id = ids[0][0]

    def update(self):
        if(self.id == None):
            self._add()
        else:
            # update all value to  sql
            cmd='UPDATE {0} SET name="{1}", month={2}, money={3} WHERE id={4}'.format(emptbl,self.name, self.month, self.money, self.id)
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
        if(self.id != None):
            cmd='DELETE FROM {0} WHERE id={1}'.format(emptbl, self.id)
            sqlobj.runcmd(cmd)

    def _add(self):
        # insert to table
        cmd = 'INSERT INTO {0} (id,name,month,money) VALUES (NULL,"{1}",{2},{3})'.format(emptbl,self.name, self.month, self.money)
        sqlobj.runcmd(cmd)
        # get id
        cmd ='SELECT id FROM {0} ORDER BY id DESC LIMIT  1'.format(emptbl)
        ids=sqlobj.runcmd(cmd)
        if(len(ids) != 1):
            logging.error("get id after insert faild\n")
            return -1
        self.id = ids[0]
        return 0

if __name__ == '__main__':
    ep = Employ("ni")
    ep.money = 20
    ep.update()
    #ep.money = 1
    #ep.update()
    ep.remove()

    ep = Employ("kk")
    ep.set(None, 23,111)
    ep.update()
