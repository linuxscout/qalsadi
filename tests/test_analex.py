#!/usr/bin/python
# -*- coding = utf-8 -*-
from __future__ import absolute_import
import sys
sys.path.append("../")
sys.path.append("../support")
#~ from . import qalsadi.analex
import qalsadi.analex


filename="samples/text.txt"

try:
    myfile=open(filename)
    text=(myfile.read()).decode('utf8');

    if text == None:
        text=u"السلام عليكم"
except:
    text=u"أسلم"
    print " given text"

debug=False;
limit=500
analyzer=qalsadi.analex.Analex(cache_path="cache/")
#ianalyzer.disable_allow_cache_use()
analyzer.set_debug(debug);
result = analyzer.check_text(text);

import pandas as pd
adapted_result = []

for i, analyzed_list in enumerate(result):
    for analyzed in analyzed_list:
        adapted_result.append(analyzed.__dict__)

df = pd.DataFrame(adapted_result)
print df
