#!/usr/bin/env python
# -*- coding:utf-8 -*-
#coding=utf-8  

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path
import pdb

class PinYin(object):
    loaded = None
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file
        if(PinYin.loaded == None):
            self.load_word()
            PinYin.loaded = 1

    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with open(self.dict_file,encoding='utf-8') as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]


    def cvt(self, string=""):
        result = []
        #if not isinstance(string, unicode):
            #string = string.decode("utf-8")
        
        alpha=""
        for char in string:
            key = '%X' % ord(char)
            #pdb.set_trace()
            if(char.isalnum()):
                alpha +=char
            elif(char.isspace()):
                if(len(alpha)>0):
                    result.append(alpha)
                    alpha=""
            else:
                if(len(alpha)>0):
                    result.append(alpha)
                    alpha=""
                result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        if(len(alpha)>0):
            result.append(alpha)
            alpha=""

        return result


    def cvt_split(self, string="", split=""):
        result = self.cvt(string=string)
        if split == "":
            return result
        else:
            return split.join(result)

piny = PinYin(os.path.dirname(os.path.abspath(__file__)) + './word.data')

if __name__ == "__main__":
    test = PinYin('./word.data')
    test.load_word()
    string = "钓鱼岛是中国的"
    print("in: %s" % string)
    print("out: %s" % str(test.cvt(string=string)))
    print("out: %s" % test.cvt_split(string=string, split="-"))
