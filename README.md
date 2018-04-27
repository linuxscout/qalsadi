#Qalsadi Arabic Morphological Analyzer for Python



  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/qalsadi/master/AUTHORS.md)
Release  | 0.2 
License  |[GPL](https://github.com/linuxscout/qalsadi/master/LICENSE)
Tracker  |[linuxscout/qalsadi/Issues](https://github.com/linuxscout/qalsadi/issues)
Website  |[https://pypi.python.org/pypi/qalsadi](https://pypi.python.org/pypi/qalsadi)
Doc  |[package Documentaion](http://pythonhosted.org/qalsadi/)
Source  |[Github](http://github.com/linuxscout/qalsadi)
Download  |[sourceforge](http://qalsadi.sourceforge.net)
Feedbacks  |[Comments](http://tahadz.com/qalsadi/contact)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projects/qalsadi/)



## Citation
If you would cite it in academic work, can you use this citation
```
T. Zerrouki‏, Qalsadi, Arabic mophological analyzer Library for python.,  https://pypi.python.org/pypi/qalsadi/
```
or in bibtex format
```bibtex
@misc{zerrouki2012qalsadi,
  title={qalsadi, Arabic mophological analyzer Library for python.},
  author={Zerrouki, Taha},
  url={https://pypi.python.org/pypi/qalsadi},
  year={2012}
}
```


##   مزايا
 
 
## Features
 - Arabic word Light Stemming.
* Features:
	- Vocalized Text Analyzer, 
	- Use Qutrub library to analyze verbs.
	- give word frequency in arabic modern use.
 
* Requirement:
	- libQutrub: Qutrub verb conjugation library: http://pypi.pyton/LibQutrub
	- PyArabic: Arabic language tools library   : http://pypi.pyton/pyarabic
	- Tashaphyne;Arabic Light Stemmer library	: http://pypi.python.org/pypi/Tashaphyne/


Applications
====
* Stemming texts
* Text Classification and categorization
* Sentiment Analysis
* Named Entities Recognition

Installation
=====
```
pip install qalsadi
```    
Requirements
----------------
 - libQutrub: Qutrub verb conjugation library: http://pypi.pyton/LibQutrub
 - PyArabic: Arabic language tools library   : http://pypi.pyton/pyarabic
 - Tashaphyne;Arabic Light Stemmer library	: http://pypi.python.org/pypi/Tashaphyne/
 - Naftawayh : Arabic words tagger: 	: http://pypi.python.org/pypi/Naftawayh/ 
 - Arramooz : Arabic dictionary
 - CodernityDB : No Sql native python database 
  
Usage
=====




### Example 

``` python
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
analyzer=Analex()
analyzer.set_debug(debug);
result = analyzer.check_text(text);
print '----------------python format result-------'
print result
for i in range(len(result)):
#       print "--------تحليل كلمة  ------------", word.encode('utf8');
    print "-------------One word detailed case------";
    for analyzed in  result[i]:
        print "-------------one case for word------";
        print repr(analyzed);
```





Files
=====
* file/directory    category    description 



## Featured Posts


