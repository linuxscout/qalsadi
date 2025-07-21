#!/usr/bin/python
# -*- coding=utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        analex
# Purpose:     Arabic lexical analyser, provides feature to stem arabic
# words as noun, verb, stopword
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
# -------------------------------------------------------------------------------
"""Cache Module for analex"""


class Cache(object):
    """
    cache for word morphological analysis
    """

    def __init__(self, dp_path=False):
        """
        Create Analex Cache
        """
        self.cache = {
            "checkedWords": {},
            "FreqWords": {"noun": {}, "verb": {}, "stopword": {}},
        }
        self.db = False

    def __del__(self):
        """
        Delete instance and clear cache

        """
        self.cache = None

    def is_already_checked(self, word):
        """return if ``word`` is already cached"""
        return word in self.cache["checkedWords"]

    def get_checked(self, word):
        """return checked ``word`` form cache"""

        return self.cache["checkedWords"].get(word, {})

    def add_checked(self, word, data):
        """add checked ``word`` form cache"""
        if not word in self.cache["checkedWords"]:
            self.cache["checkedWords"][word] = data

    def exists_cache_freq(self, word, wordtype):
        """return if word exists in freq cache"""
        return word in self.cache["FreqWords"]

    def get_freq(self, originalword, wordtype):
        """return  ``word`` frequency form cache"""
        return self.cache["FreqWords"][wordtype].get(originalword, 0)

    def add_freq(self, original, wordtype, freq):
        """add   ``original`` frequency ``freq`` to cache"""
        self.cache["FreqWords"][wordtype][original] = freq


def mainly():
    """main function"""
    print("test")


if __name__ == "__main__":
    mainly()
