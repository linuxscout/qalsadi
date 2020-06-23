#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        CArabic Dictionary from Arramooz Al Waseet
# Purpose:     Morphological porpus Dictionary.
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     16-12-2013
# Copyright:   (c) Taha Zerrouki 2013
# Licence:     GPL
#-------------------------------------------------------------------------------
"""
Arabic Dictionary Class from Arramooz Al Waseet.
Used in multiporpus morpholigical treatment
"""
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import re
import os, os.path
#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import sys
FILE_DB = u"data/custom_dictionary.sqlite"
import pyarabic.araby as araby
import arramooz.arabicdictionary
class custom_dictionary(arramooz.arabicdictionary.ArabicDictionary):
    """
    Arabic dictionary Class customized, used to add new words before add them to arramooz project.
    It's used to add new entries manually to this dictionary by user, 
    In order to improve lately Arramooz project.
    """

    def __init__(self, table_name, filename_db=FILE_DB):
        """
        initialisation of dictionary from a data dictionary, create indexes 
        to speed up the access.

        """
        
        arramooz.arabicdictionary.ArabicDictionary.__init__(self, table_name)

        # costumized data
        # get the database path
        if hasattr(sys, 'frozen'): # only when running in py2exe this exists
            base = sys.prefix
        else: # otherwise this is a regular python script
            base = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base, filename_db)

        if os.path.exists(file_path):
            try:
                self.db_connect = sqlite.connect(file_path)                
                self.db_connect.row_factory = sqlite.Row 
                self.cursor = self.db_connect.cursor()
                #print("Connect with success")
            except  IOError:
                print("Fatal Error Can't find the database file", file_path)
        else:
            print(u" ".join(["Inexistant File", file_path, " current dir ", 
            os.curdir]).encode('utf8'))

#Class test
def mainly():
    """
    main test
    """
    #ToDo: use the full dictionary of arramooz
    mydict = custom_dictionary('verbs')
    wordlist = [u"استقلّ", u'استقل', u"كذب"]
    tmp_list = []
    for word in wordlist:
        foundlist = mydict.lookup(word)
        for word_tuple in foundlist:
            word_tuple = dict(word_tuple)
            vocalized = word_tuple['vocalized']
            tmp_list.append(dict(word_tuple))
    print(repr(tmp_list).replace('},','},\n').decode("unicode-escape"))            
if __name__  ==  '__main__':
    mainly()
