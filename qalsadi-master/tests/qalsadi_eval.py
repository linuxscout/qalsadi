import os
import csv
import re
import argparse
import xml.etree.ElementTree as ET
import qalsadi.lemmatizer
from pyarabic.araby import strip_tashkeel, strip_lastharaka

class QalsadiEvaluator:
    def __init__(self, folder, recursive=False, ignore_diacritics=False, csv_file=None, limit=None):
        self.folder = folder
        self.recursive = recursive
        # self.ignore_diacritics = ignore_diacritics
        self.csv_file = csv_file
        self.limit = limit
        self.lemmatizer = qalsadi.lemmatizer.Lemmatizer()
        self.lemmatizer.set_vocalized_lemma()
        self.all_mismatches = []
        self.total = 0
        self.correct = 0
        self.correct_vocalized = 0
        self.total_sentences = 0

    def normalize(self, text):
        """Remove Arabic diacritics using pyarabic."""
        return strip_tashkeel(text)

    def normalize_end(self, text):
        """Remove Arabic diacritics using pyarabic."""
        return strip_lastharaka(text)

    def extract_lemma(self, word):
        """Use Qalsadi to extract lemmas."""
        lemmas = self.lemmatizer.lemmatize(word, all=True)
        return lemmas

    def match_lemma(self, gold_lemma, predicted_lemmas, vocalized=False):
        """Compare gold lemma to predicted lemmas, considering normalization if needed."""
        # if not vocalized or self.ignore_diacritics:
        if not vocalized:
            gold_lemma = self.normalize(gold_lemma)
            predicted_lemmas = [self.normalize(p) for p in predicted_lemmas]
        elif vocalized:
            gold_lemma = self.normalize_end(gold_lemma)
            predicted_lemmas = [self.normalize_end(p) for p in predicted_lemmas]
        return gold_lemma in predicted_lemmas

    def evaluate_file(self, xml_path):
        """Evaluate a single XML file."""
        tree = ET.parse(xml_path)
        root = tree.getroot()

        file_total = 0
        file_correct = 0
        file_correct_vocalized = 0
        file_sentences = 0
        mismatches = []

        for sentence in root.findall(".//sentence"):
            file_sentences += 1
            sentence_id = sentence.get("id", "")
            for lexical in sentence.findall(".//ArabicLexical"):
                word = lexical.get("word")

                word_nm = strip_tashkeel(word)
                gold_lemma = lexical.get("lemma")
                predicted_lemmas = self.extract_lemma(word_nm)

                if self.match_lemma(gold_lemma, predicted_lemmas, vocalized=False):
                    file_correct += 1
                else:
                    mismatches.append({
                        "filename": os.path.basename(xml_path),
                        "sentence_id": sentence_id,
                        "word": word,
                        "gold_lemma": gold_lemma,
                        "predicted_lemmas": "|".join(predicted_lemmas),
                        "vocalized":"no"
                    })
                if self.match_lemma(gold_lemma, predicted_lemmas, vocalized=True):
                    file_correct_vocalized += 1
                else:
                    mismatches.append({
                        "filename": os.path.basename(xml_path),
                        "sentence_id": sentence_id,
                        "word": word,
                        "gold_lemma": gold_lemma,
                        "predicted_lemmas": "|".join(predicted_lemmas),
                        "vocalized":"yes"
                    })

                file_total += 1

        return file_total, file_correct, file_correct_vocalized, file_sentences, mismatches

    def get_xml_files(self):
        """Recursively or flatly collect all XML files."""
        xml_files = []
        for root_dir, _, files in os.walk(self.folder):
            for file in files:
                if file.endswith(".xml"):
                    xml_files.append(os.path.join(root_dir, file))
            if not self.recursive:
                break
        if self.limit:
            xml_files = xml_files[:self.limit]
        return xml_files

    def run(self):
        """Run the evaluation across all XML files."""
        xml_files = self.get_xml_files()
        print(f"🔍 Found {len(xml_files)} XML file(s).")
        summary_rows = []

        for num, path in enumerate(xml_files):
            print(f"\n📄 {num+1}. Processing file:  {os.path.basename(path)}")
            total, correct, correct_vocalized, sentences, mismatches = self.evaluate_file(path)

            accuracy = correct / total * 100 if total else 0
            accuracy_vocalized = correct_vocalized / total * 100 if total else 0
            print(f"  ➤ Total sentences: {sentences}")
            print(f"  ➤ Total words: {total}")
            print(f"  ➤ Correct matches: {correct}")
            print(f"  ➤ Correct vocalized matches: {correct_vocalized}")
            print(f"  ➤ Accuracy: {accuracy:.2f}%")
            print(f"  ➤ Accuracy Vocalized: {accuracy_vocalized:.2f}%")
            print(f"  ❌ Mismatches: {len(mismatches)}")

            self.total += total
            self.correct += correct
            self.correct_vocalized += correct_vocalized
            self.total_sentences += sentences
            self.all_mismatches.extend(mismatches)

            summary_rows.append({
                "filename": os.path.basename(path),
                "sentences": sentences,
                "total": total,
                "correct": correct,
                "correct_vocalized": correct_vocalized,
                "accuracy": f"{accuracy:.2f}",
                "accuracy_vocalized": f"{accuracy_vocalized:.2f}"
            })

        self.report_summary()

        if self.csv_file:
            self.export_csv()

        if summary_rows:
            self.export_summary_by_file(summary_rows)

    def report_summary(self):
        """Print summary stats."""
        print("\n=== 🧾 Overall Summary ===")
        print(f"Total Sentences: {self.total_sentences}")
        print(f"Total Words: {self.total}")
        print(f"Correct Matches: {self.correct}")
        print(f"Correct Vocalized Matches: {self.correct_vocalized}")
        overall_accuracy = self.correct / self.total * 100 if self.total else 0
        print(f"Overall Accuracy: {overall_accuracy:.2f}%")
        overall_vocalized_accuracy = self.correct_vocalized / self.total * 100 if self.total else 0
        print(f"Overall Vocalized Accuracy: {overall_vocalized_accuracy:.2f}%")

    def export_summary_by_file(self, summary_data, filename="summary.csv"):
        summary_file = self.csv_file[:-4] + ".summary.csv"
        with open(summary_file, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["filename", "sentences", "total", "correct", "correct_vocalized", "accuracy",'accuracy_vocalized'])
            writer.writeheader()
            writer.writerows(summary_data)
        print(f"\n📤 Overall Summary saved to: {summary_file}")

    def export_csv(self):
        """Export mismatches to a CSV file."""
        if not self.all_mismatches:
            print("✅ No mismatches to export.")
            return

        with open(self.csv_file, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["filename", "sentence_id", "word", "gold_lemma", "predicted_lemmas","vocalized"])
            writer.writeheader()
            writer.writerows(self.all_mismatches)

        print(f"\n📤 Mismatches saved to: {self.csv_file}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate Qalsadi lemmatizer against Arabic XML gold standard.")
    parser.add_argument("folder", help="Path to folder containing XML files")
    parser.add_argument("--csv", help="Export mismatches to CSV file (e.g. results.csv)")
    parser.add_argument("--recursive", action="store_true", help="Scan XML files in nested subfolders")
    # parser.add_argument("--ignore-diacritics", action="store_true", help="Ignore diacritics in lemma comparison")
    parser.add_argument("--limit", type=int, help="Limit the number of XML files to process")

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"❌ Error: '{args.folder}' is not a valid directory.")
        return

    evaluator = QalsadiEvaluator(
        folder=args.folder,
        recursive=args.recursive,
        # ignore_diacritics=args.ignore_diacritics,
        csv_file=args.csv,
        limit=args.limit
    )

    evaluator.run()


if __name__ == "__main__":
    main()