import sys

sys.path.append("../support")

import pyarabic.araby as araby
import tashaphyne.stem_const as tasha
import qalsadi.stem_verb_const as vconst
import qalsadi.stem_noun_const as nconst
import qalsadi.stem_stopwords_const as sconst
import repr as reprlib


class ArabicRepr(reprlib.Repr):
    """A redefinition of repr function.

    Example:
        >>> import pyarabic.arabrepr as arabrepr
        >>> arepr = arabrepr.ArabicRepr()
        >>> repr = arepr.repr
        >>> word = u"السلام عليكم ورحمة الله"
        >>> wordlist = word.split(" ")
        >>> print(wordlist)
        ['السلام', 'عليكم', 'ورحمة', 'الله']
        >>> print(repr(wordlist))
        [u'السلام', u'عليكم', u'ورحمة', u'الله']
    """

    def repr_unicode(self, obj, level):
        # Python 3 strings are Unicode by default
        return "u'%s'" % obj


reprAr = ArabicRepr()
repra = reprAr.repr


def myprint(wordlist):
    JOINER = ", "
    l = set([araby.strip_tashkeel(x) for x in wordlist])
    print(JOINER.join(sorted(l)))


def print_automate(tree_dict):
    # Use the custom repr for Unicode readability
    print(repra(tree_dict))


# --------------------------------------
# Demonstration
# --------------------------------------

print("Default Prefixes")
myprint(tasha.DEFAULT_PREFIX_LIST)

print("Default Suffixes")
myprint(tasha.DEFAULT_SUFFIX_LIST)

print("Default Infixes")
myprint(tasha.DEFAULT_INFIX_LETTERS)

# Verb affixes
print("Verb Syntaxic Prefixes")
myprint(vconst.COMP_PREFIX_LIST)
print("Verb Syntaxic Suffixes")
myprint(vconst.COMP_SUFFIX_LIST)

print("Verb Morphologic Prefixes")
myprint(vconst.CONJ_PREFIX_LIST)
print("Verb Morphologic Suffixes")
myprint(vconst.CONJ_SUFFIX_LIST)

# Noun affixes
print("Noun Syntaxic Prefixes")
myprint(nconst.COMP_PREFIX_LIST)
print("Noun Syntaxic Suffixes")
myprint(nconst.COMP_SUFFIX_LIST)

print("Noun Morphologic Prefixes")
myprint(nconst.CONJ_PREFIX_LIST)
print("Noun Morphologic Suffixes")
myprint(nconst.CONJ_SUFFIX_LIST)

# Stopword affixes
print("StopWord Syntaxic Prefixes")
myprint(sconst.COMP_PREFIX_LIST)
print("StopWord Syntaxic Suffixes")
myprint(sconst.COMP_SUFFIX_LIST)

print("StopWord Morphologic Prefixes")
myprint(sconst.CONJ_PREFIX_LIST)
print("StopWord Morphologic Suffixes")
myprint(sconst.CONJ_SUFFIX_LIST)

# Automata
import tashaphyne.stemming as tast

stemmer = tast.ArabicLightStemmer()

print("Build Tashaphyne automaton")
print("Tashaphyne prefix automaton")
print_automate(stemmer.prefixes_tree)

print("Tashaphyne suffix automaton")
print_automate(stemmer.suffixes_tree)

print("Build verb automaton")
stemmer.set_prefix_list(vconst.COMP_PREFIX_LIST)
stemmer.set_suffix_list(vconst.COMP_SUFFIX_LIST)

print("Prefix automaton")
print_automate(stemmer.prefixes_tree)

print("Suffix automaton")
print_automate(stemmer.suffixes_tree)
