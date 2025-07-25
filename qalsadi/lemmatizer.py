﻿#!/usr/bin/python
# -*- coding=utf-8 -*-
# ------------------------------------------------------------------------
# Name:        lemmatizer
# Purpose:     Arabic Lemmatizer
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     26-08-2020
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
# ------------------------------------------------------------------------
"""
Syntaxic Analysis
"""

# ~ from operator import xor
# ~ import functools
# ~ import operator
import pprint

import pyarabic.araby as araby
from . import analex
from . import stemnode
from . import stemmedword
import functools
import operator


class Lemmatizer:
    """
    Arabic Lemmatizer
    """

    def __init__(self, cache_path=False):
        """ """
        # create analexer
        self.analexer = analex.Analex(cache_path)
        self.vocalized_lemma = False

    def __del__(self):
        pass

    def analyze(self, detailed_stemming_dict):
        """
        lemmatization  of stemming results.
        morphological Result is a list of stemmedword objects
        @param detailed_stemming_dict: detailed stemming dict.
        @type detailed_stemming_dict:list of list of stemmedword objects
        @return: lemmas.
        @rtype: list lemmas.
        """
        # create stemmed word instances
        stemmedsynwordlistlist = []
        stemnode_list = []
        # convert objects from stemmedWord to stemmedSynWord
        # in order to add syntaxic proprities
        for stemming_list in detailed_stemming_dict:
            # ~ for order in range(len(stemming_list)):
            # ~ stemming_list[order].order = order
            # create the stemnode object from tmplist
            stemnode_list.append(stemnode.StemNode(stemming_list, self.vocalized_lemma))
        return stemnode_list

    def get_lemmas(self, stemnode_list, pos="", return_pos=False, all=False):
        """
        Generate all lemmas from stemnode_list

        """
        lemmas = []
        for stnd in stemnode_list:
            # ~ lemmas.append(stnd.get_lemmas())
            if all:
                lemmas.append(stnd.get_lemmas())
            else:
                lemmas.append(stnd.get_lemma(pos=pos, return_pos=return_pos))
            # ~ lemmas.append([stnd.get_lemma(), stnd.get_lemmas()])

        return lemmas

    def decode(self, stemmed_synwordlistlist):
        """
        Decode objects result from analysis. helps to display result.
        @param stemmed_synwordlistlist: list of  list of StemmedSynWord.
        @type word_result: list of  list of StemmedSynWord
        @return: the list of list of dict to display.
        @rtype: list of  list of dict
        """
        flat_list = functools.reduce(operator.concat, stemmed_synwordlistlist)
        flat_list = [x.__dict__ for x in flat_list]
        return flat_list

    def display(self, stemmed_synwordlistlist):
        """
        display objects result from analysis
        @param stemmed_synwordlistlist: list of  list of StemmedSynWord.
        @type word_result: list of  list of StemmedSynWord
        """
        text = "["
        for rlist in stemmed_synwordlistlist:
            text += "\n\t["
            for item in rlist:
                text += "\n\t\t{"
                stmword = item.__dict__
                for key in sorted(stmword.keys()):
                    text += "\n\t\tu'%s' = u'%s'," % (key, stmword[key])
                text += "\n\t\t}"
            text += "\n\t]"
        text += "\n]"
        return text

    def pprint(self, stemmed_synwordlistlist):
        """
        print objects result from analysis
        @param stemmed_synwordlistlist: list of  list of StemmedSynWord.
        @type word_result: list of  list of StemmedSynWord
        """
        flat_list = self.decode(stemmed_synwordlistlist)
        pprint.pprint(flat_list)

    def analyze_text(self, text, vocalized_lemma=False):
        """
        Text Analysis syntacticly
        @param text: input text
        @type text: unicode
        """
        result = self.analexer.check_text(text)
        stemnodelist = self.analyze(result)
        return stemnodelist

    def set_vocalized_lemma(
        self,
    ):
        """
        set output lemma as vocalized
        @param text: input text
        @type text: unicode
        """
        self.vocalized_lemma = True

    def unset_vocalized_lemma(
        self,
    ):
        """
        set output lemma as vocalized
        @param text: input text
        @type text: unicode
        """
        self.vocalized_lemma = False

    def lemmatize_text(self, text, return_pos=False, pos="",all=False):
        """
        Lemmatize text
        @param text: input text
        @type text: unicode
        """

        result = self.analexer.check_text(text)
        stemnodelist = self.analyze(result)
        lemmas = self.get_lemmas(stemnodelist, return_pos=return_pos, pos=pos, all=all)
        return lemmas

    def lemmatize(self, word, return_pos=False, pos="", all=False):
        """
        Lemmatize text
        @param text: input text
        @type text: unicode
        """
        lemmasListOfList = self.lemmatize_text(word, return_pos=return_pos, pos=pos, all=all)
        # lemmas is a lis
        if lemmasListOfList:
            return lemmasListOfList[0]
            # if not all:
            #
            # else:
            #     return lemmas
        else:
            if return_pos:
                return ()
            else:
                return ""


def mainly():
    """
    main test
    """
    # #test syn
    text = "إلى البيت"
    result = []
    lemmer = Lemmatizer()
    result = lemmer.analyze_text(text)
    result = lemmer.morph(text)
    # the result contains objects
    pprint.pprint(result)


if __name__ == "__main__":
    mainly()
