#!/usr/bin/env python
# -*- coding: utf-8 -*-
# "equal" flag : if the flag is False, the actual output is not correct according to the expected 
# result
# used to watch lemmatizer changes 
Lemmas_DataSet = [
{'token': 'هل', 'lemmas': ['هَلْ'], 'wordtype': 'stopword', 'vocalizeds': ['هَل'], 'equal': True} ,
{'token': 'تحتاج', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'إلى', 'lemmas': ['إِلَى'], 'wordtype': 'stopword', 'vocalizeds': ['إِلَى'], 'equal': True} ,
{'token': 'ترجمة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'كي', 'lemmas': ['كَيْ'], 'wordtype': 'stopword', 'vocalizeds': ['كَي'], 'equal': True} ,
{'token': 'تفهم', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'خطاب', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الملك', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '؟', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'اللغة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '"', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الكلاسيكية', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '"(', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الفصحى', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': ')', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'موجودة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'في', 'lemmas': ['فِي'], 'wordtype': 'moststopword', 'vocalizeds': ['فِي'], 'equal': True} ,
{'token': 'كل', 'lemmas': ['كُلُّ', 'كُلَّ'], 'wordtype': 'ambiguous', 'vocalizeds': ['كُلّ'], 'equal': True} ,
{'token': 'اللغات', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'وكذلك', 'lemmas': ['ذَلِكَ', 'كَذَلِكَ'], 'wordtype': 'ambiguous', 'vocalizeds': ['وذَلِك', 'وكَذَلِك'], 'equal': True} ,
{'token': 'اللغة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '"', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الدارجة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '"..', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الفرنسية', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'التي', 'lemmas': ['الَّتِي'], 'wordtype': 'ambiguous', 'vocalizeds': ['الَّتِي'], 'equal': True} ,
{'token': 'ندرس', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'في', 'lemmas': ['فِي'], 'wordtype': 'moststopword', 'vocalizeds': ['فِي'], 'equal': True} ,
{'token': 'المدرسة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'ليست', 'lemmas': ['لَيْسَتْ'], 'wordtype': 'stopword', 'vocalizeds': ['لَيْسَت'], 'equal': True} ,
{'token': 'الفرنسية', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'التي', 'lemmas': ['الَّتِي'], 'wordtype': 'ambiguous', 'vocalizeds': ['الَّتِي'], 'equal': True} ,
{'token': 'يستخدمها', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الناس', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'في', 'lemmas': ['فِي'], 'wordtype': 'moststopword', 'vocalizeds': ['فِي'], 'equal': True} ,
{'token': 'شوارع', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'باريس', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '..', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'وملكة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'بريطانيا', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'لا', 'lemmas': ['لَا'], 'wordtype': 'stopword', 'vocalizeds': ['لَا'], 'equal': True} ,
{'token': 'تخطب', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'بلغة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'شوارع', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'لندن', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '..', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'لكل', 'lemmas': ['كُلُّ', 'كُلَّ'], 'wordtype': 'ambiguous', 'vocalizeds': ['لكُلّ'], 'equal': True} ,
{'token': 'مقام', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'مقال', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,

]