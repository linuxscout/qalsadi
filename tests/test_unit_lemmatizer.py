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
import pyarabic.araby as araby

sys.path.append("../")
import qalsadi.lemmatizer

from fixtures import lemmas_dataset


class qalsadilemmatizerTestCase(unittest.TestCase):
    """Tests for `Lemmatizer`."""

    def setUp(self):
        """
        initial lemmatizer
        """
        self.lemmer = qalsadi.lemmatizer.Lemmatizer()
        self.word_lemma_list = lemmas_dataset.Lemmas_DataSet
        self.limit = 1000

    def test_text_cases(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        expected_lemmas = [
            "هل",
            "احتاج",
            "إلى",
            "ترجمة",
            "كي",
            "تف",
            "خطاب",
            "ملك",
            "؟",
            "لغة",
            '"',
            "كلاسيكي",
            '"(',
            "فصحى",
            ")",
            "موجود",
            "في",
            "كل",
            "لغة",
            "كذلك",
            "لغة",
            '"',
            "دارج",
            '"..',
            "فرنسة",
            "التي",
            "درس",
            "في",
            "مدرس",
            "ليست",
            "فرنسة",
            "التي",
            "استخدم",
            "ناس",
            "في",
            "شوارع",
            "باريس",
            "..",
            "ملك",
            "بريطاني",
            "لا",
            "خطب",
            "بلغة",
            "شوارع",
            "أدان",
            "..",
            "كل",
            "مقام",
            "مقال",
        ]
        lemmas = self.lemmer.lemmatize_text(text)
        print("Len Lemmas", len(lemmas), lemmas)
        print("Len Lemmas  expected", len(expected_lemmas), expected_lemmas)
        print(list(zip(lemmas, expected_lemmas)))
        # ~ self.assertCountEqual(lemmas, expected_lemmas)
        self.assertListEqual(lemmas, expected_lemmas)

    @unittest.skip("used to generate Data Set")
    def test_generate_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        tokens = araby.tokenize(text)

        expected_lemmas = [
            "هل",
            "احتاج",
            "إلى",
            "ترجمة",
            "كي",
            "تف",
            "خطاب",
            "ملك",
            "؟",
            "لغة",
            '"',
            "كلاسيكي",
            '"(',
            "فصحى",
            ")",
            "موجود",
            "في",
            "كل",
            "لغة",
            "كذلك",
            "لغة",
            '"',
            "دارج",
            '"..',
            "فرنسة",
            "التي",
            "درس",
            "في",
            "مدرس",
            "ليست",
            "فرنسة",
            "التي",
            "استخدم",
            "ناس",
            "في",
            "شوارع",
            "باريس",
            "..",
            "ملك",
            "بريطاني",
            "لا",
            "خطب",
            "بلغة",
            "شوارع",
            "أدان",
            "..",
            "كل",
            "مقام",
            "مقال",
        ]
        self.lemmer.set_vocalized_lemma()
        lemmas = self.lemmer.lemmatize_text(text, return_pos=True)
        print(len(tokens), len(lemmas), len(expected_lemmas))
        print(lemmas)
        for i in range(len(lemmas)):
            lm = lemmas[i]
            if isinstance(lemmas[i], str):
                lm = (lm, "")

            print(
                {
                    "token": tokens[i],
                    "lemma": lm[0],
                    # ~ "unvocalized":araby.strip_tashkeel(lm[0]),
                    "wordtype": lm[1],
                    # ~ "expected_lemma":expected_lemmas[i],
                    # ~ "expected_wordtype":lm[1],
                    "equal": True,
                },
                ",",
            )
        self.assertCountEqual(lemmas, expected_lemmas)
        # ~ self.assertListEqual(lemmas, expected_lemmas)

    # ~ @unittest.skip("Not yet ready")
    def _test_many_lemmatization(self, words_lemmas, vocalized=False, limit=10):
        """
        private method
        test word list lemmatization from dataset
        @return: a tuple, of (wrong_generation dicotnary, nb_diff_expected as int, nb_diff_generated as int
        """
        wrong_lemmatization = []
        nb_diff = 0
        if vocalized:
            self.lemmer.set_vocalized_lemma()
        for item in words_lemmas:
            token = item.get("token")
            expected_lemma = item.get("lemma")
            if not vocalized:
                expected_lemma = araby.strip_tashkeel(expected_lemma)
            expected_wordtype = item.get("wordtype")
            # used to handle incorrect cases,
            # if the flag is False, the actual output is not correct according to the expected
            # result
            # used to watch lemmatizer changes
            result_flag = item.get("equal", True)

            lemma, wordtype = self.lemmer.lemmatize(token, return_pos=True)

            # the result can be false or true,
            # if the result is expected, no error
            if lemma != expected_lemma:
                if result_flag:
                    nb_diff += 1
                    wrong_lemmatization.append(
                        {
                            "token": token,
                            "output": lemma,
                            "expected": expected_lemma,
                            "wordtype": wordtype,
                            "expected_wordtype": expected_wordtype,
                            "flag": result_flag,
                        }
                    )
        if vocalized:
            self.lemmer.set_vocalized_lemma()
        return wrong_lemmatization

    def test_word_cases(
        self,
    ):
        """test word case"""
        word = "يحتاج"
        lemma = "احتاج"
        self.assertEqual(self.lemmer.lemmatize(word), lemma)
        word = "وفي"
        lemma = "في"
        self.assertEqual(self.lemmer.lemmatize(word), lemma)
        word = "يحتاج"
        lemma = "احتاج"
        self.assertEqual(self.lemmer.lemmatize(word), lemma)

    def test_word_cases_tuple(
        self,
    ):
        """test word case"""
        word = '"'
        result = self.lemmer.lemmatize(word, return_pos=True)
        self.assertIsInstance(result, tuple, " Result Type is %s" % type(result))

    # cases

    def test_lemmatization_case1(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_lemmatization(self.word_lemma_list, limit=self.limit)
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_lemmatization_vocalized_case(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_lemmatization(
            self.word_lemma_list, vocalized=True, limit=self.limit
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )


if __name__ == "__main__":
    unittest.main()
