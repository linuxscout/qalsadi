#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
Constants for pounctuation stemming
"""
POUNCTUATION = {}

POUNCTUATION["."] = {
    "word": ".",
    "tags": "نقطة:break",
}
POUNCTUATION["~"] = {
    "word": "~",
    "tags": "شفاف",
}

POUNCTUATION[","] = {
    "word": ",",
    "tags": "فاصلة:break",
}
POUNCTUATION["،"] = {
    "word": "،",
    "tags": "فاصلة:break",
}
# POUNCTUATION[u',']={'word':u',', 'tags':u'فاصلة:شفاف',}
# POUNCTUATION[u'،']={'word':u'،', 'tags':u'فاصلة:شفاف',}

POUNCTUATION["?"] = {
    "word": "?",
    "tags": "استفهام:break",
}
POUNCTUATION["؟"] = {
    "word": "؟",
    "tags": "استفهام:break",
}
POUNCTUATION["!"] = {
    "word": "!",
    "tags": "تعجب:break",
}

POUNCTUATION[";"] = {
    "word": ";",
    "tags": "نقطة فاصلة:break",
}
POUNCTUATION["-"] = {
    "word": "-",
    "tags": "مطة:break",
}

POUNCTUATION[":"] = {
    "word": ":",
    "tags": "نقطتان:break",
}

POUNCTUATION["'"] = {
    "word": "'",
    "tags": "تنصيص مفرد:شفاف",
}
POUNCTUATION[" "] = {
    "word": " ",
    "tags": "فراغ:شفاف",
}

POUNCTUATION['"'] = {
    "word": '"',
    "tags": "تنصيص مزدوج:شفاف",
}

POUNCTUATION[")"] = {
    "word": ")",
    "tags": "قوس",
}
POUNCTUATION["("] = {
    "word": "(",
    "tags": "قوس",
}

POUNCTUATION["["] = {
    "word": "[",
    "tags": "عارضة",
}
POUNCTUATION["]"] = {
    "word": "]",
    "tags": "عارضة",
}

POUNCTUATION["{"] = {
    "word": "{",
    "tags": "حاضنة",
}
POUNCTUATION["}"] = {
    "word": "}",
    "tags": "حاضنة:break",
}
# treat newline as pounct for now
POUNCTUATION["\n"] = {
    "word": "\n",
    "tags": "سطر جديد:newline:break",
}
