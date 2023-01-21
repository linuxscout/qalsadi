#!/usr/bin/python
# -*- coding=utf-8 -*-
#------------------------------------------------------------------------
# Name:        lemmatizer
# Purpose:     Arabic Lemmatizer 
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     26-08-2020
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#------------------------------------------------------------------------
"""
Syntaxic Analysis
"""

#~ from operator import xor
#~ import functools
#~ import operator
import pprint
import re
import pyarabic.araby as araby

class Templater:
    """
        Arabic Templater
    """
    def __init__(self, cache_path=False):
        """
        """
        # create analexer
        pass

    def extract_wazns(self, lemmas_roots_list):
        """
        Extract a list of wazns
        """
        wazns = []
        for lemmas, roots,word_type in lemmas_roots_list:
            if word_type == "stopword":
                continue
            lemmas = list(set(lemmas))
            roots = list(set(roots))
            for lemma in lemmas:
                
                for root in roots:
                    # uniq
                    wazns.append(self.extract_wazn(lemma, root))
        wazns = list(set(wazns))        
        return wazns
    @staticmethod        
    def is_invalid_wazn(wazn):
        """
        Test if the wazn is valid
        test invalid letters in a wazn, before make it a template
        here F, Ain, Lam, are coded 0,1,2
        """
        # حروف غير اشتقاقية
        if bool(re.search(r"[بثجحخذرزسشصضظعفقكلهء]",wazn)):
            return True
        # if the numbers are missplaced
        if bool(re.search(r"[^0][دط]",wazn)):
            return True    
        # if the numbers are missplaced
        if bool(re.search(r"[12].*0|2.*1",wazn)):
            return True
        return False
      
    def extract_wazn(self, lemma, root):
        """
        extract a wazn from a given lemma and root
        """
        if not root or len(root)<3:
            return ""
        else:
            wazn = lemma[::-1]
            if len(root) == 4:
                wazn = wazn.replace(root[2], "2",2)
            else:
                #  doubled root
                if root[2]==root[1]:
                    wazn = wazn.replace(root[2], "1",1)
                else:
                    wazn = wazn.replace(root[2], "2",1)                
            wazn = wazn.replace(root[1], "1",1)
            wazn = wazn.replace(root[0], "0",1)
            wazn = wazn[::-1]
            if self.is_invalid_wazn(wazn):
                return ""
            wazn = wazn.replace("2","ل")
            wazn = wazn.replace("1","ع")
            wazn = wazn.replace("0","ف")        
            return wazn         
        

            

def mainly():
    """
    main test
    """
    # #test syn
    text = u"إلى البيت"
    result = []
    lemmer = Lemmatizer()
    result = lemmer.analyze_text(text)
    # the result contains objects
    pprint.pprint(result)

if __name__ == "__main__":
    mainly()

