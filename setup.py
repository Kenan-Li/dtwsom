#!/usr/bin/env python

from distutils.core import setup

setup(name='DtwSom',
  version= '1.0',
  description='Implementation of the Dynamic Time Warping Self Organizing Maps (DTW-SOM)',
  author='Kenan Li',
  package_data={'': ['Readme.md']},
  include_package_data=True,
  license="CC BY 3.0",
  py_modules=['dtwsom'],
  requires = ['numpy', 'fastdtw'],
  url = 'https://github.com/Kenan-Li/dtwsom',
  download_url = 'https://github.com/Kenan-Li/dtwsom/archive/master.zip',
  keywords = ['machine learning', 'neural networks', 'clustering', 'dimentionality reduction']
 )
