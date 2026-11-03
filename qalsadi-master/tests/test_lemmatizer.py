#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_lemmatizer.py
#
#  Copyright 2020 zerrouki <zerrouki@majd4>
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

import sys
import pprint
import pyarabic.araby as araby

sys.path.append("../")
import qalsadi.lemmatizer


def main(args):
    # #test syn
    text = "إلى البيت"
    text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال
    """
    text = "اسمائها وصفاتها"
    result = []
    lemmer = qalsadi.lemmatizer.Lemmatizer()
    lemmer.set_vocalized_lemma()
    # ~ result = lemmer.analyze_text(text)
    # ~ lemmas = lemmer.get_lemmas(result)
    print("****************")
    lemmas = lemmer.lemmatize_text(text, return_pos=True)
    # ~ lemmas = lemmer.lemmatize_text(text)
    print(lemmas)
    print("****************")
    # the result contains objects
    pprint.pprint(result)
    tokens = araby.tokenize(text)
    pprint.pprint(list(zip(tokens, lemmas)))
    for tok in tokens:
        result = lemmer.lemmatize(tok, return_pos=True)
        # ~ lemma, pos = lemmer.lemmatize(tok, return_pos=True)
        print(tok, result)
    word = "وفي"
    result = lemmer.lemmatize(tok, return_pos=True)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
