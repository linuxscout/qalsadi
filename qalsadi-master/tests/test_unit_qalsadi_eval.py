# import unittest
# from .qalsadi_eval import QalsadiEvaluator
#
# class TestQalsadiEvaluator(unittest.TestCase):
#
#     def setUp(self):
#         self.evaluator = QalsadiEvaluator(folder="tests/samples/Nemlar", recursive=False)
#
#     def test_normalize_removes_diacritics(self):
#         self.assertEqual(self.evaluator.normalize("يُصْبِحُ"), "يصبح")
#
#     def test_extract_lemma_returns_list(self):
#         lemmas = self.evaluator.extract_lemma("لَاعِبٍ")
#         self.assertIsInstance(lemmas, list)
#         self.assertTrue(len(lemmas) > 0)
#
#     def test_get_xml_files(self):
#         files = self.evaluator.get_xml_files()
#         self.assertTrue(all(f.endswith(".xml") for f in files))
#
#     def test_evaluate_file_structure(self):
#         total, correct, mismatches = self.evaluator.evaluate_file("tests/samples/Nemlar/GeneralNews_104.xml")
#         self.assertIsInstance(total, int)
#         self.assertIsInstance(correct, int)
#         self.assertIsInstance(mismatches, list)
#
# if __name__ == "__main__":
#     unittest.main()
#
import unittest
import os
from .qalsadi_eval  import QalsadiEvaluator  # Replace with actual module name


class TestQalsadiEvaluatorNoMock(unittest.TestCase):

    def setUp(self):
        # Create a temporary folder and XML file
        self.test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"samples/Nemlar")
        self.test_file = os.path.join(self.test_dir,"AASample.xml")

        # Write sample XML with Arabic word and lemma
        xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
        <root>
          <sentence id="1">
            <text> كتبت سيارات مشينا</text>
            <ArabicLexical word="كتبت" lemma="َكَتَبَ"/>
            <ArabicLexical word="سيارات" lemma="سَيَّارَةٌ"/>
            <ArabicLexical word="مشينا" lemma="مَشَى"/>
          </sentence>
        </root>'''
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(xml_content)

    # def tearDown(self):
    #     self.test_dir.cleanup()

    def test_get_xml_files(self):
        evaluator = QalsadiEvaluator(folder=self.test_dir)
        xml_files = evaluator.get_xml_files()
        self.assertIn(self.test_file, xml_files)
        self.assertEqual(len(xml_files), 491)

    def test_evaluate_file_accuracy(self):
        evaluator = QalsadiEvaluator(folder=self.test_dir)
        total, correct, correct_vocalized, sentences, mismatches = evaluator.evaluate_file(self.test_file)

        self.assertEqual(total, 3)
        self.assertGreaterEqual(correct, 2)  # Allowing Qalsadi to miss one case
        self.assertGreaterEqual(correct_vocalized, 2)  # Allowing Qalsadi to miss one case
        self.assertEqual(sentences, 1)
        self.assertLessEqual(len(mismatches), 1)

    def test_ignore_diacritics_flag(self):
        evaluator = QalsadiEvaluator(folder=self.test_dir, ignore_diacritics=True)
        stripped = evaluator.normalize("يُصْبِحُ")
        self.assertEqual(stripped, "يصبح")

    def test_extract_lemma_returns_list(self):
        evaluator = QalsadiEvaluator(folder=self.test_dir)
        result = evaluator.extract_lemma("كتبت")
        self.assertIsInstance(result, list)
        self.assertTrue(evaluator.match_lemma("كَتَبَ", result), msg= "Result is '%s'"%", ".join(result))


if __name__ == "__main__":
    unittest.main()
