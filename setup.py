#!/usr/bin/env python
from distutils.core import setup

with open('Readme.md') as f:
      long_description = f.read()

setup(name='DtwSom',
      packages=['DtwSom'],
      version='0.2.1',
      description='Implementation of the Dynamic Time Warping Self Organizing Maps (DTW-SOM)',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Kenan Li',
      author_email="kenanl@usc.edu",
      license="CC BY 3.0",
      install_requires=['numpy', 'fastdtw'],
      url='https://github.com/Kenan-Li/dtwsom',
      download_url='https://github.com/Kenan-Li/dtwsom/archive/master.zip',
      keywords=['self-organizing map', 'time series analysis', 'clustering', 'dimentionality reduction', 'dynamic time warping']
 )
