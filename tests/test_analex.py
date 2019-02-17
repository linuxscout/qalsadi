#!/usr/bin/python
# -*- coding = utf-8 -*-
from __future__ import absolute_import

import argparse
import sys
import pyarabic.araby as araby
def grabargs():
    parser = argparse.ArgumentParser(description='Test Qalsadi Analex.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=True,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-o", dest="outfile", nargs='?', 
    help="Output file to convert", metavar="OUT_FILE")
    parser.add_argument("-c", dest="command", nargs='?', 
    help="command to run", metavar="COMMAND")
    
    parser.add_argument("--all", type=bool, nargs='?',
                        const=True, 
                        help="")
    args = parser.parse_args()
    return args
    
#~ import qalsadi.analex as qanalex
sys.path.append('../qalsadi')
import analex as qanalex

import pandas as pd
class tester:
    def __init__(self,):
        pass
    @staticmethod
    def test_quran(text, debug, outfile):
        analyzer = qanalex.Analex(cache_path="cache/")
        analyzer.disable_allow_cache_use()
        analyzer.enable_fully_vocalized_input()
        analyzer.set_debug(debug);
        result = analyzer.check_text(text);

        adapted_result = []

        for i, analyzed_list in enumerate(result):
            for analyzed in analyzed_list:
                adapted_result.append(analyzed.__dict__)

        df = pd.DataFrame(adapted_result)
        print df.columns.values
        #~ print(df.columns.values)
        #~ print(df.head(12))
        display = df[['vocalized','unvocalized', 'word','stem','type','root', 'original', "tags"]]
        display = display.drop_duplicates()
        #~ print(display.head(10))
        #~ print(display)
        #~ print("root exists ", ('root' in df.columns))
        display.to_csv(outfile, sep='\t', encoding="utf8")
        display_unknown = display[display.type =="unknown"]
        display_unknown.to_csv(outfile+".unknown.csv",sep='\t',encoding='utf8')
        display_known = display[display.type !="unknown"]
        display_known.to_csv(outfile+".known.csv",sep='\t',encoding='utf8')
        print("Unknown ",display_unknown.count())      
        print("known ",display_known.count())      

    @staticmethod
    def test_one(text, debug, outfile):
        analyzer = qanalex.Analex(cache_path="cache/")
        analyzer.disable_allow_cache_use()
        #~ analyzer.enable_fully_vocalized_input()
        debug = True
        analyzer.set_debug(debug);
        #~ tokens = araby.tokenize(text)
        #~ if tokens:
            #~ text = tokens[0]
        result = analyzer.check_text(text);
        adapted_result = []

        for i, analyzed_list in enumerate(result):
            for analyzed in analyzed_list:
                adapted_result.append(analyzed.__dict__)

        df = pd.DataFrame(adapted_result)
        print df.columns.values
        #~ print(df.columns.values)
        #~ print(df.head(12))
        display = df[['vocalized','unvocalized', 'word','stem','type','root', 'original', "tags"]]
        display = display.drop_duplicates()
        display.to_csv(outfile, sep='\t', encoding="utf8")

    def run(self, command, text, limit, debug, outfile):
        """ run command to test"""
        if command=="test_quran":
            df = self.test_quran(text, debug, outfile)
        elif command=="test_one":
            df = self.test_one(text, debug, outfile)
        else:
            print("choose a command")
            
def main(args):
    args = grabargs()
    filename = args.filename
    outfile = args.outfile
    command = args.command
    try:
        myfile=open(filename)
        text=(myfile.read()).decode('utf8');

        if text == None:
            text=u"السلام عليكم يستعملونهم"
    except:
        text=u"أسلم"
        print " given text"

    #~ debug=True;
    debug=False;
    limit=500
    mytester = tester()
    
    #~ command = "test_quran"
    mytester.run(command, text, limit, debug, outfile)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
