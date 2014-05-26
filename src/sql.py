#!/usr/bin/env python  
#coding=utf-8  
import sqlite3
import os.path
import pdb
import logging


logging.basicConfig(level=logging.DEBUG,
        format='[%(filename)s:%(funcName)s:%(lineno)d]%(message)s',
                    )

dbfile = "employs.db"
itemtbls="workitem"
emptbl="employs"
class sql(object):
    def __init__(self):
        try:
            self.sql_con = sqlite3.connect(dbfile)
            self.cur = self.sql_con.cursor()
        except sqlite3.Error,e:
            print("sql connect error {0}"%(dbfile))
            return None

        self.createdb()

    def createdb(self):
        # create workitem table
        cmd = "SELECT name from sqlite_master WHERE type='table' and name='{0}'".format(itemtbls)
        logging.debug("cmd={0}".format(cmd))
        self.cur.execute(cmd)
        rows = self.cur.fetchall()
        pdb.set_trace()
        if(len(rows) == 0):
            cmd = """
                CREATE TABLE `{0}` (
                    `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    `name`	TEXT NOT NULL,
                    `price`	REAL NOT NULL DEFAULT '0',
                    `radio`	REAL NOT NULL,
                    `len`	REAL NOT NULL
                );
            """.format(itemtbls)
            self.cur.execute(cmd) 
            self.sql_con.commit()

        # create employee table
        cmd = "SELECT name from sqlite_master WHERE type='table' and name={0}".format(emptbl)
        logging.debug("cmd={0}".format(cmd))
        if(len(rows) == 0):
            cmd = """
                CREATE TABLE `{0}` (
                    `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    `name`	TEXT NOT NULL,
                    `month`	REAL NOT NULL,
                    `money`	REAL NOT NULL
                );
            """.format(emptbl)
            self.cur.execute(cmd) 
            self.sql_con.commit()

if __name__ == '__main__':
    obj = sql()
