CREATE TABLE nouns (
  id int(11) NOT NULL UNIQUE,
  vocalized varchar(30) DEFAULT NULL,
  unvocalized varchar(30) DEFAULT NULL,
  wordtype varchar(30) DEFAULT NULL,
  root varchar(30) DEFAULT NULL,
  normalized varchar(30) NOT NULL,
  stamped varchar(30) NOT NULL,
  original varchar(30) DEFAULT NULL,
  mankous varchar(30) DEFAULT NULL,
  feminable varchar(30) DEFAULT NULL,
  number varchar(30) DEFAULT NULL,
  dualable varchar(30) DEFAULT NULL,
  masculin_plural varchar(30) DEFAULT NULL,
  feminin_plural varchar(30) DEFAULT NULL,
  broken_plural varchar(30) DEFAULT NULL,
  mamnou3_sarf varchar(30) DEFAULT NULL,
  relative varchar(30) DEFAULT NULL,
  w_suffix varchar(30) DEFAULT NULL,
  hm_suffix varchar(30) DEFAULT NULL,
  kal_prefix varchar(30) DEFAULT NULL,
  ha_suffix varchar(30) DEFAULT NULL,
  k_suffix varchar(30) DEFAULT NULL,
  annex varchar(30) DEFAULT NULL,
  definition text,
  note text
);

INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(1, 'أَبُو', 'أبو', 'اسم', 'أبب', 'ابو', 'اب', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', 'ـو', 'هم', 'كال', 'ها', 'k', 'Cv', '"أَبُو-أَبُو [أ ب ب]. (اسم). 1. ""هَذَا أَبُوكَ"" : وَالِدُكَ. مِنْ الأَسْمَاءِ الخَمْسَةِ."', ':الأسماء الخمسة');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(2, 'أَخُو', 'أخو', 'اسم', 'أخو', 'اخو', 'اخ', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', 'ـو', 'هم', 'كال', 'ها', 'k', 'Cv', '"أَخُو-أَخُو [أ خ و]. (اسم). 1. ""جَاءَ أَخُوكَ"" : مِنْ الأَسْمَاءِ الخَمْسَةِ."', ':الأسماء الخمسة');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(3,'حَمُو', 'حمو', 'اسم', 'حمو', 'حمو', 'حم', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', 'ـو', 'هم', 'كال', 'ها', 'k', 'Cv', '"حَمُو-حَمُو [ح م و]. (اسم). 1. ""هَذَا حَمُوكَ"" : أبو الزَّوْجِ أَو الزَّوْجَةِ، مِنْ الأَسْمَاءِ الخَمْسَةِ."', ':الأسماء الخمسة');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(4, 'فُوو', 'فو', 'اسم', 'فوه', 'فوه', 'ف', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', 'ـو', 'هم', 'كال', 'ها', 'k', 'Cv', '"فُو-فُو [ف و ه]. (اسم). 1. ""هَذَا فُوكَ"" : فَمُكَ، مِنْ الأَسْمَاءِ الخَمْسَةِ."', ':الأسماء الخمسة');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(5, 'ذُو', 'ذو', 'اسم', 'ذوي', 'ذو', 'ذ', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', 'ـو', 'هم', 'كال', 'ها', 'k', 'Cv', '"ذُو-ذُو [ذ و ي]. (اسم). 1. ""جَاءَ ذُو مَالٍ"" : صَاحِبُ مَالٍ، مِنْ الأَسْمَاءِ الخَمْسَةِ."', ':الأسماء الخمسة');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(6, 'أَنْتَ', 'أنت', 'اسم', 'أنت', 'انت', 'انت', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"أَنْتَ [أ ن ت]. (ضمير). ضمير منفصل للمخاطب المذكر المفرد."', ':ضمائر المخاطب');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(7, 'أَنْتِ', 'أنت', 'اسم', 'أنت', 'انت', 'انت', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"أَنْتِ [أ ن ت]. (ضمير). ضمير منفصل للمخاطبة المؤنثة المفردة."', ':ضمائر المخاطب');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(8, 'أَنْتُمَا', 'أنتما', 'اسم', 'أنت', 'انتما', 'انت', '', '', '', 'مثنى', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"أَنْتُمَا [أ ن ت]. (ضمير). ضمير منفصل للمثنى بنوعيه (المذكر والمؤنث المخاطب)."', ':ضمائر المخاطب');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(9, 'أَنْتُمْ', 'أنتم', 'اسم', 'أنت', 'انتم', 'انت', '', '', '', 'جمع', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"أَنْتُمْ [أ ن ت]. (ضمير). ضمير منفصل لجمع المذكر المخاطب."', ':ضمائر المخاطب');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(10, 'هُوَ', 'هو', 'اسم', 'هو', 'هو', 'هو', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"هُوَ [ه و]. (ضمير). ضمير منفصل للغائب المذكر المفرد."', ':ضمائر الغائب');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(11, 'هِيَ', 'هي', 'اسم', 'هي', 'هي', 'هي', '', '', '', 'مفرد', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"هِيَ [ه ي]. (ضمير). ضمير منفصل للغائبة المؤنثة المفردة."', ':ضمائر الغائب');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(12, 'هُمَا', 'هما', 'اسم', 'هم', 'هما', 'هم', '', '', '', 'مثنى', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"هُمَا [ه م]. (ضمير). ضمير منفصل للمثنى بنوعيه (المذكر والمؤنث الغائب)."', ':ضمائر الغائب');
INSERT INTO nouns (id, vocalized, unvocalized, wordtype, root, normalized, stamped, original, mankous, feminable, number, dualable, masculin_plural, feminin_plural, broken_plural, mamnou3_sarf, relative, w_suffix, hm_suffix, kal_prefix, ha_suffix, k_suffix, annex, definition, note) VALUES(13, 'هُمْ', 'هم', 'اسم', 'هم', 'هم', 'هم', '', '', '', 'جمع', 'DnT', '', '', '', '', '', '', '', '', '', '', '', '"هُمْ [ه م]. (ضمير). ضمير منفصل لجمع المذكر الغائب."', ':ضمائر الغائب');