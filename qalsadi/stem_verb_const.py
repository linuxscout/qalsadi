#!/usr/bin/python
# -*- coding=utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        stem_verb_const
# Purpose:     Arabic lexical analyser constants, provides feature for stemming arabic word as verb
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
# -------------------------------------------------------------------------------
"""
Arabic lexical analyser constants, provides feature for stemming arabic word as verb
"""
import re
import pyarabic.araby as ar
import libqutrub.verb_const as qutrubVerbConst

VERB_STAMP_PAT = re.compile(
    "[%s%s%s%s%s%s]" % (ar.ALEF, ar.YEH, ar.WAW, ar.ALEF_MAKSURA, ar.HAMZA, ar.SHADDA),
    re.UNICODE,
)
# Compound affixes
COMP_PREFIX_LETTERS = "أسلفو"
COMP_SUFFIX_LETTERS = "ينهكماو"
COMP_INFIX_LETTERS = ""
COMP_MAX_PREFIX = 3
COMP_MAX_SUFFIX = 6
COMP_MIN_STEM = 2
COMP_JOKER = "*"
"""COMP_PREFIX_LIST=set([
    "",
    ar.ALEF_HAMZA_ABOVE,
    ar.ALEF_HAMZA_ABOVE+ ar.FEH,
    ar.ALEF_HAMZA_ABOVE+ ar.FEH+ ar.LAM,
    ar.ALEF_HAMZA_ABOVE+ ar.FEH+ ar.SEEN,
    ar.ALEF_HAMZA_ABOVE+ ar.WAW,
    ar.ALEF_HAMZA_ABOVE+ ar.WAW+ ar.SEEN,
    ar.ALEF_HAMZA_ABOVE+ ar.WAW+ ar.LAM,
    ar.ALEF_HAMZA_ABOVE+ ar.LAM,
    ar.ALEF_HAMZA_ABOVE+ ar.SEEN,
    ar.FEH,
    ar.FEH+ ar.LAM,
    ar.FEH+ ar.SEEN,
    ar.WAW,
    ar.WAW+ ar.LAM,
    ar.WAW+ ar.SEEN,
    ar.LAM,
    ar.SEEN,
    ]);
COMP_SUFFIX_LIST=set(["",
    ar.YEH,
    ar.NOON+ ar.YEH,
    ar.NOON+ ar.ALEF,
    ar.KAF,
    ar.KAF+ ar.MEEM+ ar.ALEF,
    ar.KAF+ ar.MEEM,
    ar.KAF+ ar.NOON,
    ar.HEH,
    ar.HEH+ ar.ALEF,
    ar.HEH+ ar.MEEM+ ar.ALEF,
    ar.HEH+ ar.MEEM,
    ar.HEH+ ar.NOON,
# To double MAf3ool suffix
    u'يي',
    u'يني',
    u'ينا',
    u'يك',
    u'يكما',
    u'يكم',
    u'يكن',
    u'يه',
    u'يها',
    u'يهما',
    u'يهم',
    u'يهن',
    u'نيي',
    u'نيني',
    u'نينا',
    u'نيك',
    u'نيكما',
    u'نيكم',
    u'نيكن',
    u'نيه',
    u'نيها',
    u'نيهما',
    u'نيهم',
    u'نيهن',
    u'ناي',
    u'ناني',
    u'نانا',
    u'ناك',
    u'ناكما',
    u'ناكم',
    u'ناكن',
    u'ناه',
    u'ناها',
    u'ناهما',
    u'ناهم',
    u'ناهن',
    u'كي',
    u'كني',
    u'كنا',
    u'كك',
    u'ككما',
    u'ككم',
    u'ككن',
    u'كه',
    u'كها',
    u'كهما',
    u'كهم',
    u'كهن',
    u'كماي',
    u'كماني',
    u'كمانا',
    u'كماك',
    u'كماكما',
    u'كماكم',
    u'كماكن',
    u'كماه',
    u'كماها',
    u'كماهما',
    u'كماهم',
    u'كماهن',
    u'كموي',
    u'كموني',
    u'كمونا',
    u'كموك',
    u'كموكما',
    u'كموكم',
    u'كموكن',
    u'كموه',
    u'كموها',
    u'كموهما',
    u'كموهم',
    u'كموهن',
    u'كني',
    u'كنني',
    u'كننا',
    u'كنك',
    u'كنكما',
    u'كنكم',
    u'كنكن',
    u'كنه',
    u'كنها',
    u'كنهما',
    u'كنهم',
    u'كنهن',
    u'هي',
    u'هني',
    u'هنا',
    u'هك',
    u'هكما',
    u'هكم',
    u'هكن',
    u'هه',
    u'هها',
    u'ههما',
    u'ههم',
    u'ههن',
    u'هاي',
    u'هاني',
    u'هانا',
    u'هاك',
    u'هاكما',
    u'هاكم',
    u'هاكن',
    u'هاه',
    u'هاها',
    u'هاهما',
    u'هاهم',
    u'هاهن',
    u'هماي',
    u'هماني',
    u'همانا',
    u'هماك',
    u'هماكما',
    u'هماكم',
    u'هماكن',
    u'هماه',
    u'هماها',
    u'هماهما',
    u'هماهم',
    u'هماهن',
    u'هموي',
    u'هموني',
    u'همونا',
    u'هموك',
    u'هموكما',
    u'هموكم',
    u'هموكن',
    u'هموه',
    u'هموها',
    u'هموهما',
    u'هموهم',
    u'هموهن',
    u'هني',
    u'هنني',
    u'هننا',
    u'هنك',
    u'هنكما',
    u'هنكم',
    u'هنكن',
    u'هنه',
    u'هنها',
    u'هنهما',
    u'هنهم',
    u'هنهن',
    ]);
"""
COMP_PREFIX_LIST_TAGS = {
    "": {"tags": ("",), "vocalized": ("",)},
    "أ": {"tags": ("استفهام",), "vocalized": ("أَ",)},
    "أس": {"tags": ("استفهام", "استقبال"), "vocalized": ("أَسَ",)},
    "و": {"tags": ("عطف",), "vocalized": ("وَ",)},
    "وس": {"tags": ("عطف", "استقبال"), "vocalized": ("وَسَ",)},
    "أو": {"tags": ("استفهام",), "vocalized": ("أَوََ",)},
    "أوس": {"tags": ("استفهام", "استقبال"), "vocalized": ("أَوََسَ",)},
    "أول": {"tags": ("استفهام", "عطف", "لام"), "vocalized": ("أَوَلََ",)},
    "س": {"tags": ("استقبال",), "vocalized": ("سَ",)},
    "ف": {"tags": ("عطف",), "vocalized": ("فَ",)},
    "فس": {"tags": ("عطف", "استقبال"), "vocalized": ("فَسَ",)},
    "أف": {
        "tags": (
            "استفهام",
            "عطف",
        ),
        "vocalized": ("أَفَ",),
    },
    "أفس": {
        "tags": (
            "استفهام",
            "عطف",
            "استقبال",
        ),
        "vocalized": ("أَفَسَ",),
    },
    "ل": {"tags": ("لام",), "vocalized": ("لِ", "لَ")},
    "ول": {"tags": ("عطف", "لام"), "vocalized": ("وَلََ",)},
    "فل": {"tags": ("عطف", "لام"), "vocalized": ("فَلَ", "فَلِ", "فَلْ")},
}
COMP_PREFIX_LIST = list(COMP_PREFIX_LIST_TAGS.keys())
COMP_SUFFIX_LIST_TAGS = {
    "": {"tags": ("",), "vocalized": ("",)},
    "ني": {
        "tags": ("مفعول به",),
        "vocalized": ("نِي",),
    },
    "ي": {
        "tags": ("مفعول به",),
        "vocalized": ("ي",),
    },
    "ك": {
        "tags": ("مفعول به",),
        "vocalized": (
            "كَ",
            "كِ",
        ),
    },
    "ه": {
        "tags": ("مفعول به",),
        "vocalized": ("هُ",),
    },
    "كم": {
        "tags": ("مفعول به",),
        "vocalized": ("كُمْ", "كُمُ"),
    },
    "كن": {
        "tags": ("مفعول به",),
        "vocalized": ("كُنَّ",),
    },
    "ها": {
        "tags": ("مفعول به",),
        "vocalized": ("هَا",),
    },
    "هم": {
        "tags": ("مفعول به",),
        "vocalized": ("هُمْ", "هُمُ"),
    },
    "هن": {
        "tags": ("مفعول به",),
        "vocalized": ("هُنَّ",),
    },
    "نا": {
        "tags": ("مفعول به",),
        "vocalized": ("نَا",),
    },
    "كما": {
        "tags": ("مفعول به",),
        "vocalized": ("كُمَا",),
    },
    "هما": {
        "tags": ("مفعول به",),
        "vocalized": ("هُمَا",),
    },
}
COMP_SUFFIX_LIST = list(COMP_SUFFIX_LIST_TAGS.keys())

CONJ_PREFIX_LETTERS = "تأنياء"
CONJ_SUFFIX_LETTERS = "متواني"
CONJ_INFIX_LETTERS = ""
CONJ_MAX_PREFIX = 1
CONJ_MAX_SUFFIX = 3
CONJ_MIN_STEM = 2
CONJ_JOKER = "*"
CONJ_PREFIX_LIST = ("", ar.ALEF, ar.YEH, ar.TEH, ar.NOON, ar.ALEF_HAMZA_ABOVE, ar.HAMZA)
CONJ_SUFFIX_LIST = (
    "",
    ar.TEH,
    ar.TEH + ar.ALEF,
    ar.TEH + ar.MEEM,
    ar.TEH + ar.MEEM + ar.WAW,
    ar.TEH + ar.MEEM + ar.ALEF,
    ar.TEH + ar.NOON,
    ar.ALEF,
    ar.NOON,
    ar.NOON + ar.ALEF,
    ar.ALEF + ar.NOON,
    ar.WAW + ar.ALEF,
    ar.WAW + ar.NOON,
    ar.WAW,
    ar.YEH,
    ar.YEH + ar.NOON,
)
SUFFIX_LIST_STRIPOUS = set(
    [
        "",
        ar.TEH,
        ar.TEH + ar.ALEF,
        ar.WAW + ar.ALEF,
        ar.WAW + ar.NOON,
        ar.WAW,
        ar.YEH,
        ar.YEH + ar.NOON,
    ]
)
SUFFIX_LIST_SAKEN = set(
    [
        "",
        ar.TEH,
        # حالة خاصة مع الفعل الناقص
        ar.TEH + ar.ALEF,
        ar.TEH + ar.MEEM,
        # TEH+MEEM+WAW,
        ar.TEH + ar.MEEM + ar.ALEF,
        ar.TEH + ar.NOON,
        ar.NOON,
        ar.NOON + ar.ALEF,
    ]
)
SUFFIX_LIST_VOWELED = set(
    [
        "",
        ar.ALEF,
        ar.ALEF + ar.NOON,
        ar.NOON,
        ar.TEH,
        ar.TEH + ar.NOON,
        ar.TEH + ar.MEEM,
    ]
)
PREFIX_LIST_STRIPOUS = (ar.YEH, ar.TEH, ar.NOON, ar.ALEF_HAMZA_ABOVE, ar.HAMZA)
VERBAL_CONJUGATION_AFFIX = set(
    [
        "-",
        "-ا",
        "-ت",
        "-تا",
        "-تم",
        "-تما",
        "-تنّ",
        "-تن",
        "-ن",
        "-نا",
        "-وا",
        "أ-",
        "أ-نّ",
        "ا-",
        "ا-ا",
        "ا-انّ",
        "ا-ن",
        "ا-نانّ",
        "ا-نّ",
        "ا-وا",
        "ا-ي",
        "ت-",
        "ت-ا",
        "ت-ان",
        "ت-انّ",
        "ت-ن",
        "ت-نانّ",
        "ت-نّ",
        "ت-وا",
        "ت-ون",
        "ت-ي",
        "ت-ين",
        "ن-",
        "ن-نّ",
        "ي-",
        "ي-ا",
        "ي-ان",
        "ي-انّ",
        "ي-ن",
        "ي-نانّ",
        "ي-نّ",
        "ي-وا",
        "ي-ون",
        # تمو
        ##u"-تمو",
        ##u'ي-و',
        ##u'ت-و',
        ##u'ا-و',
        ##u'-و',
        "-ي",
        # added confirmed
        "-تن",
        "أ-ن",
        "ا-ان",
        "ا-نان",
        "ا-ن",
        "ت-ان",
        "ت-نان",
        "ت-ن",
        "ن-ن",
        "ي-ان",
        "ي-نان",
        "ي-ن",
        "ء-ن",
        "ء-",
    ]
)
TABLE_DOUBLE_TRANSITIVE_SUFFIX = {
    "يك": {"first": "ي", "second": "ي"},
    "يكما": {"first": "ي", "second": "ي"},
    "يكم": {"first": "ي", "second": "ي"},
    "يكن": {"first": "ي", "second": "ي"},
    "يه": {"first": "ي", "second": "ي"},
    "يها": {"first": "ي", "second": "ي"},
    "يهما": {"first": "ي", "second": "ي"},
    "يهم": {"first": "ي", "second": "ي"},
    "يهن": {"first": "ي", "second": "ي"},
    "نيي": {"first": "ني", "second": "ني"},
    "نيني": {"first": "ني", "second": "ني"},
    "نينا": {"first": "ني", "second": "ني"},
    "نيك": {"first": "ني", "second": "ني"},
    "نيكما": {"first": "ني", "second": "ني"},
    "نيكم": {"first": "ني", "second": "ني"},
    "نيكن": {"first": "ني", "second": "ني"},
    "نيه": {"first": "ني", "second": "ني"},
    "نيها": {"first": "ني", "second": "ني"},
    "نيهما": {"first": "ني", "second": "ني"},
    "نيهم": {"first": "ني", "second": "ني"},
    "نيهن": {"first": "ني", "second": "ني"},
    "ناي": {"first": "نا", "second": "نا"},
    "ناني": {"first": "نا", "second": "نا"},
    "نانا": {"first": "نا", "second": "نا"},
    "ناك": {"first": "نا", "second": "نا"},
    "ناكما": {"first": "نا", "second": "نا"},
    "ناكم": {"first": "نا", "second": "نا"},
    "ناكن": {"first": "نا", "second": "نا"},
    "ناه": {"first": "نا", "second": "نا"},
    "ناها": {"first": "نا", "second": "نا"},
    "ناهما": {"first": "نا", "second": "نا"},
    "ناهم": {"first": "نا", "second": "نا"},
    "ناهن": {"first": "نا", "second": "نا"},
    "كي": {"first": "ك", "second": "ك"},
    "كنا": {"first": "ك", "second": "ك"},
    ##u'كك':{'first':u'ك','second':u'ك'},
    ##u'ككما':{'first':u'ك','second':u'ك'},
    ##u'ككم':{'first':u'ك','second':u'ك'},
    ##u'ككن':{'first':u'ك','second':u'ك'},
    "كه": {"first": "ك", "second": "ك"},
    "كها": {"first": "ك", "second": "ك"},
    "كهما": {"first": "ك", "second": "ك"},
    "كهم": {"first": "ك", "second": "ك"},
    "كهن": {"first": "ك", "second": "ك"},
    "كماي": {"first": "كما", "second": "كما"},
    "كماني": {"first": "كما", "second": "كما"},
    "كمانا": {"first": "كما", "second": "كما"},
    ##u'كماك':{'first':u'كما','second':u'كما'},
    ##u'كماكما':{'first':u'كما','second':u'كما'},
    ##u'كماكم':{'first':u'كما','second':u'كما'},
    ##u'كماكن':{'first':u'كما','second':u'كما'},
    "كماه": {"first": "كما", "second": "كما"},
    "كماها": {"first": "كما", "second": "كما"},
    "كماهما": {"first": "كما", "second": "كما"},
    "كماهم": {"first": "كما", "second": "كما"},
    "كماهن": {"first": "كما", "second": "كما"},
    "كموي": {"first": "كم", "second": "كم"},
    "كموني": {"first": "كم", "second": "كم"},
    "كمونا": {"first": "كم", "second": "كم"},
    "كموك": {"first": "كم", "second": "كم"},
    "كموكما": {"first": "كم", "second": "كم"},
    "كموكم": {"first": "كم", "second": "كم"},
    "كموكن": {"first": "كم", "second": "كم"},
    "كموه": {"first": "كم", "second": "كم"},
    "كموها": {"first": "كم", "second": "كم"},
    "كموهما": {"first": "كم", "second": "كم"},
    "كموهم": {"first": "كم", "second": "كم"},
    "كموهن": {"first": "كم", "second": "كم"},
    "كني": {"first": "كن", "second": "كن"},
    "كنني": {"first": "كن", "second": "كن"},
    "كننا": {"first": "كن", "second": "كن"},
    "كنك": {"first": "كن", "second": "كن"},
    "كنكما": {"first": "كن", "second": "كن"},
    "كنكم": {"first": "كن", "second": "كن"},
    "كنكن": {"first": "كن", "second": "كن"},
    "كنه": {"first": "كن", "second": "كن"},
    "كنها": {"first": "كن", "second": "كن"},
    "كنهما": {"first": "كن", "second": "كن"},
    "كنهم": {"first": "كن", "second": "كن"},
    "كنهن": {"first": "كن", "second": "كن"},
    "هي": {"first": "ه", "second": "ه"},
    "هنا": {"first": "ه", "second": "ه"},
    "هك": {"first": "ه", "second": "ه"},
    "هكما": {"first": "ه", "second": "ه"},
    "هكم": {"first": "ه", "second": "ه"},
    "هكن": {"first": "ه", "second": "ه"},
    "هه": {"first": "ه", "second": "ه"},
    "هها": {"first": "ه", "second": "ه"},
    "ههما": {"first": "ه", "second": "ه"},
    "ههم": {"first": "ه", "second": "ه"},
    "ههن": {"first": "ه", "second": "ه"},
    "هاي": {"first": "ها", "second": "ها"},
    "هاني": {"first": "ها", "second": "ها"},
    "هانا": {"first": "ها", "second": "ها"},
    "هاك": {"first": "ها", "second": "ها"},
    "هاكما": {"first": "ها", "second": "ها"},
    "هاكم": {"first": "ها", "second": "ها"},
    "هاكن": {"first": "ها", "second": "ها"},
    "هاه": {"first": "ها", "second": "ها"},
    "هاها": {"first": "ها", "second": "ها"},
    "هاهما": {"first": "ها", "second": "ها"},
    "هاهم": {"first": "ها", "second": "ها"},
    "هاهن": {"first": "ها", "second": "ها"},
    "هماي": {"first": "هما", "second": "هما"},
    "هماني": {"first": "هما", "second": "هما"},
    "همانا": {"first": "هما", "second": "هما"},
    "هماك": {"first": "هما", "second": "هما"},
    "هماكما": {"first": "هما", "second": "هما"},
    "هماكم": {"first": "هما", "second": "هما"},
    "هماكن": {"first": "هما", "second": "هما"},
    "هماه": {"first": "هما", "second": "هما"},
    "هماها": {"first": "هما", "second": "هما"},
    "هماهما": {"first": "هما", "second": "هما"},
    "هماهم": {"first": "هما", "second": "هما"},
    "هماهن": {"first": "هما", "second": "هما"},
    "هموي": {"first": "هم", "second": "هم"},
    "هموني": {"first": "هم", "second": "هم"},
    "همونا": {"first": "هم", "second": "هم"},
    "هموك": {"first": "هم", "second": "هم"},
    "هموكما": {"first": "هم", "second": "هم"},
    "هموكم": {"first": "هم", "second": "هم"},
    "هموكن": {"first": "هم", "second": "هم"},
    "هموه": {"first": "هم", "second": "هم"},
    "هموها": {"first": "هم", "second": "هم"},
    "هموهما": {"first": "هم", "second": "هم"},
    "هموهم": {"first": "هم", "second": "هم"},
    "هموهن": {"first": "هم", "second": "هم"},
    "هني": {"first": "هن", "second": "هن"},
    "هنني": {"first": "هن", "second": "هن"},
    "هننا": {"first": "هن", "second": "هن"},
    "هنك": {"first": "هن", "second": "هن"},
    "هنكما": {"first": "هن", "second": "هن"},
    "هنكم": {"first": "هن", "second": "هن"},
    "هنكن": {"first": "هن", "second": "هن"},
    "هنه": {"first": "هن", "second": "هن"},
    "هنها": {"first": "هن", "second": "هن"},
    "هنهما": {"first": "هن", "second": "هن"},
    "هنهم": {"first": "هن", "second": "هن"},
    "هنهن": {"first": "هن", "second": "هن"},
}
# created on fly at the program start, from the Table_affix
TABLE_AFFIX_INDEX = {
    "": {
        "pronouns": qutrubVerbConst.PronounsTable,
        "tenses": [
            qutrubVerbConst.TenseJussiveFuture,
            qutrubVerbConst.TensePassiveConfirmedFuture,
            qutrubVerbConst.TensePassiveFuture,
            qutrubVerbConst.TensePassiveJussiveFuture,
            qutrubVerbConst.TensePassivePast,
            qutrubVerbConst.TensePassiveSubjunctiveFuture,
            qutrubVerbConst.TensePast,
            qutrubVerbConst.TenseSubjunctiveFuture,
            qutrubVerbConst.TenseConfirmedFuture,
            qutrubVerbConst.TenseConfirmedImperative,
            qutrubVerbConst.TenseFuture,
            qutrubVerbConst.TenseImperative,
        ],
    },
}
TABLE_AFFIX = {
    "ت-ون": [
        ("المضارع المجهول", "أنتم"),
        ("المضارع المعلوم", "أنتم"),
    ],
    "-ن": [
        ("الماضي المجهول", "هن"),
        ("الأمر المؤكد", "أنتِ"),
        ("الأمر المؤكد", "أنت"),
        ("الأمر المؤكد", "أنتم"),
        ("الماضي المعلوم", "هن"),
        ("الأمر", "أنتن"),
    ],
    "أ-": [
        ("المضارع المنصوب", "أنا"),
        ("المضارع المجهول المجزوم", "أنا"),
        ("المضارع المجهول", "أنا"),
        ("المضارع المعلوم", "أنا"),
        ("المضارع المجزوم", "أنا"),
        ("المضارع المجهول المنصوب", "أنا"),
    ],
    "ت-نان": [
        ("المضارع المؤكد الثقيل", "أنتن"),
        ("المضارع المؤكد الثقيل المجهول ", "أنتن"),
    ],
    "-ي": [
        ("الأمر", "أنتِ"),
    ],
    "ت-ان": [
        ("المضارع المؤكد الثقيل", "أنتما مؤ"),
        ("المضارع المؤكد الثقيل", "أنتما"),
        ("المضارع المؤكد الثقيل", "هما مؤ"),
        ("المضارع المجهول", "أنتما مؤ"),
        ("المضارع المجهول", "أنتما"),
        ("المضارع المجهول", "هما مؤ"),
        ("المضارع المعلوم", "أنتما مؤ"),
        ("المضارع المعلوم", "أنتما"),
        ("المضارع المعلوم", "هما مؤ"),
        ("المضارع المؤكد الثقيل المجهول ", "أنتما مؤ"),
        ("المضارع المؤكد الثقيل المجهول ", "أنتما"),
        ("المضارع المؤكد الثقيل المجهول ", "هما مؤ"),
    ],
    "ت-ا": [
        ("المضارع المنصوب", "أنتما مؤ"),
        ("المضارع المنصوب", "أنتما"),
        ("المضارع المنصوب", "هما مؤ"),
        ("المضارع المجهول المجزوم", "أنتما مؤ"),
        ("المضارع المجهول المجزوم", "أنتما"),
        ("المضارع المجهول المجزوم", "هما مؤ"),
        ("المضارع المجزوم", "أنتما مؤ"),
        ("المضارع المجزوم", "أنتما"),
        ("المضارع المجزوم", "هما مؤ"),
        ("المضارع المجهول المنصوب", "أنتما مؤ"),
        ("المضارع المجهول المنصوب", "أنتما"),
        ("المضارع المجهول المنصوب", "هما مؤ"),
    ],
    "-وا": [
        ("الماضي المجهول", "هم"),
        ("الماضي المعلوم", "هم"),
        ("الأمر", "أنتم"),
    ],
    "-تا": [
        ("الماضي المجهول", "هما مؤ"),
        ("الماضي المعلوم", "هما مؤ"),
    ],
    "ي-ون": [
        ("المضارع المجهول", "هم"),
        ("المضارع المعلوم", "هم"),
    ],
    "-": [
        ("الماضي المجهول", "هو"),
        ("الماضي المعلوم", "هو"),
        ("الأمر", "أنت"),
    ],
    "ي-نان": [
        ("المضارع المؤكد الثقيل", "هن"),
        ("المضارع المؤكد الثقيل المجهول ", "هن"),
    ],
    "ي-ا": [
        ("المضارع المنصوب", "هما"),
        ("المضارع المجهول المجزوم", "هما"),
        ("المضارع المجزوم", "هما"),
        ("المضارع المجهول المنصوب", "هما"),
    ],
    "-تم": [
        ("الماضي المجهول", "أنتم"),
        ("الماضي المعلوم", "أنتم"),
    ],
    "-تن": [
        ("الماضي المجهول", "أنتن"),
        ("الماضي المعلوم", "أنتن"),
    ],
    "ي-ان": [
        ("المضارع المؤكد الثقيل", "هما"),
        ("المضارع المجهول", "هما"),
        ("المضارع المعلوم", "هما"),
        ("المضارع المؤكد الثقيل المجهول ", "هما"),
    ],
    "ي-وا": [
        ("المضارع المنصوب", "هم"),
        ("المضارع المجهول المجزوم", "هم"),
        ("المضارع المجزوم", "هم"),
        ("المضارع المجهول المنصوب", "هم"),
    ],
    "أ-ن": [
        ("المضارع المؤكد الثقيل", "أنا"),
        ("المضارع المؤكد الثقيل المجهول ", "أنا"),
    ],
    "ت-": [
        ("المضارع المنصوب", "أنت"),
        ("المضارع المنصوب", "هي"),
        ("المضارع المجهول المجزوم", "أنت"),
        ("المضارع المجهول المجزوم", "هي"),
        ("المضارع المجهول", "أنت"),
        ("المضارع المجهول", "هي"),
        ("المضارع المعلوم", "أنت"),
        ("المضارع المعلوم", "هي"),
        ("المضارع المجزوم", "أنت"),
        ("المضارع المجزوم", "هي"),
        ("المضارع المجهول المنصوب", "أنت"),
        ("المضارع المجهول المنصوب", "هي"),
    ],
    "ت-ين": [
        ("المضارع المجهول", "أنتِ"),
        ("المضارع المعلوم", "أنتِ"),
    ],
    "ي-ن": [
        ("المضارع المنصوب", "هن"),
        ("المضارع المؤكد الثقيل", "هم"),
        ("المضارع المؤكد الثقيل", "هو"),
        ("المضارع المجهول المجزوم", "هن"),
        ("المضارع المجهول", "هن"),
        ("المضارع المعلوم", "هن"),
        ("المضارع المجزوم", "هن"),
        ("المضارع المجهول المنصوب", "هن"),
        ("المضارع المؤكد الثقيل المجهول ", "هم"),
        ("المضارع المؤكد الثقيل المجهول ", "هو"),
    ],
    "-تما": [
        ("الماضي المجهول", "أنتما مؤ"),
        ("الماضي المجهول", "أنتما"),
        ("الماضي المعلوم", "أنتما مؤ"),
        ("الماضي المعلوم", "أنتما"),
    ],
    "-ا": [
        ("الماضي المجهول", "هما"),
        ("الماضي المعلوم", "هما"),
        ("الأمر", "أنتما مؤ"),
        ("الأمر", "أنتما"),
    ],
    "-ان": [
        ("الأمر المؤكد", "أنتما مؤ"),
        ("الأمر المؤكد", "أنتما"),
    ],
    "ت-وا": [
        ("المضارع المنصوب", "أنتم"),
        ("المضارع المجهول المجزوم", "أنتم"),
        ("المضارع المجزوم", "أنتم"),
        ("المضارع المجهول المنصوب", "أنتم"),
    ],
    "-نا": [
        ("الماضي المجهول", "نحن"),
        ("الماضي المعلوم", "نحن"),
    ],
    "-نان": [
        ("الأمر المؤكد", "أنتن"),
    ],
    "-ت": [
        ("الماضي المجهول", "أنتِ"),
        ("الماضي المجهول", "أنت"),
        ("الماضي المجهول", "أنا"),
        ("الماضي المجهول", "هي"),
        ("الماضي المعلوم", "أنتِ"),
        ("الماضي المعلوم", "أنت"),
        ("الماضي المعلوم", "أنا"),
        ("الماضي المعلوم", "هي"),
    ],
    "ت-ي": [
        ("المضارع المنصوب", "أنتِ"),
        ("المضارع المجهول المجزوم", "أنتِ"),
        ("المضارع المجزوم", "أنتِ"),
        ("المضارع المجهول المنصوب", "أنتِ"),
    ],
    "ي-": [
        ("المضارع المنصوب", "هو"),
        ("المضارع المجهول المجزوم", "هو"),
        ("المضارع المجهول", "هو"),
        ("المضارع المعلوم", "هو"),
        ("المضارع المجزوم", "هو"),
        ("المضارع المجهول المنصوب", "هو"),
    ],
    "ن-ن": [
        ("المضارع المؤكد الثقيل", "نحن"),
        ("المضارع المؤكد الثقيل المجهول ", "نحن"),
    ],
    "ت-ن": [
        ("المضارع المنصوب", "أنتن"),
        ("المضارع المؤكد الثقيل", "أنتِ"),
        ("المضارع المؤكد الثقيل", "أنت"),
        ("المضارع المؤكد الثقيل", "أنتم"),
        ("المضارع المؤكد الثقيل", "هي"),
        ("المضارع المجهول المجزوم", "أنتن"),
        ("المضارع المجهول", "أنتن"),
        ("المضارع المعلوم", "أنتن"),
        ("المضارع المجزوم", "أنتن"),
        ("المضارع المجهول المنصوب", "أنتن"),
        ("المضارع المؤكد الثقيل المجهول ", "أنتِ"),
        ("المضارع المؤكد الثقيل المجهول ", "أنت"),
        ("المضارع المؤكد الثقيل المجهول ", "أنتم"),
        ("المضارع المؤكد الثقيل المجهول ", "هي"),
    ],
    "ن-": [
        ("المضارع المنصوب", "نحن"),
        ("المضارع المجهول المجزوم", "نحن"),
        ("المضارع المجهول", "نحن"),
        ("المضارع المعلوم", "نحن"),
        ("المضارع المجزوم", "نحن"),
        ("المضارع المجهول المنصوب", "نحن"),
    ],
}
EXTERNAL_PREFIX_TABLE = {}
# [ أ الإستفهام]
EXTERNAL_PREFIX_TABLE["أ"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        # qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        # qutrubVerbConst.TenseImperative,
        # qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        qutrubVerbConst.TensePassiveFuture,
        # qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        # qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [و العطف]
EXTERNAL_PREFIX_TABLE["و"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TenseImperative,
        qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        qutrubVerbConst.TensePassiveFuture,
        qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ أ الإستفهام][و العطف]
EXTERNAL_PREFIX_TABLE["أو"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        # qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        # qutrubVerbConst.TenseImperative,
        # qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        # qutrubVerbConst.TensePassiveFuture,
        # qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        # qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        # qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ف العطف]
EXTERNAL_PREFIX_TABLE["ف"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TenseImperative,
        qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        qutrubVerbConst.TensePassiveFuture,
        qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ف السببيّة]
# Added to Feh AlAtf
EXTERNAL_PREFIX_TABLE["ف"] |= set(
    [
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ أ الإستفهام][ف العطف]
EXTERNAL_PREFIX_TABLE["أف"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        # qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        # qutrubVerbConst.TenseImperative,
        # qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        # qutrubVerbConst.TensePassiveFuture,
        # qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        # qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        # qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ل التوكيد]
EXTERNAL_PREFIX_TABLE["ل"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        # qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        # qutrubVerbConst.TenseImperative,
        # qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        # qutrubVerbConst.TensePassiveFuture,
        # qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        # qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        # qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [و العطف][ل التوكيد]
EXTERNAL_PREFIX_TABLE["ول"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        # qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        # qutrubVerbConst.TenseImperative,
        # qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        # qutrubVerbConst.TensePassiveFuture,
        # qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        # qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        # qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ف العطف][ل التوكيد]
EXTERNAL_PREFIX_TABLE["فل"] = set(
    [
        qutrubVerbConst.TenseConfirmedFuture,
        # qutrubVerbConst.TenseConfirmedImperative,
        qutrubVerbConst.TenseFuture,
        # qutrubVerbConst.TenseImperative,
        # qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveConfirmedFuture,
        # qutrubVerbConst.TensePassiveFuture,
        # qutrubVerbConst.TensePassiveJussiveFuture,
        qutrubVerbConst.TensePassivePast,
        # qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TensePast,
        # qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ل التعليل]
# added to لام التوكيد
EXTERNAL_PREFIX_TABLE["ل"] |= set(
    [
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ أ الإستفهام][ل التعليل]
EXTERNAL_PREFIX_TABLE["أل"] = set(
    [
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [و العطف][ل التعليل]
# added to لام التوكيد
EXTERNAL_PREFIX_TABLE["ول"] |= set(
    [
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ف العطف][ل التعليل]
# added to لام التوكيد
EXTERNAL_PREFIX_TABLE["فل"] |= set(
    [
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ أ الإستفهام][و العطف][ل التعليل]
EXTERNAL_PREFIX_TABLE["أول"] = set(
    [
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ أ الإستفهام][ف العطف][ل التعليل]
EXTERNAL_PREFIX_TABLE["أفل"] = set(
    [
        qutrubVerbConst.TensePassiveSubjunctiveFuture,
        qutrubVerbConst.TenseSubjunctiveFuture,
    ]
)
# [ل الأمر]
# added to Lam Tawkid
EXTERNAL_PREFIX_TABLE["ل"] |= set(
    [
        qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveJussiveFuture,
    ]
)
# [و العطف][ل الأمر]
# added to Lam Tawkid
EXTERNAL_PREFIX_TABLE["ول"] |= set(
    [
        qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveJussiveFuture,
    ]
)
# [ف العطف][ل الأمر]
# added to Lam Tawkid
EXTERNAL_PREFIX_TABLE["فل"] |= set(
    [
        qutrubVerbConst.TenseJussiveFuture,
        qutrubVerbConst.TensePassiveJussiveFuture,
    ]
)
# [س سوف]
EXTERNAL_PREFIX_TABLE["س"] = set(
    [
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TensePassiveFuture,
    ]
)
# [ أ الإستفهام][س سوف]
EXTERNAL_PREFIX_TABLE["أس"] = set(
    [
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TensePassiveFuture,
    ]
)
# [و العطف][س سوف]
EXTERNAL_PREFIX_TABLE["وس"] = set(
    [
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TensePassiveFuture,
    ]
)
# [ف العطف][س سوف]
EXTERNAL_PREFIX_TABLE["فس"] = set(
    [
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TensePassiveFuture,
    ]
)
# [ أ الإستفهام][و العطف][س سوف]
EXTERNAL_PREFIX_TABLE["أوس"] = set(
    [
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TensePassiveFuture,
    ]
)
# [ أ الإستفهام][ف العطف][س سوف]
EXTERNAL_PREFIX_TABLE["أفس"] = set(
    [
        qutrubVerbConst.TenseFuture,
        qutrubVerbConst.TensePassiveFuture,
    ]
)
EXTERNAL_SUFFIX_TABLE = {}
# تصلح فقط مع الأفعال الخمسة
# ToDo
# التحقق من يالء مع ا\لأفعال  الخمسة فقط
EXTERNAL_SUFFIX_TABLE["ي"] = (
    # qutrubVerbConst.PronounAna, #u"أنا";
    # qutrubVerbConst.PronounNahnu,#u"نحن";
    # qutrubVerbConst.PronounAnta,   #u"أنت";
    qutrubVerbConst.PronounAnti,  # u"أنتِ";
    qutrubVerbConst.PronounAntuma,  # u"أنتما";
    qutrubVerbConst.PronounAntuma_f,  # u"أنتما مؤ";
    qutrubVerbConst.PronounAntum,  # u"أنتم";
    # qutrubVerbConst.PronounAntunna,   #u"أنتن";
    # qutrubVerbConst.PronounHuwa,   #u"هو";
    # qutrubVerbConst.PronounHya,   #u"هي";
    # qutrubVerbConst.PronounHuma,   #u"هما";
    # qutrubVerbConst.PronounHuma_f,   #u"هما مؤ";
    # qutrubVerbConst.PronounHum,   #u"هم";
    # qutrubVerbConst.PronounHunna,   #u"هن";
)
EXTERNAL_SUFFIX_TABLE["ني"] = (
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAna,  # u"أنا";
    # qutrubVerbConst.PronounNahnu,#u"نحن";
    qutrubVerbConst.PronounAnta,  # u"أنت";
    qutrubVerbConst.PronounAnti,  # u"أنتِ";
    qutrubVerbConst.PronounAntuma,  # u"أنتما";
    qutrubVerbConst.PronounAntuma_f,  # u"أنتما مؤ";
    qutrubVerbConst.PronounAntum,  # u"أنتم";
    qutrubVerbConst.PronounAntunna,  # u"أنتن";
    qutrubVerbConst.PronounHuwa,  # u"هو";
    qutrubVerbConst.PronounHya,  # u"هي";
    qutrubVerbConst.PronounHuma,  # u"هما";
    qutrubVerbConst.PronounHuma_f,  # u"هما مؤ";
    qutrubVerbConst.PronounHum,  # u"هم";
    qutrubVerbConst.PronounHunna,  # u"هن";
)
EXTERNAL_SUFFIX_TABLE["نا"] = (
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAna,  # u"أنا";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounNahnu,  # u"نحن";
    qutrubVerbConst.PronounAnta,  # u"أنت";
    qutrubVerbConst.PronounAnti,  # u"أنتِ";
    qutrubVerbConst.PronounAntuma,  # u"أنتما";
    qutrubVerbConst.PronounAntuma_f,  # u"أنتما مؤ";
    qutrubVerbConst.PronounAntum,  # u"أنتم";
    qutrubVerbConst.PronounAntunna,  # u"أنتن";
    qutrubVerbConst.PronounHuwa,  # u"هو";
    qutrubVerbConst.PronounHya,  # u"هي";
    qutrubVerbConst.PronounHuma,  # u"هما";
    qutrubVerbConst.PronounHuma_f,  # u"هما مؤ";
    qutrubVerbConst.PronounHum,  # u"هم";
    qutrubVerbConst.PronounHunna,  # u"هن";
)
# للمذكر: يحذف صمير المؤنث
# للمؤنث يحذف صمير المذكر
EXTERNAL_SUFFIX_TABLE["ك"] = (
    qutrubVerbConst.PronounAna,  # u"أنا";
    qutrubVerbConst.PronounNahnu,  # u"نحن";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAnta,  # u"أنت";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAnti,  # u"أنتِ";
    # qutrubVerbConst.PronounAntuma,   #u"أنتما";
    # qutrubVerbConst.PronounAntuma_f,   #u"أنتما مؤ";
    # qutrubVerbConst.PronounAntum,   #u"أنتم";
    # qutrubVerbConst.PronounAntunna,   #u"أنتن";
    qutrubVerbConst.PronounHuwa,  # u"هو";
    qutrubVerbConst.PronounHya,  # u"هي";
    qutrubVerbConst.PronounHuma,  # u"هما";
    qutrubVerbConst.PronounHuma_f,  # u"هما مؤ";
    qutrubVerbConst.PronounHum,  # u"هم";
    qutrubVerbConst.PronounHunna,  # u"هن";
)
EXTERNAL_SUFFIX_TABLE["كما"] = (
    qutrubVerbConst.PronounAna,  # u"أنا";
    qutrubVerbConst.PronounNahnu,  # u"نحن";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAnta,  # u"أنت";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAnti,  # u"أنتِ";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntuma,  # u"أنتما";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntuma_f,  # u"أنتما مؤ";
    # qutrubVerbConst.PronounAntum,   #u"أنتم";
    # qutrubVerbConst.PronounAntunna,   #u"أنتن";
    qutrubVerbConst.PronounHuwa,  # u"هو";
    qutrubVerbConst.PronounHya,  # u"هي";
    qutrubVerbConst.PronounHuma,  # u"هما";
    qutrubVerbConst.PronounHuma_f,  # u"هما مؤ";
    qutrubVerbConst.PronounHum,  # u"هم";
    qutrubVerbConst.PronounHunna,  # u"هن";
)
EXTERNAL_SUFFIX_TABLE["كم"] = (
    qutrubVerbConst.PronounAna,  # u"أنا";
    qutrubVerbConst.PronounNahnu,  # u"نحن";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAnta,  # u"أنت";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAnti,  # u"أنتِ";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntuma,  # u"أنتما";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntuma_f,  # u"أنتما مؤ";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntum,  # u"أنتم";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntunna,  # u"أنتن";
    qutrubVerbConst.PronounHuwa,  # u"هو";
    qutrubVerbConst.PronounHya,  # u"هي";
    qutrubVerbConst.PronounHuma,  # u"هما";
    qutrubVerbConst.PronounHuma_f,  # u"هما مؤ";
    qutrubVerbConst.PronounHum,  # u"هم";
    qutrubVerbConst.PronounHunna,  # u"هن";
)
EXTERNAL_SUFFIX_TABLE["كن"] = (
    qutrubVerbConst.PronounAna,  # u"أنا";
    qutrubVerbConst.PronounNahnu,  # u"نحن";
    # qutrubVerbConst.PronounAnta,   #u"أنت";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAnti,  # u"أنتِ";
    qutrubVerbConst.PronounAntuma,  # u"أنتما";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntuma_f,  # u"أنتما مؤ";
    # qutrubVerbConst.PronounAntum,   #u"أنتم";
    # أفعال القلوب المتعدية لمفعول به عاقل
    qutrubVerbConst.PronounAntunna,  # u"أنتن";
    qutrubVerbConst.PronounHuwa,  # u"هو";
    qutrubVerbConst.PronounHya,  # u"هي";
    qutrubVerbConst.PronounHuma,  # u"هما";
    qutrubVerbConst.PronounHuma_f,  # u"هما مؤ";
    qutrubVerbConst.PronounHum,  # u"هم";
    qutrubVerbConst.PronounHunna,  # u"هن";
)
# This cases take all Pronoun
EXTERNAL_SUFFIX_TABLE["ه"] = qutrubVerbConst.PronounsTable
EXTERNAL_SUFFIX_TABLE["ها"] = qutrubVerbConst.PronounsTable
EXTERNAL_SUFFIX_TABLE["هما"] = qutrubVerbConst.PronounsTable
EXTERNAL_SUFFIX_TABLE["هم"] = qutrubVerbConst.PronounsTable
EXTERNAL_SUFFIX_TABLE["هنّ"] = qutrubVerbConst.PronounsTable
EXTERNAL_SUFFIX_TABLE["هن"] = qutrubVerbConst.PronounsTable
