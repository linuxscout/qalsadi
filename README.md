# Qalsadi Arabic Morphological Analyzer and Lemmatizer for Python



  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/qalsadi/master/AUTHORS.md)
Release  | 0.4.4
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
Another Citation:
```
Zerrouki, Taha. "Towards An Open Platform For Arabic Language Processing." (2020).
```
or in bibtex format

```bibtex
@misc{zerrouki2012qalsadi,
  title={qalsadi, Arabic mophological analyzer Library for python.},
  author={Zerrouki, Taha},
  url={https://pypi.python.org/pypi/qalsadi},
  year={2012}
}

```bibtex
@thesis{zerrouki2020towards,
  title={Towards An Open Platform For Arabic Language Processing},
  author={Zerrouki, Taha},
  year={2020}
}

```

 
## Features  مزايا
 - Lemmatization
 - Vocalized Text Analyzer, 
 - Use Qutrub library to analyze verbs.
 - give word frequency in arabic modern use.
 
### Applications

* Stemming texts
* Text Classification and categorization
* Sentiment Analysis
* Named Entities Recognition

### Installation

```
pip install qalsadi
```    
#### Requirements

``` 
pip install -r requirements.txt 
```

 - libQutrub: Qutrub verb conjugation library: http://pypi.pyton/LibQutrub
 - PyArabic: Arabic language tools library   : http://pypi.pyton/pyarabic
 - Tashaphyne;Arabic Light Stemmer library	: http://pypi.python.org/pypi/Tashaphyne/
 - Naftawayh : Arabic words tagger: 	: http://pypi.python.org/pypi/Naftawayh/ 
 - Arramooz-pysqlite : Arabic dictionary
 - CodernityDB : No Sql native python database 
  
## Usage

### Example 
* Lemmatization
```python
>>> import qalsadi.lemmatizer 
>>> text = u"""هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية" (الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" .. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""
>>> lemmer = qalsadi.lemmatizer.Lemmatizer()
>>> # lemmatize a word
... lemmer.lemmatize("يحتاج")
'احتاج'
>>> # lemmatize a word with a specific pos
>>> lemmer.lemmatize("وفي")
'في'
>>> lemmer.lemmatize("وفي", pos="v")
'وفى'

>>> 
>>> lemmas = lemmer.lemmatize_text(text)
>>> print(lemmas)
['هل', 'احتاج', 'إلى', 'ترجمة', 'كي', 'تفهم', 'خطاب', 'ملك', '؟', 'لغة', '"', 'كلاسيكي', '"(', 'فصحى', ')', 'موجود', 'في', 'كل', 'لغة', 'ذلك', 'لغة', '"', 'دارج', '"..', 'فرنسي', 'التي', 'درس', 'في', 'مدرسة', 'ليست', 'فرنسي', 'التي', 'استخدم', 'ناس', 'في', 'شوارع', 'باريس', '..', 'ملك', 'بريطانيا', 'لا', 'خطب', 'بلغة', 'شوارع', 'دنو', '..', 'كل', 'مقام', 'مقالي']
>>> # lemmatize a text and return lemma pos
... lemmas = lemmer.lemmatize_text(text, return_pos=True)
>>> print(lemmas)
[('هل', 'stopword'), ('احتاج', 'verb'), ('إلى', 'stopword'), ('ترجمة', 'noun'), ('كي', 'stopword'), ('تفهم', 'noun'), ('خطاب', 'noun'), ('ملك', 'noun'), '؟', ('لغة', 'noun'), '"', ('كلاسيكي', 'noun'), '"(', ('فصحى', 'noun'), ')', ('موجود', 'noun'), ('في', 'stopword'), ('كل', 'stopword'), ('لغة', 'noun'), ('ذلك', 'stopword'), ('لغة', 'noun'), '"', ('دارج', 'noun'), '"..', ('فرنسي', 'noun'), ('التي', 'stopword'), ('درس', 'verb'), ('في', 'stopword'), ('مدرسة', 'noun'), ('ليست', 'stopword'), ('فرنسي', 'noun'), ('التي', 'stopword'), ('استخدم', 'verb'), ('ناس', 'noun'), ('في', 'stopword'), ('شوارع', 'noun'), ('باريس', 'all'), '..', ('ملك', 'noun'), ('بريطانيا', 'noun'), ('لا', 'stopword'), ('خطب', 'verb'), ('بلغة', 'noun'), ('شوارع', 'noun'), ('دنو', 'verb'), '..', ('كل', 'stopword'), ('مقام', 'noun'), ('مقالي', 'noun')]

>>># Get vocalized output lemmas
>>> lemmer.set_vocalized_lemma()
>>> lemmas = lemmer.lemmatize_text(text)
>>> print(lemmas)
['هَلْ', 'اِحْتَاجَ', 'إِلَى', 'تَرْجَمَةٌ', 'كَيْ', 'تَفَهُّمٌ', 'خَطَّابٌ', 'مَلَكٌ', '؟', 'لُغَةٌ', '"', 'كِلاَسِيكِيٌّ', '"(', 'فُصْحَى', ')', 'مَوْجُودٌ', 'فِي', 'كُلَّ', 'لُغَةٌ', 'ذَلِكَ', 'لُغَةٌ', '"', 'دَارِجٌ', '"..', 'فَرَنْسِيّ', 'الَّتِي', 'دَرَسَ', 'فِي', 'مَدْرَسَةٌ', 'لَيْسَتْ', 'فَرَنْسِيّ', 'الَّتِي', 'اِسْتَخْدَمَ', 'نَاسٌ', 'فِي', 'شَوَارِعٌ', 'باريس', '..', 'مَلَكٌ', 'برِيطانِيا', 'لَا', 'خَطَبَ', 'بَلَغَةٌ', 'شَوَارِعٌ', 'أَدَانَ', '..', 'كُلَّ', 'مَقَامٌ', 'مَقَالٌ']
>>> 


```

* Morphology analysis
``` python
filename="samples/text.txt"
import qalsadi.analex as qa
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
analyzer = qa.Analex()
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



## Output description


| Category | Applied on | feature | شرح                         | example |
|-------------|----------------|-----------|--------------------------|-------------|
| affix | all | affix_key | مفتاح الزوائد | ال--َاتُ-|البيانات |
| affix | all | affix | الزوائد |  |
| input | all | word | الكلمة المدخلة | البيانات |
| input | all | unvocalized | غير مشكول |  |
| morphology | noun | tag_mamnou3 | ممنوع من الصرف | 0 |
| morphology | verb | tag_confirmed | خاصية الفعل المؤكد | 0 |
| morphology | verb | tag_mood |  حالة الفعل المضارع (منصوب، مجزوم، مرفوع) | 0 |
| morphology | verb | tag_pronoun | الضمير | 0 |
| morphology | verb | tag_transitive | التعدي اللزوم | 0 |
| morphology | verb | tag_voice | البناء للمعلوم/ البناء للمجهول | 0 |
| morphology | noun | tag_regular | قياسي/ سماعي | 1 |
| morphology | noun/verb | tag_gender | النوع ( مؤنث مذكر) | 3 |
| morphology | verb | tag_person | الشخص (المتكلم الغائب المخاطب) | 4 |
| morphology | noun | tag_number | العدد(فرد/مثنى/جمع) | 21 |
| original | noun/verb | freq | درجة  شيوع الكلمة | 694644 |
| original | all | original_tags | خصائص الكلمة الأصلية | (u |
| original | all | original | الكلمة الأصلية | بَيَانٌ |
| original | all | root | الجذر | بين |
| original | all | tag_original_gender | جنس الكلمة الأصلية | مذكر |
| original | noun | tag_original_number | عدد الكلمة الأصلية | مفرد |
| output | all | type | نوع الكلمة | Noun:مصدر |
| output | all | semivocalized | الكلمة مشكولة بدون علامة الإعراب | الْبَيَانَات |
| output | all | vocalized | الكلمةمشكولة | الْبَيَانَاتُ |
| output | all | stem | الجذع | بيان |
| output | all | tags |  | تعريف::جمع مؤنث سالم:مرفوع:متحرك:ينون:جمع::: |
| syntax | all | tag_break | الكلمة منفصلة عمّا قبلها | 0 |
| syntax | all | tag_initial | خاصية نحوية، الكلمة في بداية الجملة | 0 |
| syntax | all | tag_transparent | البدل | 0 |
| syntax | noun | tag_added | خاصية نحوية، الكلمة مضاف | 0 |
| syntax | all | need | الكلمة تحتاج إلى  كلمة أخرى (المتعدي، العوامل) غير منجزة |  |
| syntax | tool | action | العمل |  |
| syntax | tool | object_type | نوع المعمول، بالنسبة للعامل، مثلا اسم لحرف الجر |  |



