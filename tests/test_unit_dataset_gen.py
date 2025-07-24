#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_unit_lemmatizer.py
#
#  Copyright 2023 zerrouki <zerrouki@majd4>
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

#!/usr/bin/python
# -*- coding=utf-8 -*-
import unittest
import sys
import pprint

# check if list are identical
# using collections.Counter()
import collections
import pyarabic.araby as araby


# sys.path.append("../")
import qalsadi.analex
from qalsadi.stemnode import StemNode


class qalsadiAnalyzerDataSetTestCase(unittest.TestCase):
    """Tests for `Lemmatizer`."""

    def setUp(self):
        """
        initial lemmatizer
        """
        self.analyzer = qalsadi.analex.Analex()
        self.analyzer.disable_allow_cache_use()

      # @unittest.skip("used to generate Data Set")
    def test_generate_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        wordcaseslistlist = self.analyzer.check_text(text)
        # wordcaseslistlist = self.analyzer.check_text(text, mode="nouns")

        for wordcaseslist in wordcaseslistlist[-4:]:
            stmnode = StemNode(wordcaseslist, vocalized_lemma=True)
            print(
                {
                    "token": stmnode.get_word(),
                    "lemmas": stmnode.get_lemmas(),
                    "wordtype": stmnode.get_word_type(),
                    "vocalizeds": stmnode.get_vocalizeds(),
                    "equal": True,
                },
                ",",
            )
        # wordcaseslistlist = self.analyzer.check_text(text, mode="nouns")
        #
        # # wordcaseslistlist = self.analyzer.check_text(text, mode="nouns")
        #
        # for wordcaseslist in wordcaseslistlist[-4:]:
        #     stmnode = StemNode(wordcaseslist, vocalized_lemma=True)
        #     print(
        #         {
        #             "token": stmnode.get_word(),
        #             "lemmas": stmnode.get_lemmas(),
        #             "wordtype": stmnode.get_word_type(),
        #             "vocalizeds": stmnode.get_vocalizeds(),
        #             "equal": True,
        #         },
        #         ",",
        #     )
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

if __name__ == "__main__":
    unittest.main()
