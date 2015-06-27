#!/usr/bin/env python

import os
from setuptools import setup

setup(name='logarithmicwordcloud',
      version=1.0,
      description='Creates logarithmic sized word clouds from text files',
      author='Thomas Kajder',
      author_email='tkajder@asu.edu',
      license='MIT',
      url='https://github.com/tkajder/logarithmic-word-cloud',
      packages=['cloud', 'cloud.utils'],
      install_requires='nltk==3.0.3',
      classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Operating System :: Unix',
      'Programming Language :: Python :: 3 :: Only'])
