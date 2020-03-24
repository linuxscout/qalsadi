#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  print_debug.py
#  
#  Copyright 2019 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    #~ division,
    )

from builtins import str
from future.utils import python_2_unicode_compatible
import sys


from pyarabic.arabrepr import arepr
def print_md_table(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList:
       colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict:
       #~ myList.append([unicode(item[col] or '') for col in colList])
       myList.append([str(item[col] or '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = u' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList:
       print(formatStr.format(*item).encode('utf8'))
    
def print_table(myDict, colList=None, sep=u"\t"):
    """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
    If column names (colList) aren't specified, they will show in random order.
    Author: Thierry Husson - Use it as you want but don't blame me.
    """
    if not colList:
        colList = list(myDict[0].keys() if myDict else [])
    myList = [colList] # 1st row = header
    for item in myDict:
        row = []
        for col in colList:
            if isinstance(item[col], dict):
                row.append(u";".join(item[col].values()))
            if isinstance(item[col], list):
                row.append(u";".join(item[col]))
            else:
                #~ row.append(unicode(item[col] or ''))
                row.append(str(item[col] or ''))
        myList.append(row)
    for item in myList:
        #~ print(u'\t'.join(item).encode('utf8'))
        if sys.version_info >= (3, 0):
            print(u'\t'.join(item))#.encode('utf8'))
        else:
            print(u'\t'.join(item).encode('utf8'))

def main(args):
    d = [{'enc': u'', 'stem_conj': u'يأمرهم', 'pro': u'', 'prefix': u'', 'verb': u'يأمرهم', 'stem_comp': u'يأمرهم', 'trans_comp': False, 'suffix': u''},
 {'enc': u'', 'stem_conj': u'أمرهم', 'pro': u'', 'prefix': u'ي', 'verb': u'يأمرهم', 'stem_comp': u'يأمرهم', 'trans_comp': False, 'suffix': u''},
 {'enc': u'هم', 'stem_conj': u'أمر', 'pro': u'', 'prefix': u'ي', 'verb': u'يأمرهم', 'stem_comp': u'يأمر', 'trans_comp': True, 'suffix': u''},
 {'enc': u'هم', 'stem_conj': u'يأمر', 'pro': u'', 'prefix': u'', 'verb': u'يأمرهم', 'stem_comp': u'يأمر', 'trans_comp': True, 'suffix': u''}]
    print_table(d)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
