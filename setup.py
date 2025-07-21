#! /usr/bin/python
from setuptools import setup
from io import open
# to install type:
# python setup.py install --root=/
def readme():
    with open('README.md', encoding='utf8') as f:
        return f.read()

setup (name='qalsadi', version='0.5.1',
      description='Qalsadi Arabic Morphological Analyzer and lemmatizer for Python',
      long_description = readme(),  
      long_description_content_type='text/markdown',
      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail .com',
      url='http://qalsadi.sourceforge.net/',
      license='GPL',
      package_dir={'qalsadi': 'qalsadi',},
      packages=['qalsadi'],
      include_package_data=True,
      install_requires=['Arabic-Stopwords>=0.4.2', 
            'alyahmor>=0.2', 
            'arramooz-pysqlite>=0.4.2', 
            'codernitydb3', 
            'libqutrub>=1.2.3', 
            'mysam-tagmanager>=0.4.1',
            'naftawayh>=0.3', 
            'pickledb>=0.9.2', 
            'pyarabic>=0.6.7', 
            'tashaphyne>=0.3.4.1',
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

