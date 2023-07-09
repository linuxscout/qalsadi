#!/usr/bin/python
# -*- coding = utf-8 -*-

from io import open
import argparse
import sys
import os
import pyarabic.araby as araby
import mysam.tagmaker
from console_progressbar import ProgressBar

def grabargs():
    parser = argparse.ArgumentParser(description='Test Qalsadi Analex.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=True,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-o", dest="outfile", nargs='?', 
    help="Output file to convert", metavar="OUT_FILE")
    parser.add_argument("-c", dest="command", nargs='?', 
    help="command to run", metavar="COMMAND")
    parser.add_argument("-l", dest="limit", type=int, nargs='?', default=0, 
    help="limit lines to treat", metavar="LIMIT")
    
    parser.add_argument("--all", type=bool, nargs='?',
                        const=True, 
                        help="")
    args = parser.parse_args()
    return args
    
#~ import qalsadi.analex as qanalex
#~ sys.path.append('../qalsadi')
sys.path.append('../')
import qalsadi.analex as qanalex
import qalsadi.cache_codernity
import qalsadi.cache_pickle
import qalsadi.cache_pickledb
PANDAS = False
# test performance without pandas
if PANDAS:
    import pandas as pd
class tester:
    def __init__(self,):
        pass
    @staticmethod
    def test_quran(text, debug, outfile):
        analyzer = qanalex.Analex(cache_path="cache/")
        #~ analyzer.disable_allow_cache_use()
        # install a cache system for analyzer
        db_path = os.path.join(os.path.dirname(__file__),"cache", '.qalsadiCache')
        cacher = qalsadi.cache_codernity.Cache(db_path)
        analyzer.set_cacher(cacher)
        analyzer.enable_allow_cache_use()        

        analyzer.enable_fully_vocalized_input()
        analyzer.set_debug(debug);
        result = analyzer.check_text(text);

        adapted_result = []

        for i, analyzed_list in enumerate(result):
            for analyzed in analyzed_list:
                adapted_result.append(analyzed.__dict__)

        if not PANDAS:
            pprint.pprint(adapted_result = [])
        else:
            df = pd.DataFrame(adapted_result)


            print(df.columns.values)

            #~ print(df.columns.values)
            #~ print(df.head(12))
            display = df[['vocalized','unvocalized', 'word','stem','type','root', 'original', "tags"]]
            display = display.drop_duplicates()
            #~ print(display.head(10))
            #~ print(display)
            #~ print("root exists ", ('root' in df.columns))
            display.to_csv(outfile, sep=str('\t'), encoding="utf8")
            display_unknown = display[display.type =="unknown"]
            display_unknown.to_csv(outfile+".unknown.csv",sep='\t',encoding='utf8')
            display_known = display[display.type !="unknown"]
            display_known.to_csv(outfile+".known.csv",sep='\t',encoding='utf8')
            print("Unknown ",display_unknown.count())      
            print("known ",display_known.count())      

    @staticmethod
    def test_one(text, debug, outfile, limit=False):
        
        analyzer = qanalex.Analex(allow_tag_guessing=True)
        # configure cache
        # ~ db_path = os.path.join(os.path.abspath("./"),"cache", '.qalsadiCache')
        # ~ print(__file__, db_path)
        # ~ cacher = qalsadi.cache_codernity.Cache(db_path)
        # ~ analyzer.set_cacher(cacher)
        
        cacher = qalsadi.cache_pickle.Cache("IMPORTANT")
        analyzer.set_cacher(cacher)
        
        analyzer.enable_allow_cache_use()  
        # ~ analyzer.disable_allow_cache_use()        

        analyzer.set_debug(debug);
        print(len(text))
        if type(text) ==str:
            result = analyzer.check_text(text);
        elif type(text) == list:

            if not limit :
                limit = len(text)
            progress = ProgressBar(total=limit,prefix='', suffix='', decimals=2, length=50, fill='#', zfill='-', file=sys.stderr)

            lines = text
            result = []
            for counter, line in enumerate(lines[:limit]):
                result += analyzer.check_text(line);
                progress.print_progress_bar(counter)
        adapted_result = []
        # flatten
        for i, analyzed_list in enumerate(result):
            for analyzed in analyzed_list:
                adapted_result.append(analyzed.__dict__)
                #~ adapted_result.append(vars(analyzed))
        if(not adapted_result):
            print("Empty out Data")
            sys.exit()
        # test tagmaker
        mytagmaker = mysam.tagmaker.tagMaker()
        mytagmaker.debug = True
        mytagmaker.lang = "en"
        for adp in adapted_result:
            mytagmaker._encode(adp.get("tags").split(':'))
            mytagmaker._encode(adp.get("type").split(':'))
            print(str(mytagmaker))
            print(str(mytagmaker._decode()))
            mytagmaker.reset()
            
        #~ print("Adapted Data")
        #~ print(adapted_result)
        if PANDAS:
            df = pd.DataFrame(adapted_result)
            print(df.columns.values)
            #~ sys.exit()
            #~ print(df.columns.values)
            #~ print(df.head(12))
            display = df[['vocalized','unvocalized', 'word','stem','type','root', 'original', "tags"]]
            display = display.drop_duplicates()
            display.to_csv(outfile, sep=str('\t'), encoding="utf8")

    def run(self, command, text, limit, debug, outfile):
        """ run command to test"""
        if command=="test_quran":
            df = self.test_quran(text, debug, outfile)
        elif command=="test_one":
            df = self.test_one(text, debug, outfile, limit)
        else:
            df = self.test_one(text, debug, outfile, limit)
            #print("choose a command")
            
def main(args):
    args = grabargs()
    filename = args.filename
    outfile = args.outfile
    command = args.command
    limit = args.limit
    try:
        myfile=open(filename, encoding="utf-8")
        text=(myfile.readlines())#.decode('utf8');
        #~ print(len(araby.tokenize(text)))
        #~ sys.exit()
        if text == None:
            text=u"السلام عليكم يستعملونهم"
    except:
        text=u"أسلم"
        print(" given text")

    #~ debug=True;
    debug=False;
    #~ limit=500
    if not limit:
        limit = 100000000
    mytester = tester()
    
    #~ command = "test_quran"
    mytester.run(command, text, limit, debug, outfile)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
