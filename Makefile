#/usr/bin/sh
# Build pyArabic package

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
	sudo python setup.py bdist_wheel
wheel3:
	sudo python3 setup.py bdist_wheel
install:
	sudo python setup.py install
install3:
	sudo python3 setup.py install
sdist:
	sudo python setup.py sdist
upload:
	echo "use twine upload dist/Tashaphyne-0.3-py2-none-any.whl"

doc:
	epydoc -v --config epydoc.conf
test:
	cd tests;python test_analex.py -f samples/text.txt -o output/text.csv > output/text.txt
testqrn:
	cut -f2 tests/samples/klm.csv.unknown.csv  >/tmp/klm.txt
	cd tests;python test_analex.py -c test_quran -f /tmp/klm.txt -o output/klm.csv > output/klm.txt
teststop:
	cd tests;python test_analex.py -f samples/stopwords.txt -o output/stopwords.csv > output/text.txt
	cd tests;grep "unknown" output/stopwords.csv  > output/stopwords.unk.txt
testone:
	cd tests;python test_analex.py -c test_one -f samples/words.txt -o output/words.csv > output/words.txt

