# qalsadi/__main__.py

import sys
import argparse
from .analex import Analex
from .lemmatizer import Lemmatizer
from .resultformatter import ResultFormatter
import json


def read_input(args):
    if args.stdin:
        return sys.stdin.read()
    elif args.file:
        with open(args.file, encoding="utf-8") as f:
            return f.read()
    elif args.text:
        return args.text
    else:
        print("Error: Provide input using --text, --file, or --stdin")
        sys.exit(1)


def run_analyze(args, text):
    analyzer = Analex()
    analyzer.set_limit(args.limit)
    results = analyzer.check_text(text)

    formatter = ResultFormatter(results)
    formatter.set_used_fields(profile=args.profile)
    output = formatter.as_format(tablefmt=args.format)
    print(output)


def run_lemmatize(args, text):
    lemmatizer = Lemmatizer()
    lemmas = lemmatizer.lemmatize_text(text, return_pos=args.return_pos, all=args.all)

    if args.format == "json":
        print(json.dumps(lemmas, ensure_ascii=False, indent=2))
    else:
        for group in lemmas:
            if isinstance(group, list):
                print(" / ".join(str(l) for l in group))
            else:
                print(group)


def main():
    parser = argparse.ArgumentParser(
        description="Qalsadi Arabic Morphological Analyzer"
    )

    parser.add_argument("--mode", choices=["analyze", "lemmatize"], default="analyze", help="Choose mode (default: analyze)")

    # Input
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--text", help="Input Arabic text")
    input_group.add_argument("--file", help="Path to input file")
    input_group.add_argument("--stdin", action="store_true", help="Read input from stdin")

    # Common output format
    parser.add_argument("--format", choices=["json", "csv", "html", "table"], default="table", help="Output format")

    # Analyze options
    parser.add_argument("--profile", choices=["main", "all", "lemmas", "roots", "inflect", "custom"], default="main")
    parser.add_argument("--limit", type=int, default=10000, help="Word limit")

    # Lemmatize options
    parser.add_argument("--return-pos", action="store_true", help="Include POS in lemma output")
    parser.add_argument("--all", action="store_true", help="Return all lemmas, not just best guess")

    args = parser.parse_args()
    text = read_input(args)

    if args.mode == "analyze":
        run_analyze(args, text)
    elif args.mode == "lemmatize":
        run_lemmatize(args, text)


if __name__ == "__main__":
    main()
