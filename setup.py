#! /usr/bin/python
from setuptools import setup

# to install type:
# python setup.py install --root=/
def readme():
    with open('README.md') as f:
        return f.read()

setup (name='qalsadi', version='0.3',
      description='Qalsadi Arabic Morpholoc=gical Analyzer for Python',
      long_description = readme(),      
      author='Taha Zerrouki',
      author_email='taha. zerrouki@gmail .com',
      url='http://qalsadi.sourceforge.net/',
      license='GPL',
      package_dir={'qalsadi': 'qalsadi',},
      packages=['qalsadi'],
      include_package_data=True,
      install_requires=[ 'pyarabic',
      ],         
      package_data = {
        'qalsadi': ['doc/*.*','doc/html/*', 'data/*.*', 'qalsadi/data'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Natural Language :: Arabic',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Linguistic',
          ],
    );

