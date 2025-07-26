import unittest
from tabulate import tabulate
import qalsadi.analex as qa
from qalsadi.resultformatter import ResultFormatter


class TestResultFormatterWithRealData(unittest.TestCase):

    def setUp(self):
        # Real morphological analysis result
        text = "لا يحمل الحقد من تعلو به الرتب"
        analyzer = qa.Analex()
        self.result = analyzer.check_text(text)
        self.formatter = ResultFormatter(self.result)

    def test_set_and_get_used_fields(self):
        self.formatter.set_used_fields("main")
        expected = ["id","word", "vocalized", "stem", "affix", "lemma", "type", "tags"]
        self.assertEqual(self.formatter.get_used_fields(), expected)

    def test_set_and_get_used_fields_add(self):
        self.formatter.set_used_fields("main", additional_fields=["NON_EXISTANT", "root"])
        expected = ["id","word", "vocalized", "stem", "affix", "lemma", "type", "tags", "root"]
        self.assertEqual(self.formatter.get_used_fields(), expected)

    def test_as_table_output(self):
        self.formatter.set_used_fields("main")
        table = self.formatter.as_table()
        self.assertIsInstance(table, str)
        self.assertIn("word", table)
        self.assertIn("الحقد", table)

    def test_as_json_output(self):
        self.formatter.set_used_fields("main")
        output = self.formatter.as_json()
        self.assertIn("الحقد", output)
        self.assertIn("type", output)

    def test_as_csv_output(self):
        self.formatter.set_used_fields("main")
        output = self.formatter.as_csv()
        self.assertTrue(output.startswith("id,word,vocalized,stem,affix"))
        self.assertIn("الحقد", output)

    def test_as_xml_output(self):
        self.formatter.set_used_fields("main")
        output = self.formatter.as_xml()
        self.assertIn("<word>", output)
        self.assertIn("<lemma>", output)

    def test_filter_by(self):
        self.formatter.set_used_fields("main")
        # Just test filter returns a ResultFormatter
        filtered = self.formatter.filter(type="Verb")
        self.assertTrue(self.formatter._is_valid_result_type(filtered), msg=" The filtred data is not a valid list of list of stemmedword object")
        self.assertLessEqual(len(filtered), len(self.result), msg="The filter does nt reduce the result size {len(filtered)}=={len(self.result)}")

    def test_group_by(self):
        self.formatter.set_used_fields("main")
        # Just test filter returns a ResultFormatter

        grouped = self.formatter.group_by("root")
        self.assertIsInstance(grouped, dict)
        self.assertGreater(len(grouped), 0)
        for root, items in grouped.items():
            self.assertIsInstance(items, list)

    def test_list_fields(self):
        fields = self.formatter.list_fields()
        self.assertIsInstance(fields, list)
        self.assertIn("word", fields)
        self.assertIn("lemma", fields)


if __name__ == '__main__':
    unittest.main()
