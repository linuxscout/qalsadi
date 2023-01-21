#!/usr/bin/python
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------
# Name:        stop_affixer
# Purpose:     Arabic lexical analyser, provides feature for
#~stemming arabic word as stop
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-------------------------------------------------------------------------
"""
    Arabic stop stemmer
"""
#~ import re
import pyarabic.araby as araby
import tashaphyne.stemming
import tashaphyne.normalize
import arramooz.stopwordsdictionaryclass as stopwordsdictionaryclass
from . import stem_stopwords_const as SSC





class stopword_affixer:
    """
        Arabic stop stemmer
    """
    def __init__(self,):
        """
        """
        self.procletics_tags = SSC.COMP_PREFIX_LIST_TAGS
        #~ # get prefixes
        self.prefixes = []
        # ~ # get suffixes
        self.suffixes_tags = SSC.CONJ_SUFFIX_LIST_TAGS
        # get enclitics:
        self.enclitics_tags = SSC.COMP_SUFFIX_LIST_TAGS
        # ~ self.enclitics = SSC.COMP_SUFFIX_LIST
        # ~ self.affixes = SSC.STOPWORDS_CONJUGATION_AFFIX
        # ~ self.clitics = SSC.COMP_stopword_AFFIXES
        # adjustement table 
        self.ajustment_table = SSC.AJUSTMENT

    @staticmethod
    def get_stem_variants(stem, suffix_nm):
        """
        Generate the Stop stem variants according to the affixes.
        For example مدرستي = >مدرست+ي = > مدرسة +ي.
        Return a list of possible cases.
        @param stem: the input stem.
        @type stem: unicode.
        @param suffix_nm: suffix (no mark).
        @type suffix_nm: unicode.
        @return: list of stem variants.
        @rtype: list of unicode.
        """
        #some cases must have some correction
        #determinate the  suffix types
        #~suffix = suffix_nm

        possible_stop_list = set([
            stem,
        ])
        if not suffix_nm or suffix_nm in (araby.YEH + araby.NOON,
                                          araby.WAW + araby.NOON):
            possible_stop = stem + araby.YEH
            possible_stop_list.add(possible_stop)
        if stem.endswith(araby.YEH):
            possible_stop = stem[:-1] + araby.ALEF_MAKSURA
            possible_stop_list.add(possible_stop)
        #to be validated
        validated_list = possible_stop_list
        return validated_list

    def get_suffix_variants(self, word, suffix, enclitic):
        """
        Get the suffix variant to be joined to the word.
        For example: word = مدرس, suffix = ة, encletic = ي.
        The suffix is converted to Teh.
        @param word: word found in dictionary.
        @type word: unicode.
        @param suffix: second level suffix.
        @type suffix: unicode.
        @param enclitic: first level suffix.
        @type enclitic: unicode.
        @return: variant of suffixes  (vocalized suffix and vocalized
        suffix without I'rab short mark).
        @rtype: (unicode, unicode)
        """
        enclitic_nm = araby.strip_tashkeel(enclitic)
        newsuffix = suffix  #default value
        #if the word ends by a haraka
        if not enclitic_nm and word[-1:] in (
                araby.ALEF_MAKSURA, araby.YEH,
                araby.ALEF) and araby.is_haraka(suffix):
            newsuffix = u""

        #gererate the suffix without I'rab short mark
        # here we lookup with given suffix because the new suffix is
        # changed and can be not found in table
        if u'متحرك' in self.suffixes_tags[suffix]['tags']:
            suffix_non_irab_mark = araby.strip_lastharaka(newsuffix)
        else:
            suffix_non_irab_mark = newsuffix

        return newsuffix, suffix_non_irab_mark

    @staticmethod
    def get_enclitic_variants(word, enclitic):
        """
        Get the enclitic variant to be joined to the word.
        For example: word = عن, suffix = , encletic = ني.
        The word and enclitic are geminated.
        @param word: word found in dictionary.
        @type word: unicode.
        @param enclitic: first level suffix.
        @type enclitic: unicode.
        @return: variant of suffixes  (vocalized suffix and vocalized
        suffix without I'rab short mark).
        @rtype: (unicode, unicode)
        """
        #enclitic_nm = araby.strip_tashkeel(enclitic)
        #newsuffix = suffix #default value
        #if the word ends by a haraka
        # الإدغام في النون والياء في مثل فيّ، إليّ، عنّا ، منّا
        if enclitic.startswith(araby.NOON) and word.endswith(araby.NOON):
            enclitic = enclitic[1:] + araby.SHADDA
            #~ print "xxxxxxxxxxx--1"
        if enclitic.startswith(araby.KASRA + araby.YEH) and word.endswith(
                araby.YEH):
            enclitic = enclitic[1:] + araby.SHADDA
            #~ print "xxxxxxxxxxx--2"

        return enclitic

    @staticmethod
    def get_word_variant(word, suffix):
        """
        Get the word variant to be joined to the suffix.
        For example: word = مدرسة, suffix = ي. The word is converted to مدرست.
        @param word: word found in dictionary.
        @type word: unicode.
        @param suffix: suffix ( firts or second level).
        @type suffix: unicode.
        @return: variant of word.
        @rtype: unicode.
        """
        word_stem = word
        suffix_nm = araby.strip_tashkeel(suffix)

        # تحويل الألف المقصورة إلى ياء في مثل إلى => إليك
        if word_stem.endswith(araby.ALEF_MAKSURA) and suffix_nm:
            if word_stem == u"سِوَى":
                word_stem = word_stem[:-1] + araby.ALEF
            else:
                word_stem = word_stem[:-1] + araby.YEH + araby.SUKUN
        # تحويل الهمزة حسب موقعها
        elif word_stem.endswith(araby.HAMZA) and suffix_nm:
            if suffix.startswith(araby.DAMMA):
                word_stem = word_stem[:-1] + araby.WAW_HAMZA
            elif suffix.startswith(araby.KASRA):
                word_stem = word_stem[:-1] + araby.YEH_HAMZA

        # this option is not used with stop words, because most of them are not inflected مبني
        #if the word ends by a haraka strip the haraka if the suffix is not null
        if suffix and suffix[0] in araby.HARAKAT:
            word_stem = araby.strip_lastharaka(word_stem)

        # الإدغام في النون والياء في مثل فيّ، إليّ، عنّا ، منّا
        if suffix.startswith(
                araby.NOON) and word.endswith(araby.NOON + araby.SUKUN):
            word_stem = araby.strip_lastharaka(word_stem)
        elif suffix.startswith(araby.KASRA + araby.YEH) and word.endswith(
                araby.YEH + araby.SUKUN):
            word_stem = araby.strip_lastharaka(word_stem)

        return word_stem

    def vocalize(self, stop, proclitic, suffix, enclitic):
        """
        Join the  stop and its affixes, and get the vocalized form
        @param stop: stop found in dictionary.
        @type stop: unicode.
        @param proclitic: first level prefix.
        @type proclitic: unicode.

        @param suffix: second level suffix.
        @type suffix: unicode.
        @param enclitic: first level suffix.
        @type enclitic: unicode.
        @return: vocalized word.
        @rtype: unicode.
        """
        # procletic have only an uniq vocalization in arabic
        proclitic_voc = self.procletics_tags[proclitic]["vocalized"][0]
        # enclitic can have many vocalization in arabic
        # like heh => عليهِ سواهُ
        # in this stage we consider only one,
        # the second situation is ajusted by vocalize_ajust
        enclitic_voc = self.enclitics_tags[enclitic]["vocalized"][0]
        suffix_voc = suffix  #CONJ_SUFFIX_LIST_TAGS[suffix]["vocalized"][0]

        # generate the word variant for some words witch ends by special
        #letters like Alef_maksura, or hamza,
        #the variant is influed by the suffix harakat,
        # for example إلي +ك = إلى+ك
        stop = self.get_word_variant(stop, suffix + enclitic)

        # generate the suffix variant. if the suffix is removed for some letters like
        # Alef Maqsura and Yeh
        # for example
        suffix_voc, suffix_non_irab_mark = self.get_suffix_variants(
            stop, suffix_voc, enclitic_voc)

        # generate the suffix variant. if the suffix is Yeh or Noon for geminating
        # for example عنّي = عن+ني
        enclitic_voc = self.get_enclitic_variants(stop, enclitic_voc)

        # generate the non vacalized end word: the vocalized word
        # without the I3rab Mark
        # if the suffix is a short haraka
        word_non_irab_mark = ''.join(
            [proclitic_voc, stop, suffix_non_irab_mark, enclitic_voc])


        word_vocalized = ''.join([proclitic_voc, stop, suffix_voc, enclitic_voc])
        
        # adjust vocalization
        word_non_irab_mark  = self.ajust_vocalization(word_non_irab_mark)            
        word_vocalized = self.ajust_vocalization(word_vocalized)
        return word_vocalized, word_non_irab_mark

    @staticmethod
    def verify_affix(word, list_seg, affix_list):
        """
        Verify possible affixes in the resulted segments according
        to the given affixes list.
        @param word: the input word.
        @type word: unicode.
        @param list_seg: list of word segments indexes (numbers).
        @type list_seg: list of pairs.
        @return: list of acceped segments.
        @rtype: list of pairs.
        """
        return [
            s for s in list_seg
            if '-'.join([word[:s[0]], word[s[1]:]]) in affix_list
        ]

    @staticmethod
    def validate_tags(stop_tuple, affix_tags, procletic, encletic_nm):
        """
        Test if the given word from dictionary is compabilbe with affixes tags.
        @param stop_tuple: the input word attributes given from dictionary.
        @type stop_tuple: dict.
        @param affix_tags: a list of tags given by affixes.
        @type affix_tags:list.
        @param procletic: first level prefix vocalized.
        @type procletic: unicode.
        @param encletic_nm: first level suffix vocalized.
        @type encletic_nm: unicode.
        @return: if the tags are compaatible.
        @rtype: Boolean.
        """
        procletic = araby.strip_tashkeel(procletic)
        #~ encletic = encletic_nm
        #~ suffix = suffix_nm

        if u"تعريف" in affix_tags and not stop_tuple['definition']:
            return False
        if u"تعريف" in affix_tags and stop_tuple['defined']:
            return False
        #~preposition
        if u'جر' in affix_tags and stop_tuple['is_inflected'] and not u"مجرور"  in affix_tags:
            return False
        if u'جر' in affix_tags and not stop_tuple['preposition']:
            return False
        if u"متحرك" in affix_tags and not stop_tuple['is_inflected']:
            return False

        if u"مضاف" in affix_tags and not stop_tuple['pronoun']:
            return False
        if u"مضاف" in affix_tags and stop_tuple['defined']:
            return False
        # حين تكون الأداة متحركة فهي تقبل الاتصال بياء المتكلم مباشرة
        if encletic_nm == araby.YEH and not stop_tuple['is_inflected']:
            return False
        # noon wiqaya نون الوقاية
        # حين تكون الأداة غير متحركة فهي تلزم  الاتصال بنون الوقاية قبل ياء المتكلم مباشرة
        if u"وقاية" in affix_tags and (stop_tuple['is_inflected']
                                       or stop_tuple['word'].endswith(araby.YEH)):
            return False
            #~interrog
        if u"استفهام" in affix_tags and not stop_tuple['interrog']:
            return False
            #~conjugation
            #~qasam

        if u"قسم" in affix_tags and not stop_tuple['qasam']:
            return False
            #~
            #~defined
            #~is_inflected
            #~tanwin
        if u"تنوين" in affix_tags and not stop_tuple['tanwin']:
            return False
            #~action
            #~object_type
            #~need
        return True

    def ajust_vocalization(self, vocalized):
        """
        ajust vocalization
        Temporary function
        @param vocalized: vocalized word.
        @type vocalized: unicode.
        @return: ajusted vocalized word.
        @rtype: unicode.
        """
        ajusted = self.ajustment_table.get(vocalized, vocalized)

        return ajusted
