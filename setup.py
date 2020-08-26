#! /usr/bin/python
from setuptools import setup
from io import open
# to install type:
# python setup.py install --root=/
def readme():
    with open('README.rst', encoding='utf8') as f:
        return f.read()

setup (name='qalsadi', version='0.4',
      description='Qalsadi Arabic Morphological Analyzer for Python',
      long_description = readme(),      
      author='Taha Zerrouki',
      author_email='taha. zerrouki@gmail .com',
      url='http://qalsadi.sourceforge.net/',
      license='GPL',
      package_dir={'qalsadi': 'qalsadi',},
      packages=['qalsadi'],
      include_package_data=True,
      install_requires=[ "six>=1.10.0",
                "future>=0.16.0",
                "pickledb>=0.9.2",
                "alyahmor>=0.1",
                "libqutrub>=1.2.3",
                "naftawayh>=0.3",
                "pyarabic>=0.6.7",
                "tashaphyne>=0.3.4.1",
                "arramooz-pysqlite>=0.3",
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

