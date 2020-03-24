#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  genAffixes.py
#  
#  Copyright 2019 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import itertools
import stem_noun_const as SNC
import stem_verb_const as SVC
from pyarabic.arabrepr import arepr
import pyarabic.araby as araby
import stem_noun
import stem_verb
def generate_noun_forms(word):
    """ generate all possible affixes"""
    # get procletics
    procletics = SNC.COMP_PREFIX_LIST
    #~ # get prefixes
    #~ prefixes =
    # get suffixes
    suffixes = SNC.CONJ_SUFFIX_LIST
    # get enclitics:
    enclitics = SNC.COMP_SUFFIX_LIST
    vocalizer = stem_noun.muwaled()
    noun_forms = []
    #~ word = u"قَصْدٌ"
    for element in itertools.product(procletics, suffixes, enclitics):
        proc = element[0]
        suff = element[1]
        enc = element[2]
        if u"-".join([proc, enc]) in SNC.COMP_NOUN_AFFIXES:
            if stem_noun.check_clitic_affix(proc, enc, suff):
                #~ print(arepr(element))
                newword = vocalizer.vocalize(word, proc, suff, enc)
                #~ print(arepr(newword))
            noun_forms.append(newword)
    return noun_forms                
def generate_verb_forms(word):
    """ generate all possible affixes"""
    # get procletics
    procletics = SVC.COMP_PREFIX_LIST
    #~ # get prefixes
    prefixes = SVC.CONJ_PREFIX_LIST
    # get suffixes
    suffixes = SVC.CONJ_SUFFIX_LIST
    # get enclitics:
    enclitics = SVC.COMP_SUFFIX_LIST
    vocalizer = stem_verb.muwaled()
    #~ word = u"قصد"
    verb_forms =[]
    for element in itertools.product(procletics,  prefixes, suffixes, enclitics):
        proc = element[0]
        pref = element[1]
        suff = element[2]
        enc = element[3]
        if u"-".join([pref, suff]) in SVC.VERBAL_CONJUGATION_AFFIX:
            if stem_verb.check_clitic_affix(proc, enc, pref+'-'+suff):
                #~ print(arepr(element))
                conj_verb = u"".join([pref, word,suff])
                newword = vocalizer.vocalize(conj_verb, proc,  enc)
                #~ print(arepr(newword))
                verb_forms.append(newword)
    return verb_forms
def generate_noun_affix_list():
    """ generate all affixes """
    word = u"قصد"    
    # generate all possible word forms
    noun_forms = generate_noun_forms(word)
    # remove diacritics
    list_affixes = [ araby.strip_tashkeel(d[0]) for d in noun_forms]
    # remove duplicated
    list_affixes = list(set(list_affixes))
    # remove stem and get only affixes
    list_affixes = [ x.replace(word,'-') for x in list_affixes]
     
    return list_affixes
def generate_verb_affix_list():
    """ generate all affixes """
    word = u"قصد"    
    # generate all possible word forms
    verb_forms = generate_verb_forms(word)
    # remove diacritics
    list_affixes = [ araby.strip_tashkeel(d[0]) for d in verb_forms]
    # remove duplicated
    list_affixes = list(set(list_affixes))
    # remove stem and get only affixes
    list_affixes = [ x.replace(word,'-') for x in list_affixes]
     
    return list_affixes
        
    
def main(args):
    word = u"قَصْدٌ"    
    noun_forms = generate_noun_forms(word)
    #~ print(arepr(noun_forms).replace('),', '),\n'))
    #~ print('************verb*****')
    word = u"قصد"    
    verb_forms =generate_verb_forms(word)
    #~ print(arepr(verb_forms).replace('),', '),\n'))
    
    print ('NOUN_AFFIX_LIST=')
    noun_affixes = generate_noun_affix_list()
    print(arepr(noun_affixes).replace(',', ',\n'))
    
    print('VERB_AFFIX_LIST=')
    verb_affixes = generate_verb_affix_list()
    print(arepr(verb_affixes).replace(',', ',\n'))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
