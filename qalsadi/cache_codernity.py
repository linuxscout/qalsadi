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
from codernitydb3.database import Database
from codernitydb3.hash_index import HashIndex
    
#~ class WithAIndex(HashIndex):

    #~ def __init__(self, *args, **kwargs):
        #~ kwargs['key_format'] = '32s'
        #~ super(WithAIndex, self).__init__(*args, **kwargs)

    #~ def make_key_value(self, data):
        #~ a_val = data.get("a")
        #~ if a_val is not None:
            #~ return a_val, None
        #~ return None

    #~ def make_key(self, key):
        #~ return key
class WithAIndex(HashIndex):
    def __init__(self, *args, **kwargs):
        # kwargs['entry_line_format'] = '<32s32sIIcI'
        #~ kwargs['key_format'] = '16s'
        kwargs['key_format'] = '32s'
        kwargs['hash_lim'] = 8 * 1024
        super(WithAIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("a")
        if a_val:
            if not isinstance(a_val, str):
                a_val = str(a_val)
            return md5(a_val.encode('utf8')).digest(), None
        return None

    def make_key(self, key):
        if not isinstance(key, str):
            key = str(key)
        return md5(key.encode('utf8')).digest()





class Cache(object):
    """
        cache for word morphological analysis
    """
    def __init__(self, dp_path = False):
        """
        Create Analex Cache
        """
        DB_PATH = os.path.join(os.path.expanduser('~'), '.qalsadiCache')
        self.cache = {
            'checkedWords': {},
            'FreqWords': {
                'noun': {},
                'verb': {},
                'stopword': {}
            },
        }
        if not dp_path:
            dp_path = self.DB_PATH
        else:
            dp_path = os.path.join(os.path.dirname(dp_path), '.qalsadiCache')
        #~ sys.stderr.write("Tahahahah\n"+" "+ dp_path +" "+str(type(dp_path)))
        #~ self.db = Database("/tmp/QC")
        try:
        #~ if True:
            self.db = Database(str(dp_path))
            if not self.db.exists():
                self.db.create()
                x_ind = WithAIndex(self.db.path, "a")
                self.db.add_index(x_ind)
            else:
                self.db.open()
        except:
        #~ else:
            print("Can't Open data base")
            self.db = None
    def __del__(self):
        """
        Delete instance and clear cache

        """
        self.cache = None
        if self.db:
            self.db.close()

    def is_already_checked(self, word):
        """ return if ``word`` is already cached"""
        try:
            return bool(self.db.get('a', word))
        except:
            return False
        #~ except: return False;

    def get_checked(self, word):
        """ return checked ``word`` form cache"""
        #~ word = bytes(word, "utf-8")
        if self.db:
            xxx = self.db.get('a', word, with_doc=True)
            yyy = xxx.get('doc', False)
            if yyy:
                return yyy.get('d', [])
            else: return []
        else: return []

    def add_checked(self, word, data):
        """ add checked ``word`` form cache"""
        #~ word = bytes(word, "utf-8")        
        idata = {"a": word, 'd': data}
        if self.db:
            self.db.insert(idata)

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
    print(d2)

if __name__ == "__main__":
    mainly()
