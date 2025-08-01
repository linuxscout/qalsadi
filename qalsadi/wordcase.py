﻿#!/usr/bin/python
# -*- coding = utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        wordCase
# Purpose:     representat data analyzed given by morphoanalyzer Qalsadi
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     18-05-2014
# Copyright:   (c) Taha Zerrouki 2014
# Licence:     GPL
# -------------------------------------------------------------------------------
"""
wordCase represents the data resulted from the morpholocigal analysis
"""
if __name__ == "__main__":
    import sys

    sys.path.append("..")
import pyarabic.araby as araby
import pyarabic.arabrepr as arabrepr

arabicRepr = arabrepr.ArabicRepr()

# ~import analex_const


class WordCase:
    """
    wordCase represents the data resulted from the morpholocigal analysis
    """

    def __init__(self, result_dict=None):
        self.word = ("",)
        # ~"""input word"""
        self.word_nm = ("",)
        # ~"""input word with marks"""
        self.vocalized = ("",)
        # ~"""vocalized form of the input word """
        self.semivocalized = ("",)
        # ~"""vocalized form without inflection mark """
        self.unvocalized = ("",)
        # ~"""unvocalized form"""
        self.tags = ("",)
        # ~"""tags of affixes and tags extracted form lexical dictionary"""
        self.affix_key = "-"
        # ~affixTags = u""
        # ~"""tags of affixes"""
        # stemmed word attributes
        self.stem = ("",)
        # ~"""the word stem"""
        # Original word attributes from dictionary.
        self.original_tags = ("",)
        # ~""" tags extracted form lexical dictionary"""
        self.freq = (0,)
        # ~"""the word frequency from Word Frequency database """
        self.type = ("",)
        # ~""" the word type  """
        self.original = ""
        # ~""" original word from lexical dictionary"""
        self.lemma = ""
        # ~""" lemma word from lexical dictionary"""
        if result_dict:
            self.word = result_dict.get("word", "")
            self.vocalized = result_dict.get("vocalized", "")
            if not self.vocalized:
                self.vocalized = result_dict.get("word", "T")
            self.semivocalized = result_dict.get("semivocalized", "")
            self.stem = result_dict.get("stem", "")
            self.root = result_dict.get("root", "")
            self.affix = result_dict.get("affix", [])
            self.tags = ":".join(
                [result_dict.get("tags", ""), result_dict.get("originaltags", "")]
            )

            self.freq = result_dict.get("freq", "")
            self.type = result_dict.get("type", "")
            self.original = result_dict.get("original", "")
            self.lemma = result_dict.get("lemma", "")
            self.tense = result_dict.get("tense", "")
            self.pronoun = result_dict.get("pronoun", "")
            self.action = result_dict.get("action", "")

            self.object_type = result_dict.get("object_type", "")
            self.need = result_dict.get("need", "")
            self.number = result_dict.get("number", "")
            self.gender = result_dict.get("gender", "")
            self.person = result_dict.get("person", "")
            self.voice = result_dict.get("voice", "")
            self.mood = result_dict.get("mood", "")
            self.transitive = result_dict.get("transitive", False)

            # calculated attributes
            self.unvocalized = araby.strip_tashkeel(self.vocalized)
            # ~ self.word_nm = araby.strip_tashkeel(self.word)

    ######################################################################
    # { Attribut Functions
    ######################################################################
    def get(self, key, default=""):
        """
        get item by []
        """
        return self.__dict__.get(key, default)

    def __getitem__(self, key):
        """
        get item by key
        """
        return self.__dict__.get(key, "")

    def __setitem__(self, key, value):
        """
        setitem by key and value
        """
        self.__dict__[key] = value

    def __contains__(self, item):
        """
        in function
        """
        return item in self.__dict__

    def get_word(
        self,
    ):
        """
        Get the input word given by user
        @return: the given word.
        @rtype: unicode string
        """
        return self.word

    def set_word(self, newword):
        """
        Set the input word given by user
        @param newword: the new given word.
        @type newword: unicode string
        """
        self.word = newword

    def get_vocalized(
        self,
    ):
        """
        Get the vocalized form of the input word
        @return: the given vocalized.
        @rtype: unicode string
        """
        return self.vocalized

    def get_semivocalized(
        self,
    ):
        """
        Get the semi vocalized form of the input word with out inflection mark
        @return: the given vocalized.
        @rtype: unicode string
        """
        return self.semivocalized

    def is_unknown(
        self,
    ):
        """
        Get the vocalized form of the input word
        @return: the given vocalized.
        @rtype: unicode string
        """
        return "unknown" in self.type

    def set_vocalized(self, newvocalized):
        """
        Set the vocalized word
        @param newvocalized: the new given vocalized.
        @type newvocalized: unicode string
        """
        self.vocalized = newvocalized

    def get_stem(
        self,
    ):
        """
        Get the stem form of the input word
        @return: the given stem.
        @rtype: unicode string
        """
        return self.stem

    def set_stem(self, stem):
        """
        set the stem form of the input word
        @param stem: given stem
        @type stem: unicode
        @return: the given stem.
        @rtype: unicode string
        """
        self.stem = stem

    def get_tags(
        self,
    ):
        """
        Get the tags form of the input word
        @return: the given tags.
        @rtype: unicode string
        """
        return self.tags

    def set_tags(self, newtags):
        """
        Set the tags word
        @param newtags: the new given tags.
        @type newtags: unicode string
        """
        self.tags = newtags

    def get_affix(
        self,
    ):
        """
        Get the affix  form of the input word
        @return: the given affix.
        @rtype: unicode string
        """
        return self.affix

    def get_freq(
        self,
    ):
        """
        Get the freq form of the input word
        @return: the given freq.
        @rtype: unicode string
        """
        return self.freq

    def set_freq(self, newfreq):
        """
        Set the freq word
        @param newfreq: the new given freq.
        @type newfreq: unicode string
        """
        self.freq = newfreq

    def get_type(
        self,
    ):
        """
        Get the type form of the input word
        @return: the given type.
        @rtype: unicode string
        """
        return self.type

    def set_type(self, newtype):
        """
        Set the type word
        @param newtype: the new given type.
        @type newtype: unicode string
        """
        self.type = newtype

    def get_original(
        self,
    ):
        """
        Get the original form of the input word
        @return: the given original.
        @rtype: unicode string
        """
        return self.original

    def set_original(self, neworiginal):
        """
        Set the original word
        @param neworiginal: the new given original.
        @type neworiginal: unicode string
        """
        self.original = neworiginal

    def get_lemma(
        self,
    ):
        """
        Get the lemma form of the input word
        @return: the given lemma.
        @rtype: unicode string
        """
        return self.lemma

    def set_lemma(self, newlemma):
        """
        Set the lemma word
        @param newlemma: the new given lemma.
        @type newlemma: unicode string
        """
        self.lemma = newlemma

    ######################################################################
    # { Display Functions
    ######################################################################
    # ~ def __dict__(self, ):
    # ~ return self.__dict__

    def __repr__(self):
        """
        Display objects result from analysis
        @return: text
        @rtype : text
        """
        return arabicRepr.repr(self.__dict__)

    def dump(
        self,
    ):
        """
        Dump the word case as a simple list
        """
        return self.__dict__

    def load(self, a_list):
        """
        load word case attributes from a simple list stored in cache data base
        """
        self.__dict__ = a_list


if __name__ == "__main__":
    print("test")
    RDICT = {
        "word": "الحياة",  # input word
        "vocalized": "الْحَيَاةُ",  # vocalized form of the input word
        "procletic": "ال",  # the syntaxic pprefix called procletic
        "prefix": "",  # the conjugation or inflection prefix
        "stem": "حياة",  # the word stem
        "suffix": "ُ",  # the conjugation suffix of the word
        "encletic": "",  # the syntaxic suffix
        "tags": "تعريف::مرفوع*",
        # tags of affixes and tags extracted form lexical dictionary
        "freq": 0,  # the word frequency from Word Frequency database
        "root": "",  # the word root not yet used
        "template": "",  # the template وزن
        "type": "Noun:مصدر",  # the word type
        "original": "حَيَاةٌ",  # original word from lexical dictionary
        "lemma": "حَيَاةٌ",  # original word from lexical dictionary
        "syntax": "",  # used for syntaxique analysis porpos
        "semantic": "",
    }
    stmwrd = WordCase(RDICT)
    print(stmwrd.__dict__)

    stmwrd.set_word("4444")
    stmwrd.set_vocalized("4444")
    stmwrd.set_stem("4444")
    stmwrd.set_tags("4444")
    stmwrd.set_freq("4444")
    stmwrd.set_type("4444")
    stmwrd.set_original("4444")

    print(stmwrd)
