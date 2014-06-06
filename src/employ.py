#!/usr/bin/env python  
#coding=utf-8  

from workitem import WorkItem
from sql import sqlobj
from sql import emptbl
import time
import logging
import pdb
from pinyin.pinyin import piny

class Employ(object):
    def __init__(self, name):
        self.name = name
        #self.money = 0
        #self.month = time.strftime("%m")
        self.id = None
        self.pinyin = None
        self.workitems=[]
        self.pinyin = piny.hanzi2pinyin(self.name)
        self.codeid = -1;

        # check if name in db
        cmd='SELECT id,name FROM {0}  WHERE name="{1}" LIMIT 1'.format(emptbl, self.name)
        #pdb.set_trace()
        #cmd="SELECT id,name FROM {0}  WHERE name like '%{1}%' ".format(emptbl, name)
        ids=sqlobj.runcmd(cmd)
        if(len(ids) == 1):
            logging.debug(" has employ:{0}".format(self.name))
            self.id = ids[0][0]
        else:
            logging.debug(" has no employ:{0}".format(self.name))

    def update(self):
        if(self.id == None):
            self._add()
        else:
            # update all value to  sql
            cmd='UPDATE {0} SET name="{1}", WHERE id={2}'.format(emptbl,self.name, self.id)
            sqlobj.runcmd(cmd)

    def remove(self):
        if(self.id != None):
            cmd='DELETE FROM {0} WHERE id={1}'.format(emptbl, self.id)
            sqlobj.runcmd(cmd)

    def _add(self):
        # insert to table
        cmd = 'INSERT INTO {0} (id,name,codeid) VALUES (NULL,"{1}",{2})'.format(emptbl,self.name, self.codeid)
        sqlobj.runcmd(cmd)
        # get id
        cmd ='SELECT id FROM {0} ORDER BY id DESC LIMIT  1'.format(emptbl)
        ids=sqlobj.runcmd(cmd)
        if(len(ids) != 1):
            logging.error("get id after insert faild\n")
            return -1
        self.id = ids[0][0]
        return 0

if __name__ == '__main__':
    ep = Employ("ni")
    ep.update()
    #ep.money = 1
    #ep.update()
    ep.remove()

    ep = Employ("kk0")
    ep.update()
    ep.remove()
