#! /usr/bin/python
from setuptools import setup
from io import open
# to install type:
# python setup.py install --root=/
def readme():
    with open('README.rst') as f:
        return f.read()

setup (name='qalsadi', version='0.3.3',
      description='Qalsadi Arabic Morphological Analyzer for Python',
      long_description = readme(),      
      author='Taha Zerrouki',
      author_email='taha. zerrouki@gmail .com',
      url='http://qalsadi.sourceforge.net/',
      license='GPL',
      package_dir={'qalsadi': 'qalsadi',},
      packages=['qalsadi'],
      include_package_data=True,
      install_requires=[ 'CodernityDB==0.4.2', 
						'libqutrub>=1.0',
						'naftawayh>=0.2',
						'pyarabic>=0.6.2',
						'tashaphyne==0.3.1',
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

