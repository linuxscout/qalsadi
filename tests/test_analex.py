import sys
sys.path.append("../")
sys.path.append("../support")
from qalsadi.analex import *


filename="samples/text.txt"

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
analyzer=Analex()
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
