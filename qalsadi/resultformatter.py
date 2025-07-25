import json
import csv
import io
import xml.etree.ElementTree as ET
from tabulate import tabulate
from collections import defaultdict
from .stemmedword import  StemmedWord
def is_list_of_lists_of_type(obj, cls):
    return (
        isinstance(obj, list) and
        all(isinstance(sub, list) and all(isinstance(item, cls) for item in sub)
            for sub in obj)
    )
class ResultFormatter:
    def __init__(self, results):
        self.results = results
        assert self.is_valid_result_type(results)

        self.flat_results = [dict(item) for sublist in results for item in sublist]
        # self.flat_results = [item.__dict__ for sublist in results for item in sublist]
        self.all_fields = self._collect_all_fields()
        self.used_fields = list(self.all_fields)  # default is all
        # #['action', 'affix', 'affix_key', 'freq', 'lemma', 'need', 'object_type', 'original', 'original_tags', 'root',
        #  'semivocalized', 'stem', 'tag_added', 'tag_break', 'tag_confirmed', 'tag_gender', 'tag_initial', 'tag_mamnou3',
        #  'tag_mood', 'tag_number', 'tag_original_gender', 'tag_original_number', 'tag_person', 'tag_pronoun',
        #  'tag_regular', 'tag_tense', 'tag_transitive', 'tag_transparent', 'tag_type', 'tag_voice', 'tags', 'type',
        #  'unvocalized', 'vocalized', 'word']

        self.profiles = {
            "main": ["word", "vocalized", "stem", "affix", "lemma", "type","tags"],
            "all": self.all_fields,
            "roots": ["word", "root"],
            "lemmas": ["word", "lemma"],
            "inflect": [
                "word", "vocalized", "stem", "affix", "lemma", "type", "tags",
            ],
            "custom":[],
        }

    def is_valid_result_type(self, result):
        return is_list_of_lists_of_type(result, StemmedWord)

    def get_used_fields(self,):
        return self.used_fields

    def list_fields(self,):
        return self.all_fields

    def list_profiles(self,):
        return list(self.profiles.keys())

    def _collect_all_fields(self):
        """Collect all keys present in the results."""
        all_keys = set()
        for r in self.flat_results:
            all_keys.update(r.keys())
        return sorted(all_keys)

    def set_used_fields(self, profile="all", additional_fields=[]):
        """Set the fields to be displayed/exported based on a named profile."""


        self.used_fields = self.profiles.get(profile, self.all_fields)
        if additional_fields:
            # avoid non existant fields, and already used fields
            fields_to_add = [f for f in additional_fields if f in self.all_fields and f not in self.used_fields]
            self.used_fields.extend(fields_to_add)


    def load_data(self, results):
        """ load data"""
        self.results = results

    # --- Display ---
    def as_table(self, tablefmt="plain"):
        rows = [[r.get(f, "") for f in self.used_fields] for r in self.flat_results]
        return tabulate(rows, headers=self.used_fields, tablefmt=tablefmt)

    # --- Return as string ---
    def as_json(self) -> str:
        # return json.dumps(self.flat_results, ensure_ascii=False, indent=2)
        return json.dumps([[obj.to_dict(self.used_fields) for obj in row] for row in self.results],
                          ensure_ascii=False, indent=2)

    def as_csv(self) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(self.used_fields)
        for r in self.flat_results:
            writer.writerow([r.get(f, "") for f in self.used_fields])
        return output.getvalue()

    def as_xml(self) -> str:
        root = ET.Element("results")
        for word_stem_list in self.results:
            word_elem = ET.SubElement(root, "word")
            for r in word_stem_list:
                word_stem = ET.SubElement(word_elem, "wordstem", text=r.get("word", ""))
                for k in self.used_fields:
                    if k in r:
                        ET.SubElement(word_stem, k).text = str(r[k])
        xml_io = io.StringIO()
        ET.ElementTree(root).write(xml_io, encoding="unicode", xml_declaration=True)
        return xml_io.getvalue()

    # --- Save to file ---
    def to_json(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.as_json())

    def to_csv(self, filepath):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            f.write(self.as_csv())

    def to_xml(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.as_xml())

    def save_all(self, base_path):
        self.to_json(base_path + ".json")
        self.to_csv(base_path + ".csv")
        self.to_xml(base_path + ".xml")

    # --- Filtering ---
    def filter(self, **conditions):
        # print("Conditions", conditions)
        filtered = []
        for word_stem_list in  self.results:
            filtered.append([
                r for r in word_stem_list
                # if any(r.get(k, "") == v for k, v in conditions.items())
                if all(str(r.get(k, "")).strip() == str(v).strip() for k, v in conditions.items())
            ])
        return filtered

    # --- Grouping ---
    def group_by(self, key):
        grouped = defaultdict(list)
        for r in self.flat_results:
            k = r.get(key, "word")
            grouped[k].append(r)
        return grouped

    # --- Raw access ---
    def as_dicts(self):
        return self.results
