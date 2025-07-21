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


sys.path.append("../")
import qalsadi.analex
from qalsadi.stemnode import StemNode

from fixtures import analex_dataset
from fixtures import verb_dataset
from fixtures import noun_dataset
from fixtures import stopword_dataset
from fixtures import unknown_dataset
from fixtures import pounct_dataset


class qalsadiAnalyzerTestCase(unittest.TestCase):
    """Tests for `Lemmatizer`."""

    def setUp(self):
        """
        initial lemmatizer
        """
        self.analyzer = qalsadi.analex.Analex()
        self.word_lemma_list = analex_dataset.Lemmas_DataSet
        self.verb_lemma_list = verb_dataset.Lemmas_DataSet
        self.noun_lemma_list = noun_dataset.Lemmas_DataSet
        self.stopword_lemma_list = stopword_dataset.Lemmas_DataSet
        self.unknown_lemma_list = unknown_dataset.Lemmas_DataSet
        self.pounct_lemma_list = pounct_dataset.Lemmas_DataSet
        self.limit = 1000

    def _check_word(self, word, vocalized_lemma=False, check_as=""):
        """
        A costumized check word used just for tests
        """
        if check_as == "":
            wordcases = self.analyzer.check_word(word)
        elif check_as == "noun":
            wordcases = self.analyzer.check_word_as_noun(word)
        elif check_as == "verb":
            wordcases = self.analyzer.check_word_as_verb(word)
        elif check_as == "pounct":
            wordcases = self.analyzer.check_word_as_pounct(word)
        elif check_as == "unknown":
            wordcases = self.analyzer.check_word_as_unknown(word)
        elif check_as == "stopword":
            wordcases = self.analyzer.check_word_as_stopword(word)
        else:
            wordcases = self.analyzer.check_word(word)

        stmnd = StemNode(wordcases, vocalized_lemma=vocalized_lemma)
        return stmnd

    @unittest.skip("used to generate Data Set")
    def test_generate_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        wordcaseslistlist = self.analyzer.check_text(text)

        for wordcaseslist in wordcaseslistlist:
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
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

    @unittest.skip("used to generate Data Set")
    def test_generate_verb_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        self._test_generate_data_set(text, check_as="verb")
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

    @unittest.skip("used to generate Data Set")
    def test_generate_noun_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        self._test_generate_data_set(text, check_as="noun")
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

    @unittest.skip("used to generate Data Set")
    def test_generate_stopword_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        self._test_generate_data_set(text, check_as="stopword")
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

    @unittest.skip("used to generate Data Set")
    def test_generate_unknown_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        self._test_generate_data_set(text, check_as="unknown")
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

    @unittest.skip("used to generate Data Set")
    def test_generate_pounct_data_set(
        self,
    ):
        """test text case"""
        text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        self._test_generate_data_set(text, check_as="pounct")
        self.assertCountEqual(
            [
                1,
            ],
            [],
        )

    # ~ @unittest.skip("used to generate Data Set")
    def _test_generate_data_set(self, text, check_as=""):
        """test text case"""
        # ~ text = u"""هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
        tokens = araby.tokenize(text)

        for token in tokens:
            stmnode = self._check_word(token, vocalized_lemma=True, check_as=check_as)
            print(
                {
                    "token": token,
                    "lemmas": stmnode.get_lemmas(),
                    "wordtype": stmnode.get_word_type(),
                    "vocalizeds": stmnode.get_vocalizeds(),
                    "equal": True,
                },
                ",",
            )

    # ~ @unittest.skip("Not yet ready")
    def _test_many_analysis_vocalizeds(
        self, words_lemmas, vocalized=False, limit=10, check_as=""
    ):
        """
        private method
        test word list analysis from dataset
        according to vocalizations
        @param check_as: as verb, noun, etc.
        @return: a tuple, of (wrong_generation dicotnary, nb_diff_expected as int, nb_diff_generated as int
        """
        wrong_analysis = []
        nb_diff = 0
        for item in words_lemmas:
            token = item.get("token")
            expected_vocalizeds = item.get("vocalizeds")

            result_flag = item.get("equal", True)

            # ~ stmnode_result = StemNode(self.analyzer.check_word(token), vocalized_lemma=vocalized)
            stmnode_result = self._check_word(
                token, vocalized_lemma=vocalized, check_as=check_as
            )
            vocalizeds = stmnode_result.get_vocalizeds()

            # the result can be false or true,
            # if the result is expected, no error
            if collections.Counter(vocalizeds) != collections.Counter(
                expected_vocalizeds
            ):
                # ~ if vocalizeds.sort() != expected_vocalizeds.sort():
                if result_flag:
                    nb_diff += 1
                    wrong_analysis.append(
                        {
                            "token": token,
                            "output": vocalizeds,
                            "expected": expected_vocalizeds,
                            "wordtype": stmnode_result.get_word_type(),
                            "expected_wordtype": expected_wordtype,
                            "flag": result_flag,
                        }
                    )
        return wrong_analysis

    # ~ @unittest.skip("Not yet ready")
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

    def test_word_verb_cases(
        self,
    ):
        """test word case"""
        word = "يحتاج"
        expected_lemma = "اِحْتَاجَ"
        stmnode = self._check_word(word, vocalized_lemma=True, check_as="verb")
        lemmas = stmnode.get_lemmas()
        self.assertIn(expected_lemma, lemmas)

    def test_word_noun_cases(
        self,
    ):
        """test word case"""
        word = "بالمدرستين"
        expected_lemma = "مَدْرَسَةٌ"

        stmnode = self._check_word(word, vocalized_lemma=True, check_as="noun")
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
        wordcaselist_list = self.analyzer.check_text(text)
        for i, wordcases in enumerate(wordcaselist_list):
            stmnode = StemNode(wordcases)
            lemmas = stmnode.get_lemmas()
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

    # ~ @unittest.skip("not yet ready ")
    def test_analysis_vocalized_case(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.word_lemma_list, vocalized=True, limit=self.limit
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_analysis_vocalizations_case1(
        self,
    ):
        """test case according to generated vocalizations
        based on dataset"""

        result = self._test_many_analysis_vocalizeds(
            self.word_lemma_list, limit=self.limit
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # verbs

    def test_analysis_case1_verb(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.verb_lemma_list, limit=self.limit, check_as="verb"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # ~ @unittest.skip("not yet ready ")
    def test_analysis_vocalized_case_verb(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.verb_lemma_list, vocalized=True, limit=self.limit, check_as="verb"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_analysis_vocalizations_case1_verb(
        self,
    ):
        """test case according to generated vocalizations
        based on dataset"""

        result = self._test_many_analysis_vocalizeds(
            self.verb_lemma_list, limit=self.limit, check_as="verb"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # nouns

    def test_analysis_case1_noun(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.noun_lemma_list, limit=self.limit, check_as="noun"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # ~ @unittest.skip("not yet ready ")
    def test_analysis_vocalized_case_noun(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.noun_lemma_list, vocalized=True, limit=self.limit, check_as="noun"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_analysis_vocalizations_case1_noun(
        self,
    ):
        """test case according to generated vocalizations
        based on dataset"""

        result = self._test_many_analysis_vocalizeds(
            self.noun_lemma_list, limit=self.limit, check_as="noun"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # stopwords

    def test_analysis_case1_stopword(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.stopword_lemma_list, limit=self.limit, check_as="stopword"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # ~ @unittest.skip("not yet ready ")
    def test_analysis_vocalized_case_stopword(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.stopword_lemma_list,
            vocalized=True,
            limit=self.limit,
            check_as="stopword",
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_analysis_vocalizations_case1_stopword(
        self,
    ):
        """test case according to generated vocalizations
        based on dataset"""

        result = self._test_many_analysis_vocalizeds(
            self.stopword_lemma_list, limit=self.limit, check_as="stopword"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # unknowns

    def test_analysis_case1_unknown(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.unknown_lemma_list, limit=self.limit, check_as="unknown"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # ~ @unittest.skip("not yet ready ")
    def test_analysis_vocalized_case_unknown(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.unknown_lemma_list,
            vocalized=True,
            limit=self.limit,
            check_as="unknown",
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_analysis_vocalizations_case1_unknown(
        self,
    ):
        """test case according to generated vocalizations
        based on dataset"""

        result = self._test_many_analysis_vocalizeds(
            self.unknown_lemma_list, limit=self.limit, check_as="unknown"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # pouncts

    def test_analysis_case1_pounct(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.pounct_lemma_list, limit=self.limit, check_as="pounct"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    # ~ @unittest.skip("not yet ready ")
    def test_analysis_vocalized_case_pounct(
        self,
    ):
        """test case
        based on dataset"""

        result = self._test_many_analysis(
            self.pounct_lemma_list, vocalized=True, limit=self.limit, check_as="pounct"
        )
        len_wrong_cases = len(result)
        if len_wrong_cases:
            print("Wrong cases")
            pprint.pprint(result)
        self.assertEqual(
            len_wrong_cases, 0, "There are %d wrong cases " % len_wrong_cases
        )

    def test_analysis_vocalizations_case1_pounct(
        self,
    ):
        """test case according to generated vocalizations
        based on dataset"""

        result = self._test_many_analysis_vocalizeds(
            self.pounct_lemma_list, limit=self.limit, check_as="pounct"
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
