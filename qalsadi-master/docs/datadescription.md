# Data Description
## Morphology results description
* The result of morphology analysis is  a list of list of `StemmedWord` objects from `qalsadi.stemmedword` file.

The `StemmedWord` is handled as a `dict`n it contains the following fields:



Category   | Applied on | feature             | example         a |شرح
-----------|------------|---------------------|-------------------|---
affix      | all        | affix_key           | ال--َاتُ-       a |مفتاح الزوائد
affix      | all        | affix               | a                 |الزوائد
input      | all        | word                | البيانات        a |الكلمة المدخلة
input      | all        | unvocalized         | a                 |غير مشكول
morphology | noun       | tag_mamnou3         | 0                a |ممنوع من الصرف
morphology | verb       | tag_confirmed       | 0                a |خاصية الفعل المؤكد
morphology | verb       | tag_mood            | 0                a |حالة الفعل المضارع (منصوب، مجزوم، مرفوع)
morphology | verb       | tag_pronoun         | 0                a |الضمير
morphology | verb       | tag_transitive      | 0                a |التعدي اللزوم
morphology | verb       | tag_voice           | 0                a |البناء للمعلوم/ البناء للمجهول
morphology | noun       | tag_regular         | 1                a |قياسي/ سماعي
morphology | noun/verb  | tag_gender          | 3                a |النوع ( مؤنث مذكر)
morphology | verb       | tag_person          | 4                a |الشخص (المتكلم الغائب المخاطب)
morphology | noun       | tag_number          | 21               a |العدد(فرد/مثنى/جمع)
original   | noun/verb  | freq                | 694644           a |درجة شيوع الكلمة
original   | all        | original_tags       | (u              a |خصائص الكلمة الأصلية
original   | all        | original            | بَيَانٌ         a |الكلمة الأصلية
original   | all        | root                | بين             a |الجذر
original   | all        | tag_original_gender | مذكر            a |جنس الكلمة الأصلية
original   | noun       | tag_original_number | مفرد            a |عدد الكلمة الأصلية
output     | all        | type                | Noun:مصدر       a |نوع الكلمة
output     | all        | semivocalized       | الْبَيَانَات    a |الكلمة مشكولة بدون علامة الإعراب
output     | all        | vocalized           | الْبَيَانَاتُ   a |الكلمة مشكولة
output     | all        | stem                | بيان            a |الجذع
output     | all        | lemma               | بيان        a |الأصل
syntax     | all        | tag_break           | 0                a |الكلمة منفصلة عمّا قبلها
syntax     | all        | tag_initial         | 0                a |خاصية نحوية، الكلمة في بداية الجملة
syntax     | all        | tag_transparent     | 0                a |البدل
syntax     | noun       | tag_added           | 0                a |خاصية نحوية، الكلمة مضاف
syntax     | all        | need                | a                 |الكلمة تحتاج إلى كلمة أخرى (المتعدي، العوامل) غير منجزة
syntax     | tool       | action              | a                 |العمل
syntax     | tool       | object_type         | a                 |نوع المعمول، بالنسبة للعامل، مثلا اسم لحرف الجر
