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

class Sql(object):
    def __init__(self):
        try:
            self.sql_con = sqlite3.connect(dbfile)
            self.cur = self.sql_con.cursor()
        except sqlite3.Error as e:
            print("sql connect error {0}"%(dbfile))
            return None

        self.createdb()

    def createdb(self):
        # create workitem table
        cmd = "SELECT name from sqlite_master WHERE type='table' and name='{0}'".format(itemtbls)
        rows = self.runcmd(cmd)
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
            self.runcmd(cmd)

        # create employee table
        cmd = "SELECT name from sqlite_master WHERE type='table' and name='{0}'".format(emptbl)
        rows = self.runcmd(cmd)
        if(len(rows) == 0):
            cmd = """
                CREATE TABLE `{0}` (
                    `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    `name`	TEXT NOT NULL,
                    `month`	INTEGER NOT NULL,
                    `money`	REAL NOT NULL
                );
            """.format(emptbl)
            self.runcmd(cmd)

    def runcmd(self, cmdstr):
        logging.debug(" "+cmdstr)
        #pdb.set_trace()
        sql_con = None
        try:
            self.cur.execute(cmdstr)
            self.sql_con.commit()
        except sqlite3.Error as e:
            logging.error(" sql cmd:{0} error:{1}".format(cmdstr, e))
            return [] 

        if(cmdstr.lower().find("select") != -1):
            return self.cur.fetchall()
        return []


sqlobj = Sql()
