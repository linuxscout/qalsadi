#!/usr/bin/env python
# -*- coding: utf-8 -*-
# "equal" flag : if the flag is False, the actual output is not correct according to the expected 
# result
# used to watch lemmatizer changes 
Lemmas_DataSet = [
{'token': 'هل', 'lemmas': ['هَلَّ', 'وَهَلَ', 'هَالَ'], 'wordtype': 'verb', 'vocalizeds': ['هَلَّ', 'هِلْ'], 'equal': True} ,
{'token': 'تحتاج', 'lemmas': ['اِحْتَاجَ'], 'wordtype': 'verb', 'vocalizeds': ['تَحْتَاجَ', 'تَحْتَاجُ'], 'equal': True} ,
{'token': 'إلى', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'ترجمة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'كي', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'تفهم', 'lemmas': ['أَفْهَمَ', 'تَفَهَّمَ', 'فَهَّمَ', 'فَهِمَ'], 'wordtype': 'verb', 'vocalizeds': ['تَفَهَّمَ', 'تَفَهَّمْ', 'تَفْهَمَ', 'تَفْهَمُ', 'تَفْهَمْ', 'تُفَهَّمَ', 'تُفَهَّمُ', 'تُفَهَّمْ', 'تُفَهِّمَ', 'تُفَهِّمُ', 'تُفَهِّمْ', 'تُفُهِّمَ', 'تُفْهَمَ', 'تُفْهَمُ', 'تُفْهَمْ', 'تُفْهِمَ', 'تُفْهِمُ', 'تُفْهِمْ'], 'equal': True} ,
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
{'token': 'في', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'كل', 'lemmas': ['أَكَلَ', 'وَكَلَ', 'كَلَّ', 'كَالَ'], 'wordtype': 'verb', 'vocalizeds': ['كَلَّ', 'كُلْ', 'كِلْ'], 'equal': True} ,
{'token': 'اللغات', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'وكذلك', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'اللغة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '"', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الدارجة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '"..', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'الفرنسية', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'التي', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'ندرس', 'lemmas': ['دَرُسَ', 'دَرَسَ', 'دَرَّسَ'], 'wordtype': 'verb', 'vocalizeds': ['نَدْرُسَ', 'نَدْرُسُ', 'نَدْرُسْ', 'نَدْرِسَ', 'نَدْرِسُ', 'نَدْرِسْ', 'نُدَرَّسَ', 'نُدَرَّسُ', 'نُدَرَّسْ', 'نُدَرِّسَ', 'نُدَرِّسُ', 'نُدَرِّسْ', 'نُدْرَسَ', 'نُدْرَسُ', 'نُدْرَسْ'], 'equal': True} ,
{'token': 'في', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'المدرسة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'ليست', 'lemmas': ['لَيْسَ', 'لَاسَ', 'لَيِسَ', 'يَسَّ'], 'wordtype': 'verb', 'vocalizeds': ['لَيَسَّتْ', 'لَيِسَتْ', 'لَيِسْتَ', 'لَيِسْتُ', 'لَيِسْتِ', 'لِيسَتْ', 'لِيَسَّتْ'], 'equal': True} ,
{'token': 'الفرنسية', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'التي', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'يستخدمها', 'lemmas': ['اِسْتَخْدَمَ'], 'wordtype': 'verb', 'vocalizeds': ['يَسْتَخْدِمَهَا', 'يَسْتَخْدِمُهَا', 'يَسْتَخْدِمْهَا'], 'equal': True} ,
{'token': 'الناس', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'في', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'شوارع', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'باريس', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': '..', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'وملكة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'بريطانيا', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'لا', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'تخطب', 'lemmas': ['خَطُبَ', 'خَطَبَ', 'خَطِبَ'], 'wordtype': 'verb', 'vocalizeds': ['تَخْطَبَ', 'تَخْطَبُ', 'تَخْطَبْ', 'تَخْطُبَ', 'تَخْطُبُ', 'تَخْطُبْ', 'تُخْطَبَ', 'تُخْطَبُ', 'تُخْطَبْ'], 'equal': True} ,
{'token': 'بلغة', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'شوارع', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'لندن', 'lemmas': ['دَنَّ', 'أَدَانَ', 'وَدَنَ', 'دَنَا', 'دَانَ', 'دَنُوَ', 'أَدْنَى', 'نَادَ', 'دَنَّى'], 'wordtype': 'verb', 'vocalizeds': ['لَنَدُنْ', 'لَنَدِنَ', 'لَنَدِنُ', 'لَنَدِنَّ', 'لَنَدِنُّ', 'لَنَدِنْ', 'لَنَدْنُ', 'لَنُدَنَّ', 'لَنُدَنِّ', 'لَنُدَنْ', 'لَنُدِنْ', 'لَنُدْنَ', 'لَنُدْنِ', 'لِنَدُنْ', 'لِنَدِنَ', 'لِنَدِنُ', 'لِنَدِنَّ', 'لِنَدِنُّ', 'لِنَدِنْ', 'لِنَدْنُ', 'لِنُدَنَّ', 'لِنُدَنِّ', 'لِنُدَنْ', 'لِنُدِنْ', 'لِنُدْنَ', 'لِنُدْنِ'], 'equal': True} ,
{'token': '..', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'لكل', 'lemmas': ['كَلَّ'], 'wordtype': 'verb', 'vocalizeds': ['لَكَلَّ', 'لِكَلَّ'], 'equal': True} ,
{'token': 'مقام', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,
{'token': 'مقال', 'lemmas': [], 'wordtype': 'ambiguous', 'vocalizeds': [], 'equal': True} ,

]
