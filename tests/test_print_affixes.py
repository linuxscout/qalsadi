import sys
sys.path.append('../support')
import pyarabic.araby as araby
import tashaphyne.stem_const as tasha
import qalsadi.stem_verb_const as vconst
import qalsadi.stem_noun_const as nconst
import qalsadi.stem_stopwords_const as sconst
import repr as reprlib
class ArabicRepr(reprlib.Repr):
    """ A redifinition of repr fucntion,
    you can use it like this
    
    Example:
        >>> import pyarabic.arabrepr as arabrepr
        >>> arepr = arabrepr.ArabicRepr()
        >>> repr = arepr.repr
        >>> word = u"السلام عليكم ورحمة الله"
        >>> wordlist = word.split(" ")
        >>> print wordlist
        [u'\u0627\u0644\u0633\u0644\u0627\u0645', u'\u0639\u0644\u064a\u0643\u0645', u'\u0648\u0631\u062d\u0645\u0629', u'\u0627\u0644\u0644\u0647']
        >>> print repr(wordlist)
        [u'السلام', u'عليكم', u'ورحمة', u'الله']
    """
    def repr_unicode(self, obj, level):
        "Modify unicode display "
        return u"u'%s'" % obj
reprAr = ArabicRepr()
repra = reprAr.repr

def myprint(wordlist):
    JOINER = u', '
    l = set([araby.strip_tashkeel(x) for x in wordlist])
    print JOINER.join(sorted(l)).encode('utf8')

def print_automate(tree_dict):
    #~ print arrep.repr(tree_dict    )
    #add root node

    print repr(tree_dict    ).decode("unicode-escape")
    #~ print tree_dict#.encode('utf8')

# Default prefixes / affixes for Tashaphyne

print "Deafult Prefixes"
myprint(tasha.DEFAULT_PREFIX_LIST)

print  "Deafult suffixes"
myprint(tasha.DEFAULT_SUFFIX_LIST)

print  "Deafult inffixes"
myprint(tasha.DEFAULT_INFIX_LETTERS)


# prefixes / affixes for verbs
# syntaxic
print  "Verb Syntaxic Prefixes"
myprint(vconst.COMP_PREFIX_LIST)
print  "Verb Syntaxic Suffixes"
myprint(vconst.COMP_SUFFIX_LIST)

# morpholpgic
print  "Verb Morphologic Prefixes"
myprint(vconst.CONJ_PREFIX_LIST)
print  "Verb Morphologic Suffixes"
myprint(vconst.CONJ_SUFFIX_LIST)
# prefixes / affixes for nouns
# syntaxic
print  "Noun Syntaxic Prefixes"
myprint(nconst.COMP_PREFIX_LIST)
print  "Noun Syntaxic Suffixes"
myprint(nconst.COMP_SUFFIX_LIST)

# morpholpgic
print  "Noun Morphologic Prefixes"
myprint(nconst.CONJ_PREFIX_LIST)
print  "Noun Morphologic Suffixes"
myprint(nconst.CONJ_SUFFIX_LIST)

# prefixes / affixes for stopwords
# syntaxic
print  "StopWord Syntaxic Prefixes"
myprint(sconst.COMP_PREFIX_LIST)
print  "StopWord Syntaxic Suffixes"
myprint(sconst.COMP_SUFFIX_LIST)

# morpholpgic
print  "StopWord Morphologic Prefixes"
myprint(sconst.CONJ_PREFIX_LIST)
print  "StopWord Morphologic Suffixes"
myprint(sconst.CONJ_SUFFIX_LIST)



# print a customized automaton

import tashaphyne.stemming as tast
stemmer = tast.ArabicLightStemmer()


print "build tashaphyne automaton"
print "Tashaphyne prefixe automaton"
print_automate(stemmer.prefixes_tree)
print "Tashaphyne suffixe automaton"
print_automate(stemmer.suffixes_tree)

print "build verb automaton"
stemmer.set_prefix_list(vconst.COMP_PREFIX_LIST)
stemmer.set_suffix_list(vconst.COMP_SUFFIX_LIST)

print "prefixe automaton"
print_automate(stemmer.prefixes_tree)
print "suffixe automaton"
print_automate(stemmer.suffixes_tree)











