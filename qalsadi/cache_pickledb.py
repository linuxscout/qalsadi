#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        analex
# Purpose:     Arabic lexical analyser, provides feature to stem arabic 
#words as noun, verb, stopword
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-------------------------------------------------------------------------------
"""Cache Module for analex"""
import sys

    
from hashlib import md5
import os
import pickledb    

class Cache(object):
    """
        cache for word morphological analysis
    """
    def __init__(self, dp_path = False):
        """
        Create Analex Cache
        """
        DB_PATH = os.path.join(os.path.expanduser('~'), '.qalsadiCache.pickledb')
        self.cache = {
            'checkedWords': {},
            'FreqWords': {
                'noun': {},
                'verb': {},
                'stopword': {}
            },
        }
        if not dp_path:
            dp_path = DB_PATH
        else:
            dp_path = os.path.join(os.path.dirname(dp_path), '.qalsadiCache.pickledb')
        #~ self.db =  pickledb.load(dp_path, False)
        try:
            self.db =  pickledb.load(dp_path, False)
        except:
            print("Can't Open data base")
            self.db = None
    def __del__(self):
        """
        Delete instance and clear cache

        """
        self.cache = None
        if self.db:
            self.db.dump()

    def is_already_checked(self, word):
        """ return if ``word`` is already cached"""
        try:
            return bool(self.db.get(word))
        except:
            return False
        #~ except: return False;

    def get_checked(self, word):
        """ return checked ``word`` form cache"""
        #~ word = bytes(word, "utf-8")
        result = []
        if self.db:
            result = self.db.get(word)
        
        return result

    def add_checked(self, word, data):
        """ add checked ``word`` form cache"""
        if self.db:
            self.db.set(word, data)

    def exists_cache_freq(self, word, wordtype):
        """ return if word exists in freq cache"""
        return word in self.cache['FreqWords']

    def get_freq(self, originalword, wordtype):
        """ return  ``word`` frequency form cache"""
        return self.cache['FreqWords'][wordtype].get(originalword, 0)

    def add_freq(self, original, wordtype, freq):
        """ add   ``original`` frequency ``freq`` to cache"""
        self.cache['FreqWords'][wordtype][original] = freq


def mainly():
    """main function"""
    print("test")
    path = os.path.join(os.path.dirname(__file__),"cache", '.qalsadiCache')
    cacher = Cache(path)
    word = "taha"
    data = "zerrouki"
    cacher.add_checked(word, data)
    d2  = cacher.get_checked(word)
    d3  = cacher.get_checked("walid")
    print(d2)
    print(d3)

if __name__ == "__main__":
    mainly()
