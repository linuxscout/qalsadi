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

from qalsadi.cachemanager import cache
from qalsadi.cachemanager import cache_codernity, cache_pickle, cache_pickledb


class Cache_Factory(object):
    """
    cache for word morphological analysis
    """

    def __init__(
        self,
    ):
        """
        Create Analex Cache
        """
        pass

    @staticmethod
    def factory(name, path):
        """
        create a cache according name with param path to store data
        """
        name = name.lower()
        if name == "memory":
            return cache.Cache()
        elif name == "pickle":
            return cache_pickle.Cache(path)
        elif name == "pickledb":
            return cache_pickledb.Cache(path)
        elif name in ("codernity", "codernitydb"):
            return cache_codernity.Cache(path)
        else:
            return cache.Cache()

    @staticmethod
    def list():
        """
        list available cache names
        """
        return [
            "",
            "memory",
            "pickle",
            "pickledb",
            "codernity",
        ]


def mainly():
    """main function"""
    print("test")


if __name__ == "__main__":
    mainly()
