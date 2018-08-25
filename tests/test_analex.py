#!/usr/bin/python
# -*- coding = utf-8 -*-
#~ from __future__ import absolute_import

import qalsadi.analex as qanalex


filename="samples/text.txt"

try:
    myfile=open(filename)
    text=(myfile.read()).decode('utf8');

    if text == None:
        text=u"السلام عليكم يستعملونهم"
except:
    text=u"أسلم"
    print " given text"

debug=False;
limit=500
analyzer = qanalex.Analex(cache_path="cache/")
analyzer.disable_allow_cache_use()
analyzer.set_debug(debug);
result = analyzer.check_text(text);

import pandas as pd
adapted_result = []

for i, analyzed_list in enumerate(result):
    for analyzed in analyzed_list:
        adapted_result.append(analyzed.__dict__)

df = pd.DataFrame(adapted_result)
print df.columns.values
print(df.columns.values)
print(df.head(12))
display = df[['word','stem','type','root']]
display = display.drop_duplicates()
#~ print(display.head(10))
print(display)
print("root exists ", ('root' in df.columns))
display.to_csv('output/test.csv',sep='\t', encoding="utf8")
