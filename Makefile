# Makefile for building and testing the Qalsadi package

DATE := $(shell date +'%y.%m.%d-%H:%M')
LIMIT ?= 100
PROFILER ?= -m cProfile
PY := python3

.PHONY: all clean backup publish \
        md2rst md2html wheel install sdist upload \
        doc testcase archive_profile test_all \
        test2 testqrn teststop testone \
        test1000 test63 test73 test73c \
        test_unit dev unittest eval eval_all\
        clean_cache changelog \
        run run-json run-csv run-lemmas run-from-file run-stdin run-html \
        run-lemmatize run-analyze

# Default target
default: all

# Clean build artifacts
clean:
	rm -rf build dist *.egg-info
# Clean cache
clean_cache:
	rm -rf tests/cache/*
	rm -rf qalsadi/.qalsadiCache

# Backup target (optional)
backup:
	@echo "Backup logic goes here"

# Build all outputs
all: md2rst md2html wheel sdist

# Publish code to GitHub
publish:
	git push origin master

# Convert Markdown to reStructuredText
md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst

# Convert Markdown to HTML
md2html:
	pandoc -s -r markdown -w html README.md -o README.html

# Build wheel
wheel:
	$(PY) -m build --wheel

# Install package
install:
	$(PY) setup.py install

# Build source distribution
sdist:
	$(PY) setup.py sdist

# Upload instructions
upload:
	@echo "Use: twine upload dist/<package>.whl"

# Build documentation
doc:
	cd docs; make html
changelog:CHANGFILE=docs/CHANGELOG.md
changelog:
	# detailed changelog
	git log --pretty=format:"* %ad %h - %s (%an)" --date=short >docs/ChangeLog
	@echo "# Changelog" > $(CHANGFILE)
	@echo "" >>  $(CHANGFILE)
	@git tag --sort=-creatordate | while read tag; do \
		echo "## $$tag - $$(git log -1 --format=%ad --date=short $$tag)" >>  $(CHANGFILE); \
		git log "$$tag^".."$$tag" --pretty="* %s" --no-merges >>  $(CHANGFILE); \
		echo "" >>  $(CHANGFILE); \
	done
	@echo " $(CHANGFILE) generated from Git tags."

# Run generic test case
LOG := $(basename $(DATA_FILE)).log
OUT := $(basename $(DATA_FILE)).csv

testcase:clean_cache
	cd tests && PYTHONPATH=.. $(PY) $(PROFILER) $(PROFILE_OUT) test_analex.py $(TEST_MODE) -l $(LIMIT) -f samples/$(DATA_FILE) -o output/$(OUT) > output/$(LOG)
	wc -w tests/samples/$(DATA_FILE)
	@echo "Test File: samples/$(DATA_FILE)"
	@echo "Output CSV: output/$(OUT)"
	@echo "Log File: output/$(LOG)"

# Archive profiling info
archive_profile:
	@echo "Profile file: output/profile.txt"
ifeq ($(PROFILER),-m pyinstrument)
	@echo "Use pyinstrument to analyze profile"
	tail -n 3 tests/output/$(LOG) | sed "s/\[options\]/-r html --show-all/g" | sed "s/pyinstrument/$(PY) -m pyinstrument/g"
else
	@echo "Use: cprofilev -f output/profile.txt"
endif
	cp tests/output/profile.txt tests/output/profile-$(DATE).txt

# Specific test configurations
test2: DATA_FILE=text.txt
test2: testcase

testqrn:
	cut -f2 tests/samples/klm.csv.unknown.csv > tests/samples/quran_klm.txt
	$(MAKE) testcase DATA_FILE=quran_klm.txt TEST_MODE=-c\ test_quran

teststop: DATA_FILE=stopwords.txt
teststop: testcase
#	cd tests && grep "unknown" output/$(OUT) > output/$(basename $(DATA_FILE)).unk.txt

testone: DATA_FILE=words.txt
testone: TEST_MODE=-c\ test_one
testone: testcase

test1000: DATA_FILE=text1000.txt
test1000: PROFILER=-m cProfile
test1000: PROFILE_OUT=-o output/profile.txt
test1000: testcase archive_profile

test63: DATA_FILE=text63.txt
test63: PROFILER=-m cProfile
test63: PROFILE_OUT=-o output/profile.txt
test63: testcase archive_profile

test73 test73c: DATA_FILE=text63.txt
test73: PROFILER=-m pyinstrument
test73c: PROFILER=-m cProfile
test73 test73c: PROFILE_OUT=-o output/profile.txt
test73 test73c: testcase archive_profile

# Unit tests
test_unit: clean_cache
	$(PY) -m  pytest tests/test_unit_tagmaker.py
	$(PY) -m pytest tests/test_unit_cache.py
	$(PY) -m pytest tests/test_unit_lemmatizer.py
	$(PY) -m pytest tests/test_unit_analex.py
	$(PY) -m pytest tests/test_unit_qalsadi_eval.py
	$(PY) -m pytest tests/test_unit_resultformatter.py
	$(PY) -m pytest tests/test_unit_cli.py

# Unit tests
unittest:
	$(PY) -m unittest discover -s tests

eval:clean_cache
	cd tests && $(PY) qalsadi_eval.py samples/Nemlar --csv output/results.csv --recursive --limit 10
eval_all: clean_cache
	cd tests && $(PY) qalsadi_eval.py samples/Nemlar --csv output/results.csv --recursive
# Run all tests
test_all: test2 testqrn teststop testone test1000 test63 test73 test73c

# install active devvelopement qalsadi
dev:
	pip install -e .[dev]


# Default run
run:
	python -m qalsadi --text "ذهب الطفل إلى المدرسة" --format table --profile main

run_analyze:
	python -m qalsadi --mode analyze --text "الولد يلعب"

# Lemmas only using lemmatizer
run-lemmatize:
	python -m qalsadi --mode lemmatize --text "ذهب الطفل إلى المدرسة" --format json

# Output as JSON
run-json:
	python -m qalsadi --text "ذهب الطفل إلى المدرسة" --format json --profile all

# Output as CSV
run-csv:
	python -m qalsadi --text "أحب القراءة في المكتبة" --format csv --profile all

# Lemmas only
run-lemmas:
	python -m qalsadi --text "ذهب الطفل إلى المدرسة" --format table --profile lemmas

# From file
run-from-file:
	python -m qalsadi --file tests/samples/text.txt --format table --profile roots

# From stdin
run-stdin:
	echo "الولد يلعب في الحديقة" | python -m qalsadi --stdin --format html --profile inflect

# HTML display (requires browser to view output meaningfully)
run-html:
	python -m qalsadi --text "الكتاب مفيد" --format html --profile main

run-dir:
	python -m qalsadi --mode analyze --path examples/ --format json

lint:
	ruff qalsadi/

lint-fix:
	ruff qalsadi/ --fix