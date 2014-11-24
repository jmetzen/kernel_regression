#!/usr/bin/env python

from distutils.core import setup

setup(name='kernel_regression',
      version='1.0',
      description='Implementation of Nadaraya-Watson kernel regression with automatic bandwidth selection compatible with sklearn.',
      author='Jan Hendrik Metzen',
      author_email='jhm@informatik.uni-bremen.de',
      url='https://github.com/jmetzen/kernel_regression',
      py_modules = ['kernel_regression']
     )
