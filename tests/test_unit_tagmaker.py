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
import re
import pprint

# check if list are identical
# using collections.Counter()
import collections
import pyarabic.araby as araby
import mysam.tagcoder


import qalsadi.analex
from qalsadi.stemnode import StemNode

# sys.path.append('../')
# from fixtures import tagcode_dataset
from tests.fixtures import tagcode_dataset


class qalsadiTagCoderTestCase(unittest.TestCase):
    """Tests for `Lemmatizer`."""

    def setUp(self):
        """
        initial lemmatizer
        """
        self.analyzer = qalsadi.analex.Analex()
        self.word_lemma_list = tagcode_dataset.Lemmas_DataSet
        self.limit = 1000
        self.mytagcoder = mysam.tagcoder.tagCoder()

    @unittest.skip("used to generate Data Set")
    def test_generate_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""

        tokens = araby.tokenize(text)

        for token in tokens:
            print("'%s':[" % token)
            tuple_list = self._check_word_tags_tuple(token)
            for d in tuple_list:
                d["equal"] = True
                d["token"] = token

                print("  ", d, ",")
            print("],")
            # ~ pprint.pprint(tuple_list)
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

    def _check_word(self, word, vocalized_lemma=False, check_as=""):
        """
        A costumized check word used just for tests
        """
        if check_as == "":
            wordcases = self.analyzer.check_word(word)
        else:
            wordcases = self.analyzer.check_word(word)

        stmnd = StemNode(wordcases, vocalized_lemma=vocalized_lemma)
        return stmnd

    def _check_word_tags(self, word, vocalized_lemma=False, check_as=""):
        """
        A costumized check word used just for tests
        """

        stmnode = self._check_word(
            word, vocalized_lemma=vocalized_lemma, check_as=check_as
        )
        tagslist = stmnode.get_tags()

        # convert tags string into list
        tagslist = [t.split(":") for t in tagslist]

        # encode tags into mysam tag manager
        tagscode_list = [self.mytagcoder.encode(t) for t in tagslist if t]
        inflect_list = [self.mytagcoder.inflect(t) for t in tagscode_list if t]
        print("Inflection ", inflect_list)

        return tagscode_list

    def _check_word_tags_tuple(self, word):
        """
        A costumized check word used just for tests
        return list of tuples (vocalized, lemma, tags, tagcode, inflection)
        """

        wordcases = self.analyzer.check_word(word)
        tuple_list = []
        for wd in wordcases:
            lemma = wd.get_original()
            vocalized = wd.get_vocalized()
            tags = ":".join([wd.get_tags(), wd.get_type()])
            tags = tags.split(":")
            tagscode = self.mytagcoder.encode(tags)
            inflect = self.mytagcoder.inflect(tagscode)
            # inflect = re.sub(r'\s+', ' ', inflect).strip()
            tuple_list.append(
                {
                    "vocalized": vocalized,
                    "lemma": lemma,
                    "tags": tags,
                    "tagscode": tagscode,
                    "inflect": inflect,
                }
            )
        return tuple_list

    # ~ @unittest.skip("Not yet ready")
    def _test_many_analysis_tags(self, words_lemmas, test_field="tagscode", limit=10):
        """
        private method
        test word list analysis from dataset
        according to vocalizations
        @param check_as: as verb, noun, etc.
        @return: a tuple, of (wrong_generation dicotnary, nb_diff_expected as int, nb_diff_generated as int
        """
        wrong_analysis = []
        nb_diff = 0
        for token in words_lemmas:

            tuple_list = self._check_word_tags_tuple(token)
            expected_tuple_list = words_lemmas[token]
            if test_field in ("tagscode", "inflect", "tags"):
                # tests on tagscodes
                fields = [d.get(test_field, "") for d in tuple_list]
                expected_fields = [
                    d.get(test_field, "") for d in expected_tuple_list if d
                ]
            else:
                fields = [d.get("tagscode", "") for d in tuple_list]
                expected_fields = [
                    d.get("tagscode", "") for d in expected_tuple_list if d
                ]

            # the result can be false or true,
            # if the result is expected, no error
            if collections.Counter(fields) != collections.Counter(expected_fields):
                nb_diff += 1
                wrong_analysis.append(
                    {
                        "token": token,
                        "output": fields,
                        "expected": expected_fields,
                        # ~ "flag":result_flag,
                    }
                )
        return wrong_analysis

    def test_word_cases(
        self,
    ):
        """test word case"""
        word = "وفي"
        expected_tagcode = "V-1;F1Y-i--;---"
        tagscode_list = self._check_word_tags(word)
        print(tagscode_list)
        self.assertIn(expected_tagcode, tagscode_list)

        word = "بالمدرستين"
        expected_tagcode = "NA-;F2----I;-BL"
        tagscode_list = self._check_word_tags(word)
        print(tagscode_list)
        self.assertIn(expected_tagcode, tagscode_list)

        word = "يحتاج"
        expected_tagcode = "V-0;M1H-faU;---"
        # ~ expected_tagcode = ''
        tagscode_list = self._check_word_tags(word)
        print(tagscode_list)
        self.assertIn(expected_tagcode, tagscode_list)

    def test_word_cases_tuple(
        self,
    ):
        """test word case"""
        word = "وفي"
        expected_tagcode = "V-1;F1Y-i--;---"
        tuple_list = self._check_word_tags_tuple(word)
        print(tuple_list)
        tagscode_list = [d.get("tagscode", "") for d in tuple_list]
        self.assertIn(expected_tagcode, tagscode_list)

        word = "بالمدرستين"
        expected_tagcode = "NA-;F2----I;-BL"
        tuple_list = self._check_word_tags_tuple(word)
        print(tuple_list)
        tagscode_list = [d.get("tagscode", "") for d in tuple_list]
        self.assertIn(expected_tagcode, tagscode_list)

        word = "يحتاج"
        expected_tagcode = "V-0;M1H-faU;---"
        tuple_list = self._check_word_tags_tuple(word)
        print(tuple_list)
        tagscode_list = [d.get("tagscode", "") for d in tuple_list]
        self.assertIn(expected_tagcode, tagscode_list)

    # cases

    def test_analysis_tags_case1(
        self,
    ):
        """test case according to generated tagcodes
        based on dataset"""

        result = self._test_many_analysis_tags(
            self.word_lemma_list, test_field="tagscode", limit=self.limit
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_analysis_tags_case2(
        self,
    ):
        """test case according to generated inflections
        based on dataset"""

        result = self._test_many_analysis_tags(
            self.word_lemma_list, test_field="inflect", limit=self.limit
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    @unittest.skip("To do, fix tags strings to be compared")
    def test_analysis_tags_case3(
        self,
    ):
        """test case according to generated tags
        based on dataset"""

        result = self._test_many_analysis_tags(
            self.word_lemma_list, test_field="tags", limit=self.limit
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
