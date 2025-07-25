# Qalsadi Arabic Morphological Analyzer and Lemmatizer for Python

المكتبة البرمجية [القلصادي](https://github.com/linuxscout/qalsadi)  أداة متخصصة في التحليل الصرفي للنصوص العربية. تعتمد على قاعدة بيانات معجمية لتحليل النصوص سواء كانت مشكولة جزئياً أو كلياً. تقدم هذه المكتبة تشكيل الكلمات وتحليلها الصرفي، بالإضافة إلى تقييم درجة شيوع الكلمة في اللغة العربية المعاصرة.

متوفرة للتجربة على موقع [مشكال](http://tahadz.com/mishkal)، قسم  أدوات/تحليل

[Qalsadi](https://github.com/linuxscout/qalsadi) library is a specialized tool for morphological analysis of Arabic texts. It uses a lexical database to analyze fully or partially vocalized texts, providing both morphological analysis and diacritics. Additionally, it evaluates the frequency of word usage in contemporary Arabic and uses the "Qutrub" tool for verb conjugation.

The demo is available on [Mishkal](http://Tahadz.com/mishkal/ >Tools/َAnalysis

  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features  |   value
----------|---------------------------------------------------------------------------------
Authors   | [Authors.md](https://github.com/linuxscout/qalsadi/master/AUTHORS.md)
Release   | {{ release }}
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
>>> # get all lemmas for each word text
>>> lemmas = lemmer.lemmatize_text(text, all=True)
>>> lemmas
[['هل', 'وهل', 'هال'], ['احتاج'], ['إلى'], ['ترجمة'], ['كي'], ['تف', 'أفهم', 'فهم', 'تفهم'], ['خاطب', 'خطاب'], ['مالك', 'ملك'], ['؟'], ['لغة'], ['"'], ['كلاسيكي'], ['"('], ['فصحى'], [')'], ['موجود'], ['في'], ['أكل', 'كال', 'كل', 'وكل'], ['لغة'], ['كذلك', 'ذل'], ['لغة'], ['"'], ['دارج'], ['"..'], ['فرنسة', 'فرنسي'], ['التي'], ['درس'], ['في'], ['مدرس', 'مدرسة'], ['يس', 'ليست', 'لاس', 'ليس'], ['فرنسة', 'فرنسي'], ['التي'], ['استخدم'], ['ناس'], ['في'], ['شارع'], ['باريس'], ['..'], ['مالك', 'ملك', 'ملكة'], ['بريطانيا', 'بريطاني'], ['لا'], ['خطب'], ['بالغ', 'لغة', 'بلغة'], ['شارع'], ['دن', 'دنى', 'دان', 'ناد', 'دنو', 'أدنى', 'أدان', 'دنا', 'ودن'], ['..'], ['كل'], ['مقام'], ['مقالي', 'مقال']]

```

#### Morphology analysis
``` python
import qalsadi.analex as qa

text = "لا يحمل الحقد من تعلو به الرتب"
analyzer = qa.Analex()
result = analyzer.check_text(text)
print(result)
```

## Morphology analysis display

* The morphology generate a lot of fields, to manage dispaly we use the resultFormatter class

  ```python
  import qalsadi.analex as qa
  from qalsadi.resultformatter import ResultFormatter
  
  text = "لا يحمل الحقد من تعلو به الرتب"
  analyzer = qa.Analex()
  results = analyzer.check_text(text)
  formatter = ResultFormatter(result)
  
  # Use main fields display
  formatter.set_used_fields("main")
  print(formatter.as_table())
  
  ```

  * Other table formats:

    ```python
    # other table format
    print(formatter.as_table(tablefmt="github") 
    # tablefmt can  table all values from tabulate libray 
    # "plain" (default), "grid", "pipe" (Markdown), "html", "latex", "tsv"
    ```

    

  * Other display formats:

    ```python
    print(formatter.as_csv())
    print(formatter.as_json())
    print(formatter.as_xml())
    ```

  * Other display file formats saving:

    ```python
    formatter.as_csv("output/results.csv")
    formatter.to_json("output/results.json")
    formatter.to_xml("output/results.xml")
    ```

    

  * Change fields to display:

    ```python
    profile  = "main" # other values: "all" "roots", "lemmas", "inflect"
    formatter.set_used_fields(profile)
    ```

  * Add a customizable fields: 

    * if the given field name is not valid, it's ignored.

    ```python
    profile  = "main" # other values: "roots", "lemmas", "inflect"
    formatter.set_used_fields(profile, additional_fields=["root","INVALID"])
    ```

    





#### Output description:

* The result of morphology analysis is  a list of list of `StemmedWord` objects from `qalsadi.stemmedword` file.

The `StemmedWord` is handled as a `dict`n it contains the following fields:


Category   | Applied on | feature             | example         a |شرح
-----------|------------|---------------------|-------------------|---
affix      | all        | affix_key           | ال--َاتُ-       a |مفتاح الزوائد
affix      | all        | affix               | a                 |الزوائد
input      | all        | word                | البيانات        a |الكلمة المدخلة
input      | all        | unvocalized         | a                 |غير مشكول
original   | noun/verb  | freq                | 694644           a |درجة شيوع الكلمة
original   | all        | original_tags       | (u              a |خصائص الكلمة الأصلية
original   | all        | original            | بَيَانٌ         a |الكلمة الأصلية
original   | all        | root                | بين             a |الجذر
output     | all        | type                | Noun:مصدر       a |نوع الكلمة
output     | all        | semivocalized       | الْبَيَانَات    a |الكلمة مشكولة بدون علامة الإعراب
output     | all        | vocalized           | الْبَيَانَاتُ   a |الكلمة مشكولة
output     | all        | stem                | بيان            a |الجذع
output     | all        | lemma               | بيان        a |الأصل

* For more details about fields in the output, see [DOCS/DataDescription](docs/datadescription.md)

#### Using Cache

Qalsadi can use Cache to speed up the process, there are 4 kinds of cache,

* Memory cache
* Pickle cache
* Pickledb cache
* CodernityDB cache.

To use one of it, you can see the followng examples:
* Using a factory method

```python
>> > import qalsadi.analex
>> > from qalsadi.cachemanager.cache_factory import Cache_Factory
>> > analyzer = qalsadi.analex.Analex()
>> >  # list available cache names
>> > Cache_Factory.list()
['', 'memory', 'pickle', 'pickledb', 'codernity']
>> >  # configure cacher
>> >  # configure path used to store the cache
>> > path = 'cache/qalsasicache.pickledb'
>> > cacher = Cache_Factory.factory("pickledb", path)
>> > analyzer.set_cacher(cacher)
>> >  # to enable the use of cacher
>> > analyzer.enable_allow_cache_use()
```
* Memory cache

```python
>> > import qalsadi.analex
>> > analyzer = qalsadi.analex.Analex()
>> >  # configure cacher
>> > import qalsadi.cachemanager
>> > cacher = qalsadi.cache.cache.Cache()
>> > analyzer.set_cacher(cacher)
>> >  # to enable the use of cacher
>> > analyzer.enable_allow_cache_use()
>> >  # to disable the use of cacher
>> > analyzer.disable_allow_cache_use()
```
* Pickle cache

```python
>> > import qalsadi.analex
>> > from qalsadi.cachemanager.cache_pickle import Cache
>> > analyzer = qalsadi.analex.Analex()
>> >  # configure cacher
>> >  # configure path used to store the cache
>> > path = 'cache/qalsadiCache.pickle'
>> > cacher = Cache(path)
>> > analyzer.set_cacher(cacher)
>> >  # to enable the use of cacher
>> > analyzer.enable_allow_cache_use()

```
* Pickledb cache

```python
>> > import qalsadi.analex
>> > from qalsadi.cachemanager.cache_pickledb import Cache
>> > analyzer = qalsadi.analex.Analex()
>> >  # configure cacher
>> >  # configure path used to store the cache
>> > path = 'cache/qalsadiCache.pickledb'
>> > cacher = Cache(path)
>> > analyzer.set_cacher(cacher)
>> >  # to enable the use of cacher
>> > analyzer.enable_allow_cache_use()

```
* CodernityDB cache

```python
>> > import qalsadi.analex
>> > from qalsadi.cachemanager.cache_codernity import Cache
>> > analyzer = qalsadi.analex.Analex()
>> >  # configure cacher
>> >  # configure path used to store the cache
>> > path = 'cache'
>> > cacher = Cache(path)
>> > analyzer.set_cacher(cacher)
>> >  # to enable the use of cacher
>> > analyzer.enable_allow_cache_use()
```
