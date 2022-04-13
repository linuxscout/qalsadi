#/usr/bin/sh
# Build pyArabic package
date=$(shell date +'%y.%m.%d-%H:%M')
default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: 
# Publish to github
publish:
	git push origin master 

md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst
md2html:
	pandoc -s -r markdown -w html README.md -o README.html

wheel:
	sudo python3 setup.py bdist_wheel
wheel3:
	sudo python3 setup.py bdist_wheel
install:
	sudo python3 setup.py install
install3:
	sudo python3 setup.py install
sdist:
	sudo python3 setup.py sdist
upload:
	echo "use twine upload dist/qalsadi.0.3-py2-none-any.whl"

doc:
	epydoc -v --config epydoc.conf
test2:
	cd tests;python3 test_analex.py -f samples/text.txt -o output/text2.csv > output/text2.txt
test3:
	cd tests;python3 test_analex.py -f samples/text.txt -o output/text3.csv > output/text3.txt
testqrn:
	cut -f2 tests/samples/klm.csv.unknown.csv  >/tmp/klm.txt
	cd tests;python3 test_analex.py -c test_quran -f /tmp/klm.txt -o output/klm.csv > output/klm.txt
teststop:
	cd tests;python3 test_analex.py -f samples/stopwords.txt -o output/stopwords.csv > output/text.txt
	cd tests;grep "unknown" output/stopwords.csv  > output/stopwords.unk.txt
testone:
	cd tests;python3 test_analex.py -c test_one -f samples/words.txt -o output/words.csv > output/words.txt
testone3:
	cd tests;python3 test_analex.py -c test_one -f samples/words.txt -o output/words.csv > output/words.txt

test1000:LIMIT= 10
test1000:
	cd tests;python3 -m cProfile -o  output/profile.txt test_analex.py -l ${LIMIT} -f samples/text1000.txt -o output/text1000.csv > output/text1000.txt
	wc -w tests/samples/text1000.txt
	echo "Use cprofilev -f tests/output/profile.txt"

test63:LIMIT= 10000
test63:
	cd tests;python3 -m cProfile -o  output/profile.txt test_analex.py -l $(LIMIT) -f samples/text63.txt -o output/text63.csv > output/text63.txt
	wc -w tests/samples/text63.txt
	cp  tests/output/profile.txt  tests/output/profile-$(date).txt
	echo "Use cprofilev -f tests/output/profile.txt"
