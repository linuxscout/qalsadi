#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import pprint
from io import open

import pyarabic.araby as araby

# sys.path.append('../')
import qalsadi.analex as qanalex
import qalsadi.cache_codernity
import qalsadi.cache_pickle
import mysam.tagmaker
from console_progressbar import ProgressBar

# Optional dependency
PANDAS = False
if PANDAS:
    try:
        import pandas as pd

        PANDAS = True
    except ImportError:
        PANDAS = False


def grab_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Test Qalsadi Analex.")

    parser.add_argument(
        "-f",
        dest="filename",
        required=True,
        help="Input file to analyze",
        metavar="FILE",
    )
    parser.add_argument(
        "-o",
        dest="outfile",
        default=None,
        help="Optional output file",
        metavar="OUT_FILE",
    )
    parser.add_argument(
        "-c",
        dest="command",
        default="test_one",
        help="Command to run: test_quran or test_one",
        metavar="COMMAND",
    )
    parser.add_argument(
        "-l",
        dest="limit",
        type=int,
        default=0,
        help="Limit number of lines to process",
        metavar="LIMIT",
    )
    parser.add_argument(
        "--all", action="store_true", help="Process all lines regardless of limit"
    )

    return parser.parse_args()


class Tester:
    def __init__(self):
        pass

    @staticmethod
    def setup_analyzer(use_codernity=True, debug=False):
        analyzer = qanalex.Analex(cache_path="cache/")
        if use_codernity:
            db_path = os.path.join(os.path.dirname(__file__), "cache", ".qalsadiCache")
            cacher = qalsadi.cache_codernity.Cache(db_path)
        else:
            cacher = qalsadi.cache_pickle.Cache("IMPORTANT")

        analyzer.set_cacher(cacher)
        analyzer.enable_allow_cache_use()
        analyzer.set_debug(debug)
        return analyzer

    @staticmethod
    def analyze_lines(analyzer, lines, limit=0):
        if limit <= 0:
            limit = len(lines)

        progress = ProgressBar(
            total=limit,
            prefix="",
            suffix="",
            decimals=2,
            length=50,
            fill="#",
            zfill="-",
            file=sys.stderr,
        )
        results = []

        for idx, line in enumerate(lines[:limit]):
            results.extend(analyzer.check_text(line))
            progress.print_progress_bar(idx)

        return results

    @staticmethod
    def flatten_analysis(results):
        return [item.__dict__ for sublist in results for item in sublist]

    def test_quran(self, text_lines, debug, outfile, limit=0):
        analyzer = self.setup_analyzer(use_codernity=True, debug=debug)
        analyzer.enable_fully_vocalized_input()

        results = self.analyze_lines(analyzer, text_lines, limit)
        adapted_result = self.flatten_analysis(results)

        if not adapted_result:
            print("No analysis results found.")
            return

        if PANDAS:
            df = pd.DataFrame(adapted_result)
            display = df[
                [
                    "vocalized",
                    "unvocalized",
                    "word",
                    "stem",
                    "type",
                    "root",
                    "original",
                    "tags",
                ]
            ].drop_duplicates()
            display.to_csv(outfile or "output.csv", sep="\t", encoding="utf8")

            # Split unknown and known
            display[display.type == "unknown"].to_csv(
                f"{outfile}.unknown.csv", sep="\t", encoding="utf8"
            )
            display[display.type != "unknown"].to_csv(
                f"{outfile}.known.csv", sep="\t", encoding="utf8"
            )

            print("Unknown:", display[display.type == "unknown"].shape[0])
            print("Known:", display[display.type != "unknown"].shape[0])
        else:
            pprint.pprint(adapted_result)

    def test_one(self, text_lines, debug, outfile, limit=0):
        analyzer = self.setup_analyzer(use_codernity=False, debug=debug)
        results = self.analyze_lines(analyzer, text_lines, limit)
        adapted_result = self.flatten_analysis(results)

        if not adapted_result:
            print("Empty output.")
            sys.exit(1)

        # TagMaker usage
        tagger = mysam.tagmaker.tagMaker()
        tagger.debug = True
        tagger.lang = "en"

        for entry in adapted_result:
            tagger._encode(entry.get("tags", "").split(":"))
            tagger._encode(entry.get("type", "").split(":"))
            print(tagger)
            print(tagger._decode())
            tagger.reset()

        if PANDAS:
            df = pd.DataFrame(adapted_result)
            display = df[
                [
                    "vocalized",
                    "unvocalized",
                    "word",
                    "stem",
                    "type",
                    "root",
                    "original",
                    "tags",
                ]
            ].drop_duplicates()
            display.to_csv(outfile or "output.csv", sep="\t", encoding="utf8")

    def run(self, command, text_lines, limit, debug, outfile):
        if command == "test_quran":
            self.test_quran(text_lines, debug, outfile, limit)
        else:
            self.test_one(text_lines, debug, outfile, limit)


def main():
    args = grab_args()

    try:
        with open(args.filename, encoding="utf-8") as file:
            text_lines = file.readlines()
    except Exception as e:
        print(f"Error reading input file: {e}")
        text_lines = ["أسلم"]

    limit = args.limit if not args.all else 0
    debug = False

    tester = Tester()
    tester.run(args.command, text_lines, limit, debug, args.outfile)


if __name__ == "__main__":
    sys.exit(main())
