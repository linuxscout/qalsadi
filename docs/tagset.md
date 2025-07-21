Description of Arabic tag sets
source : https://github.com/linuxscout/arramooz/blob/master/docs/arabic_tags.txt
=============================
The arabic tag sytax for grammar check is composed of 4 parts

The tag starts by word class
for example 
V: Verb
N: Noun
P: tool or partical

Nouns
======

3 parts:
======
* word class and category
* Conjugation ( suffixes used to conjugate words in dual form, feminin form).
* Affixes ( prefixes and encletics)



Word class and category:
======
 define the attributes of word in dictionary, for example,
contains 2 parts
- Word type:
    N: noun,
    V: verb,
    P: particle
- Word sub class:
    Masdr
    Adj : adjective 
    comparative
    Jamed:
    ...
    -: not defined

Noun conjugation  :
======
    - Gender suffix:
        M: masculine ( ون is a mark of masculine)
        F: feminine (ة or ات)
        -: none
    - Number suffix:
        1: single
        2: dual
        3: plural ( regular masculine or feminine plural, or irregular plural)
        3I: irregular plural form
    - Case ( إعراب)
        U: marfou3
        I: Majzoum/ Majrour
        A: Mansoub
        B: Mabni
        -: not specified
Noun prefixes and encletic :
=============
contains 3 parts
W: conjonction: starts by WAW or FEH, take 3 values: W: for waw, F; for Feh, -: none.
B: preposition: B: for Beh, K: for Kaf, L: for Lam, by default we use B, -: none.
L: definite article, L: for AL,  -: none.

Ecletic
======
define the extended words added to the lexem: الضمائر المضافة
    H: if have encletic


example:

Inflected form|origin| Tag
------------------|--------|-----
بواحدي |واحد|N.adj.;M1-;-B--
بواحديي|واحد||N.adj.;M2-;-B-H
الواحدة|واحد||N.adj.;F1-;--L-
واحداك|واحد|N.adj.;M2U;---H
بواحدين|واحد|N.adj.;M2A;-B--
بواحديتي|واحد|N.adj.;F1-;-B-H
الواحدات|واحد|N.adj.;M3-;--L-
واحدتي|واحد|N.adj.;F1-;---H
بالواحدية|واحد|N.adj.;F1-;-BL-
الواحديتان|واحد|N.adj.;M2-;--L-
الواحدتان|واحد|N.adj.;M2-;--L-
بواحدياتك|واحد|N.adj.;M3-;-B-H
واحدات|واحد|N.adj.;M3-;----
واحدين|واحد|N.adj.;M2A;----
بواحداتك|واحد|N.adj.;M3-;-B-H
واحدي|واحد|N.adj.;M1-;----Verbs


Word class + conjugation + affixes 

verb Word class  :
=============
    Word type: V
    verb class:
        W: weak verb
            1/2/3: weak letter position (1: Mithal, 2 Adjwaf, 3 Naqis)
            Y/W: origin of weak letter Waw or YEH
        Dbl: doubled مضعّف

    transitivity: 
        T: transitivity/ commun, 
        I: intransitivity
    length: verb length 
    3-6: indicate length

verb conjugation  :
=============
    tense:
        P: past
        F: present
        I:  Imperative
    voice:
        P: passive
        A: active
    case:
        R: marfou3
        J: Majzoum
        N: Mansoub
        B: Mabni
        C: Confirmed
    Ponoun:
        Person: 
            I: 1st person
            Y: 2nd person
            H: 3rd person
        gender: 
            M/F
        Number: 1/2/3
Affixes ( Procletic + Ecletic)
======
Verb procletic :
=============
    W: conjonction: starts by WAW or FEH, take 3 values: W: for waw, F; for Feh, -: none.
    S: future prefix, س+يتعلم
Verb encletic :
=============
define the extended words added to the lexem: الضمائر المضافة
    H: if have encletic
