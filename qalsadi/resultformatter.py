import json
import csv
import io
import xml.etree.ElementTree as ET
from tabulate import tabulate
from collections import defaultdict
from .stemmedword import  StemmedWord
from .abstractresultformatter import AbstractResultFormatter
# def is_list_of_lists_of_type(obj, cls):
#     return (
#         isinstance(obj, list) and
#         all(isinstance(sub, list) and all(isinstance(item, cls) for item in sub)
#             for sub in obj)
#     )
class ResultFormatter(AbstractResultFormatter):
    def __init__(self, results):
        self.results = results
        assert self._is_valid_result_type(results)

        self.flat_results = self.flatten(results)
        # self.flat_results = [dict(item) for sublist in results for item in sublist]
        # self.flat_results = [item.__dict__ for sublist in results for item in sublist]
        self.all_fields = self._collect_all_fields()
        self.used_fields = list(self.all_fields)  # default is all
        # #['action', 'affix', 'affix_key', 'freq', 'lemma', 'need', 'object_type', 'original', 'original_tags', 'root',
        #  'semivocalized', 'stem', 'tag_added', 'tag_break', 'tag_confirmed', 'tag_gender', 'tag_initial', 'tag_mamnou3',
        #  'tag_mood', 'tag_number', 'tag_original_gender', 'tag_original_number', 'tag_person', 'tag_pronoun',
        #  'tag_regular', 'tag_tense', 'tag_transitive', 'tag_transparent', 'tag_type', 'tag_voice', 'tags', 'type',
        #  'unvocalized', 'vocalized', 'word']

        self.profiles = {
            "main": ["id", "word", "vocalized", "stem", "affix", "lemma", "type","tags"],
            "all": self.all_fields,
            "roots": ["id", "word", "root"],
            "lemmas": ["id", "word", "lemma"],
            "inflect": [
                "id","word", "vocalized", "stem", "affix", "lemma", "type", "tags",
            ],
            "custom":[],
        }


    def flatten(self, results):
        flat_results = [
            {**item, 'id': i}
            for i, item in enumerate(
                item for sublist in results for item in sublist
            )
        ]
        return flat_results

    def _is_valid_result_type(self, result):
        return self._is_list_of_lists_of_type(result, StemmedWord)

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
    def as_format(self, tablefmt="table"):
        """
        display as given format
        """
        if tablefmt == 'html':
            output = self.as_table(tablefmt="html")
            output = output.replace('<table>', '<table id="datatable">')
        elif tablefmt == 'json':
            output = self.as_json()
        elif tablefmt == 'csv':
            output = self.as_csv()
        elif tablefmt == 'xml':
            output = self.as_xml()
        elif tablefmt == 'tree':
            output = self.as_tree()

        elif tablefmt == 'htmltree':
            output = self.as_html_tree()
        else:
            output = self.as_table()
        return output

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

    @staticmethod
    def extract_affix_tree(solution):
        # The affix is a list joined by '-',
        # two first are prefixes, the seconds two are suffixes
        return {
            "word": solution.get("word", ""),
            "prefixes": solution.get("affix", "").split("-")[:2],
            "stem": solution.get("stem", ""),
            "root": solution.get("root", ""),
            "pattern": solution.get("pattern", ""),
            "suffixes": solution.get("affix", "").split("-")[2:],
            "lemma": solution.get("lemma", "")
        }
    @staticmethod
    def render_morphology_ascii(tree):
        """
        Build an ASCII Tree (Text Output)
        """
        lines = []
        lines.append(f"Word: {tree['word']}")
        lines.append(f" ├─ Lemma: {tree['lemma']}")
        if any(tree['prefixes']):
            lines.append(" ├─ Prefixes:")
            for p in tree['prefixes']:
                if p.strip():
                    lines.append(f" │   └─p {p}")

        lines.append(f" ├─ Stem: {tree['stem']}")

        if any(tree['suffixes']):
            lines.append(" └─ Suffixes:")
            for s in tree['suffixes']:
                if s.strip():
                    lines.append(f"     └─s {s}")
        return "\n".join(lines)
    @staticmethod
    def render_tree_html(tree):
        def li(content):
            return f"<li>{content}</li>"

        def ul(items):
            return f"<ul>{''.join(items)}</ul>"

        prefix_items = [li(p.strip()) for p in tree["prefixes"] if p.strip()]
        suffix_items = [li(s.strip()) for s in tree["suffixes"] if s.strip()]

        return f"""
        <li>{tree['word']}
            <ul>
                {li('Lemma: ' + tree['lemma'])}
                {li('Root: ' + tree['root'])}
                {li('Pattern: ' + tree['pattern'])}
                {li('Prefixes:' + ul(prefix_items) if prefix_items else '')}
                {li('Stem: ' + tree['stem'])}
                {li('Suffixes:' + ul(suffix_items) if suffix_items else '')}
            </ul>
        </li>
        """

    def as_html_tree(self):
        trees_html = [self.render_tree_html(self.extract_affix_tree(r)) for r in self.flat_results]
        return ''.join(trees_html)

    def as_tree(self):
          return "\n\n".join(
            self.render_morphology_ascii(self.extract_affix_tree(r)) for r in self.flat_results
        )
    # --- Raw access ---
    def as_dicts(self):
        return self.results
