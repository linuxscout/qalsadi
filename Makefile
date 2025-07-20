#/usr/bin/sh
# Build Qalsadi package
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
install:
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
	echo " Test File samples/text.txt"
	echo " Output File output/text3.csv"
	echo " Log File output/text3.txt"
testqrn:
	cut -f2 tests/samples/klm.csv.unknown.csv  >/tmp/klm.txt
	cd tests;python3 test_analex.py -c test_quran -f /tmp/klm.txt -o output/klm.csv > output/klm.txt
teststop:
	cd tests;python3 test_analex.py -f samples/stopwords.txt -o output/stopwords.csv > output/text.txt
	cd tests;grep "unknown" output/stopwords.csv  > output/stopwords.unk.txt
	# Test File samples/stopwords.txt
	# Output File output/stopwords.csv
	# Log File output/text.txt
	# Unkown filter File output/output/stopwords.unk.txt

testone:
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
test73c:LIMIT= 10000
test73c:PROFILER=-m cProfile

test73:LIMIT= 10000
test73:PROFILER=-m pyinstrument
test73 test73c:
	cd tests;python3 $(PROFILER) -o  output/profile.txt test_analex.py -l $(LIMIT) -f samples/text63.txt -o output/text73.csv > output/text73.txt
	echo ""
	wc -w tests/samples/text63.txt
	cp  tests/output/profile.txt  tests/output/profile-$(date).txt
	# use pyinstrument to analyze profile
	tail -n 3 tests/output/text73.txt | sed "s/\[options\]/-r html --show-all/g" | sed "s/pyinstrument/python3 -m pyinstrument/g"

test_unit:
#~ 	cd tests; python3 -m pytest test_unit_lemmatizer.py
#~ 	cd tests; python3 -m pytest test_unit_analex.py
	cd tests; python3 -m pytest test_unit_cache.py
	cd tests; python3 -m pytest test_unit_tagmaker.py
