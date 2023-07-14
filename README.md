# Qalsadi Arabic Morphological Analyzer and Lemmatizer for Python



  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features  |   value
----------|---------------------------------------------------------------------------------
Authors   | [Authors.md](https://github.com/linuxscout/qalsadi/master/AUTHORS.md)
Release   | 0.4.6
License   |[GPL](https://github.com/linuxscout/qalsadi/master/LICENSE)
Tracker   |[linuxscout/qalsadi/Issues](https://github.com/linuxscout/qalsadi/issues)
Website   |[https://pypi.python.org/pypi/qalsadi](https://pypi.python.org/pypi/qalsadi)
Doc       |[package Documentaion](https://qalsadi.readthedocs.io/)
Source    |[Github](http://github.com/linuxscout/qalsadi)
Download  |[sourceforge](http://qalsadi.sourceforge.net)
Feedbacks |[Comments](http://tahadz.com/qalsadi/contact)
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
 - give word frequency in Arabic modern use.

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

## Usage
### Demo
The demo is available on [Tahadz.com](http://tahadz.com/mishkal) >Tools/َAnalysis قسم أدوات - تحليل
### Example 
#### Lemmatization
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

>>> lemmas = lemmer.lemmatize_text(text)
>>> print(lemmas)
['هل', 'احتاج', 'إلى', 'ترجمة', 'كي', 'تفهم', 'خطاب', 'ملك', '؟', 'لغة', '"', 'كلاسيكي', '"(', 'فصحى', ')', 'موجود', 'في', 'كل', 'لغة', 'ذلك', 'لغة', '"', 'دارج', '"..', 'فرنسي', 'التي', 'درس', 'في', 'مدرسة', 'ليست', 'فرنسي', 'التي', 'استخدم', 'ناس', 'في', 'شوارع', 'باريس', '..', 'ملك', 'بريطانيا', 'لا', 'خطب', 'بلغة', 'شوارع', 'دنو', '..', 'كل', 'مقام', 'مقالي']
>>> # lemmatize a text and return lemma pos
... lemmas = lemmer.lemmatize_text(text, return_pos=True)
>>> print(lemmas)
[('هل', 'stopword'), ('احتاج', 'verb'), ('إلى', 'stopword'), ('ترجمة', 'noun'), ('كي', 'stopword'), ('تفهم', 'noun'), ('خطاب', 'noun'), ('ملك', 'noun'), '؟', ('لغة', 'noun'), '"', ('كلاسيكي', 'noun'), '"(', ('فصحى', 'noun'), ')', ('موجود', 'noun'), ('في', 'stopword'), ('كل', 'stopword'), ('لغة', 'noun'), ('ذلك', 'stopword'), ('لغة', 'noun'), '"', ('دارج', 'noun'), '"..', ('فرنسي', 'noun'), ('التي', 'stopword'), ('درس', 'verb'), ('في', 'stopword'), ('مدرسة', 'noun'), ('ليست', 'stopword'), ('فرنسي', 'noun'), ('التي', 'stopword'), ('استخدم', 'verb'), ('ناس', 'noun'), ('في', 'stopword'), ('شوارع', 'noun'), ('باريس', 'all'), '..', ('ملك', 'noun'), ('بريطانيا', 'noun'), ('لا', 'stopword'), ('خطب', 'verb'), ('بلغة', 'noun'), ('شوارع', 'noun'), ('دنو', 'verb'), '..', ('كل', 'stopword'), ('مقام', 'noun'), ('مقالي', 'noun')]

>>> # Get vocalized output lemmas
>>> lemmer.set_vocalized_lemma()
>>> lemmas = lemmer.lemmatize_text(text)
>>> print(lemmas)
['هَلْ', 'اِحْتَاجَ', 'إِلَى', 'تَرْجَمَةٌ', 'كَيْ', 'تَفَهُّمٌ', 'خَطَّابٌ', 'مَلَكٌ', '؟', 'لُغَةٌ', '"', 'كِلاَسِيكِيٌّ', '"(', 'فُصْحَى', ')', 'مَوْجُودٌ', 'فِي', 'كُلَّ', 'لُغَةٌ', 'ذَلِكَ', 'لُغَةٌ', '"', 'دَارِجٌ', '"..', 'فَرَنْسِيّ', 'الَّتِي', 'دَرَسَ', 'فِي', 'مَدْرَسَةٌ', 'لَيْسَتْ', 'فَرَنْسِيّ', 'الَّتِي', 'اِسْتَخْدَمَ', 'نَاسٌ', 'فِي', 'شَوَارِعٌ', 'باريس', '..', 'مَلَكٌ', 'برِيطانِيا', 'لَا', 'خَطَبَ', 'بَلَغَةٌ', 'شَوَارِعٌ', 'أَدَانَ', '..', 'كُلَّ', 'مَقَامٌ', 'مَقَالٌ']
>>> 
```

#### Morphology analysis
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



#### Output description
Category   | Applied on | feature              | example         a|شرح
-----------|------------|----------------------|------------------|---
affix      | all        | affix_key            | ال--َاتُ-       a|مفتاح الزوائد
affix      | all        | affix                |                 a|الزوائد
input      | all        | word                 | البيانات        a|الكلمة المدخلة
input      | all        | unvocalized          |                 a|غير مشكول
morphology | noun       | tag_mamnou3          |0                a|ممنوع من الصرف
morphology | verb       | tag_confirmed        |0                a|خاصية الفعل المؤكد
morphology | verb       | tag_mood             |0                a|حالة الفعل المضارع (منصوب، مجزوم، مرفوع)
morphology | verb       | tag_pronoun          |0                a|الضمير
morphology | verb       | tag_transitive       |0                a|التعدي اللزوم
morphology | verb       | tag_voice            |0                a|البناء للمعلوم/ البناء للمجهول
morphology | noun       | tag_regular          |1                a|قياسي/ سماعي
morphology | noun/verb  | tag_gender           |3                a|النوع ( مؤنث مذكر)
morphology | verb       | tag_person           |4                a|الشخص (المتكلم الغائب المخاطب)
morphology | noun       | tag_number           |21               a|العدد(فرد/مثنى/جمع)
original   | noun/verb  | freq                 |694644           a|درجة شيوع الكلمة
original   | all        | original_tags        | (u              a|خصائص الكلمة الأصلية
original   | all        | original             | بَيَانٌ         a|الكلمة الأصلية
original   | all        | root                 | بين             a|الجذر
original   | all        | tag_original_gender  | مذكر            a|جنس الكلمة الأصلية
original   | noun       | tag_original_number  | مفرد            a|عدد الكلمة الأصلية
output     | all        | type                 | Noun:مصدر       a|نوع الكلمة
output     | all        | semivocalized        | الْبَيَانَات    a|الكلمة مشكولة بدون علامة الإعراب
output     | all        | vocalized            | الْبَيَانَاتُ   a|الكلمةمشكولة
output     | all        | stem                 | بيان            a|الجذع
syntax     | all        | tag_break            |0                a|الكلمة منفصلة عمّا قبلها
syntax     | all        | tag_initial          |0                a|خاصية نحوية، الكلمة في بداية الجملة
syntax     | all        | tag_transparent      |0                a|البدل
syntax     | noun       | tag_added            |0                a|خاصية نحوية، الكلمة مضاف
syntax     | all        | need                 |                 a|الكلمة تحتاج إلى كلمة أخرى (المتعدي، العوامل) غير منجزة
syntax     | tool       | action               |                 a|العمل
syntax     | tool       | object_type          |                 a|نوع المعمول، بالنسبة للعامل، مثلا اسم لحرف الجر

#### Unsing Cache
Qalsadi can use Cache to speed up the process, there are 4 kinds of cache,

* Memory cache
* Pickle cache
* Pickledb cache
* CodernityDB cache.

To use one of it, you can see the followng examples:
* Using a factory method
```python
>>> import qalsadi.analex
>>> from qalsadi.cache_factory import Cache_Factory
>>> analyzer = qalsadi.analex.Analex()
>>> # list available cache names
>>> Cache_Factory.list()
['', 'memory', 'pickle', 'pickledb', 'codernity']
>>> # configure cacher
>>> # configure path used to store the cache
>>> path = 'cache/qalsasicache.pickledb'
>>> cacher = Cache_Factory.factory("pickledb", path)
>>> analyzer.set_cacher(cacher)
>>> # to enable the use of cacher
>>> analyzer.enable_allow_cache_use()
```
* Memory cache

```python
>>> import qalsadi.analex
>>> analyzer = qalsadi.analex.Analex()
>>> # configure cacher
>>> import qalsadi.cache
>>> cacher = qalsadi.cache.Cache()
>>> analyzer.set_cacher(cacher)
>>> # to enable the use of cacher
>>> analyzer.enable_allow_cache_use()
>>> # to disable the use of cacher
>>> analyzer.disable_allow_cache_use()
```
* Pickle cache

```python
>>> import qalsadi.analex
>>> from qalsadi.cache_pickle import Cache
>>> analyzer = qalsadi.analex.Analex()
>>> # configure cacher
>>> # configure path used to store the cache
>>> path = 'cache/qalsadiCache.pickle'
>>> cacher = Cache(path)
>>> analyzer.set_cacher(cacher)
>>> # to enable the use of cacher
>>> analyzer.enable_allow_cache_use()

```
* Pickledb cache

```python
>>> import qalsadi.analex
>>> from qalsadi.cache_pickledb import Cache
>>> analyzer = qalsadi.analex.Analex()
>>> # configure cacher
>>> # configure path used to store the cache
>>> path = 'cache/qalsadiCache.pickledb'
>>> cacher = Cache(path)
>>> analyzer.set_cacher(cacher)
>>> # to enable the use of cacher
>>> analyzer.enable_allow_cache_use()

```
* CodernityDB cache


```python
>>> import qalsadi.analex
>>> from qalsadi.cache_codernity import Cache
>>> analyzer = qalsadi.analex.Analex()
>>> # configure cacher
>>> # configure path used to store the cache
>>> path = 'cache'
>>> cacher = Cache(path)
>>> analyzer.set_cacher(cacher)
>>> # to enable the use of cacher
>>> analyzer.enable_allow_cache_use()
```