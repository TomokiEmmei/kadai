# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:50:41 2018

@author: Tomoki_IPG
"""

from setuptools import setup, find_packages

__author__='Tomoki Emmei'

setup(
    name='multiplication', #name of the library
    version='1.0', #version
    description='Tools to indicate a multiplication or addition table',
    author='Tomoki Emmei', # name of the author
    author_email='0699559246.edu.k@u-tokyo.ac.jp', # contact to the author
    url='https://github.com/TomokiEmmei/kadai', #github repository
    packages=find_packages(),
    include_package_data=True,
    keywords=['multiplication', 'addition'],
    license='MIT',
    entry_points={
        'console_scripts':[
            'multiplication = myapp.multiplication:main',
        ],
    },
 )
