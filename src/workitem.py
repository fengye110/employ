#!/usr/bin/env python  
#coding=utf-8  
import sqlite3


class WorkItem(object):
    def __init__(self, name):
        self.name = name
        self.price = 0

    def look(cls, name):
        if(sql_con == None):
            try:
                sql_con = sqlite3.connect(dbfile)
                cur = sql_con.cursor()
            except sqlite3.Error,e:
                print("canot open sqlfile:"%(dbfile))
        t = (name,)
        for row in cur.execute("SELECT * from ? WHERE name=?", t):
            print row
