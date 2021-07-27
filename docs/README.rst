Qalsadi Arabic Morphological Analyzer and Lemmatizer for Python
===============================================================

Developpers: Taha Zerrouki: http://tahadz.com taha dot zerrouki at gmail
dot com

+------+---------------------------------------------------------------+
| Feat | value                                                         |
| ures |                                                               |
+======+===============================================================+
| Auth | `Authors.md <https://github.com/linuxscout/qalsadi/master/AUT |
| ors  | HORS.md>`__                                                   |
+------+---------------------------------------------------------------+
| Rele | 0.4.4                                                         |
| ase  |                                                               |
+------+---------------------------------------------------------------+
| Lice | `GPL <https://github.com/linuxscout/qalsadi/master/LICENSE>`_ |
| nse  | _                                                             |
+------+---------------------------------------------------------------+
| Trac | `linuxscout/qalsadi/Issues <https://github.com/linuxscout/qal |
| ker  | sadi/issues>`__                                               |
+------+---------------------------------------------------------------+
| Webs | https://pypi.python.org/pypi/qalsadi                          |
| ite  |                                                               |
+------+---------------------------------------------------------------+
| Doc  | `package Documentaion <https://qalsadi.readthedocs.io/>`__    |
+------+---------------------------------------------------------------+
| Sour | `Github <http://github.com/linuxscout/qalsadi>`__             |
| ce   |                                                               |
+------+---------------------------------------------------------------+
| Down | `sourceforge <http://qalsadi.sourceforge.net>`__              |
| load |                                                               |
+------+---------------------------------------------------------------+
| Feed | `Comments <http://tahadz.com/qalsadi/contact>`__              |
| back |                                                               |
| s    |                                                               |
+------+---------------------------------------------------------------+
| Acco | [@Twitter](https://twitter.com/linuxscout)                    |
| unts | [@Sourceforge](http://sourceforge.net/projects/qalsadi/)      |
+------+---------------------------------------------------------------+

Citation
--------

If you would cite it in academic work, can you use this citation

::

   T. Zerrouki‏, Qalsadi, Arabic mophological analyzer Library for python.,  https://pypi.python.org/pypi/qalsadi/

Another Citation:

::

   Zerrouki, Taha. "Towards An Open Platform For Arabic Language Processing." (2020).

or in bibtex format

\```bibtex @misc{zerrouki2012qalsadi, title={qalsadi, Arabic
mophological analyzer Library for python.}, author={Zerrouki, Taha},
url={https://pypi.python.org/pypi/qalsadi}, year={2012} }

.. code:: bibtex

   @thesis{zerrouki2020towards,
     title={Towards An Open Platform For Arabic Language Processing},
     author={Zerrouki, Taha},
     year={2020}
   }

Features مزايا
--------------

-  Lemmatization
-  Vocalized Text Analyzer,
-  Use Qutrub library to analyze verbs.
-  give word frequency in arabic modern use.

Applications
~~~~~~~~~~~~

-  Stemming texts
-  Text Classification and categorization
-  Sentiment Analysis
-  Named Entities Recognition

Installation
~~~~~~~~~~~~

::

   pip install qalsadi

Requirements
^^^^^^^^^^^^

::

   pip install -r requirements.txt 

-  libQutrub: Qutrub verb conjugation library:
   http://pypi.pyton/LibQutrub
-  PyArabic: Arabic language tools library : http://pypi.pyton/pyarabic
-  Tashaphyne;Arabic Light Stemmer library :
   http://pypi.python.org/pypi/Tashaphyne/
-  Naftawayh : Arabic words tagger: :
   http://pypi.python.org/pypi/Naftawayh/
-  Arramooz-pysqlite : Arabic dictionary
-  CodernityDB : No Sql native python database

Usage
-----

Example
~~~~~~~

-  Lemmatization

.. code:: python

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

-  Morphology analysis

.. code:: python

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

