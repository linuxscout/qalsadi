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
import os
import pprint

# check if list are identical
# using collections.Counter()
import collections
import pyarabic.araby as araby


sys.path.append("../")
import qalsadi.analex
from qalsadi.cachemanager import cache
from qalsadi.cachemanager import cache_pickle, cache_pickledb, cache_codernity, cache_factory

from qalsadi.stemnode import StemNode

from tests.fixtures import analex_dataset


class qalsadiAnalyzerCacheTestCase(unittest.TestCase):
    """Tests for `Lemmatizer`."""

    def setUp(self):
        """
        initial lemmatizer
        """
        self.analyzer = qalsadi.analex.Analex()
        self.word_lemma_list = analex_dataset.Lemmas_DataSet
        self.limit = 1000

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

    def _test_many_analysis(self, words_lemmas, vocalized=False, limit=10, check_as=""):
        """
        private method
        test word list analysis from dataset
        @param check_as: as verb, noun, etc.
        @return: a tuple, of (wrong_generation dicotnary, nb_diff_expected as int, nb_diff_generated as int
        """
        wrong_analysis = []
        nb_diff = 0
        for item in words_lemmas:
            token = item.get("token")
            expected_lemmas = item.get("lemmas")
            if not vocalized:
                expected_lemmas = [araby.strip_tashkeel(x) for x in expected_lemmas]
                # reduce duplicated
                expected_lemmas = list(set(expected_lemmas))

            expected_wordtype = item.get("wordtype")

            result_flag = item.get("equal", True)

            stmnode_result = self._check_word(
                token, vocalized_lemma=vocalized, check_as=check_as
            )
            lemmas = stmnode_result.get_lemmas()

            #

            # the result can be false or true,
            # if the result is expected, no error
            if collections.Counter(lemmas) != collections.Counter(expected_lemmas):
                # ~ if lemmas.sort() != expected_lemmas.sort():
                if result_flag:
                    nb_diff += 1
                    wrong_analysis.append(
                        {
                            "token": token,
                            "output": lemmas,
                            "expected": expected_lemmas,
                            "wordtype": stmnode_result.get_word_type(),
                            "expected_wordtype": expected_wordtype,
                            "flag": result_flag,
                        }
                    )
        return wrong_analysis

    def test_word_cases(
        self,
    ):
        """test word case"""
        word = "وفي"
        expected_lemma = "فِي"
        # ~ wordcase_list = self.analyzer.check_word(word)
        # ~ stmnode = StemNode(wordcase_list, vocalized_lemma=True)

        stmnode = self._check_word(word, vocalized_lemma=True)
        lemmas = stmnode.get_lemmas()
        self.assertIn(expected_lemma, lemmas)
        word = "يحتاج"
        expected_lemma = "اِحْتَاجَ"
        stmnode = self._check_word(word, vocalized_lemma=True)
        lemmas = stmnode.get_lemmas()
        self.assertIn(expected_lemma, lemmas)

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
            "فهم",
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
            "مدرسة",
            "ليس",
            "فرنسة",
            "التي",
            "استخدم",
            "ناس",
            "في",
            "شارع",
            "باريس",
            "..",
            "ملك",
            "بريطاني",
            "لا",
            "خطب",
            "بلغة",
            "شارع",
            "أدان",
            "..",
            "كل",
            "مقام",
            "مقال",
        ]

        wordcaselist_list = self.analyzer.check_text(text)
        for i, wordcases in enumerate(wordcaselist_list):
            stmnode = StemNode(wordcases)
            lemmas = stmnode.get_lemmas()
            lemmas = [ araby.strip_tashkeel(l) for l in lemmas]
            if expected_lemmas[i] not in lemmas:
                print(f"{expected_lemmas[i]} not in {lemmas}")
            self.assertIn(expected_lemmas[i], lemmas)

    # cases

    # ~ @unittest.skip("not yet ready ")
    def test_analysis_case1(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(self.word_lemma_list, limit=self.limit)
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # ----------------------
    # Test Cache
    # ----------------------
    def test_cache_memory(
        self,
    ):
        """test Cache case"""

        cacher = cache.Cache()
        # attach cacher to analyzer
        self.analyzer.set_cacher(cacher)
        self.analyzer.enable_allow_cache_use()
        self.test_text_cases()
        # remove cacher
        self.analyzer.set_cacher()
        self.analyzer.disable_allow_cache_use()

    def test_cache_pickle(
        self,
    ):
        """test Cache case"""
        path = os.path.join(os.path.dirname(__file__), "cache/qalsadiCache.pickle")
        cacher = cache_pickle.Cache(path)
        # attach cacher to analyzer
        self.analyzer.set_cacher(cacher)
        self.analyzer.enable_allow_cache_use()
        self.test_text_cases()
        # remove cacher
        self.analyzer.set_cacher()
        self.analyzer.disable_allow_cache_use()

    def test_cache_pickledb(
        self,
    ):
        """test Cache case"""
        path = os.path.join(os.path.dirname(__file__), "cache/qalsadiCache.pickledb")
        cacher = cache_pickledb.Cache(path)
        # attach cacher to analyzer
        self.analyzer.set_cacher(cacher)
        self.analyzer.enable_allow_cache_use()
        self.test_text_cases()
        # remove cacher
        self.analyzer.set_cacher()
        self.analyzer.disable_allow_cache_use()

    def test_cache_codernity(
        self,
    ):
        """test Cache case"""
        path = os.path.join(os.path.dirname(__file__), "cache")
        cacher = cache_codernity.Cache(path)
        # attach cacher to analyzer
        self.analyzer.set_cacher(cacher)
        self.analyzer.enable_allow_cache_use()
        self.test_text_cases()
        # remove cacher
        self.analyzer.set_cacher()
        self.analyzer.disable_allow_cache_use()

    def test_cache_factory(
        self,
    ):
        """test Cache case"""
        path = os.path.join(os.path.dirname(__file__), "cache")
        for name in cache_factory.Cache_Factory.list():
            cacher = cache_factory.Cache_Factory.factory(name, path)
            # attach cacher to analyzer
            self.analyzer.set_cacher(cacher)
            self.analyzer.enable_allow_cache_use()
            self.test_text_cases()
            # remove cacher
            self.analyzer.set_cacher()
            self.analyzer.disable_allow_cache_use()


if __name__ == "__main__":
    unittest.main()
