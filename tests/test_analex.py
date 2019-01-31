#!/usr/bin/python
# -*- coding = utf-8 -*-
from __future__ import absolute_import

import argparse
import sys
def grabargs():
    parser = argparse.ArgumentParser(description='Test Qalsadi Analex.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=True,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-o", dest="outfile", nargs='?', 
    help="Output file to convert", metavar="OUT_FILE")
    
    parser.add_argument("--all", type=bool, nargs='?',
                        const=True, 
                        help="")
    args = parser.parse_args()
    return args
    
#~ import qalsadi.analex as qanalex
sys.path.append('../qalsadi')
import analex as qanalex

import pandas as pd

def main(args):
    args = grabargs()
    filename = args.filename
    outfile = args.outfile
    try:
        myfile=open(filename)
        text=(myfile.read()).decode('utf8');

        if text == None:
            text=u"السلام عليكم يستعملونهم"
    except:
        text=u"أسلم"
        print " given text"

    debug=True;
    limit=500
    analyzer = qanalex.Analex(cache_path="cache/")
    analyzer.disable_allow_cache_use()
    analyzer.set_debug(debug);
    result = analyzer.check_text(text);

    adapted_result = []

    for i, analyzed_list in enumerate(result):
        for analyzed in analyzed_list:
            adapted_result.append(analyzed.__dict__)

    df = pd.DataFrame(adapted_result)
    print df.columns.values
    print(df.columns.values)
    print(df.head(12))
    display = df[['word','stem','type','root', 'original']]
    display = display.drop_duplicates()
    #~ print(display.head(10))
    print(display)
    print("root exists ", ('root' in df.columns))
    display.to_csv(outfile, sep='\t', encoding="utf8")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
