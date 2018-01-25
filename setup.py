"""
2018.Jan
@author: Tomoki Emmei
description: setup program for packaging myapp.multiplication
"""

from setuptools import setup, find_packages

__author__='Tomoki Emmei'

setup(
    name='multiplication',
    version='1.0', #version
    description='Tools to indicate a multiplication or addition table',
    author='Tomoki Emmei', # name of the author
    author_email='0699559246.edu.k@u-tokyo.ac.jp', # contact to the author
    url='https://github.com/TomokiEmmei/kadai', #github repository
    packages=find_packages(), #find "multiplication" package
    include_package_data=True, 
    keywords=['multiplication', 'addition'],
    license='MIT',
    entry_points={
        'console_scripts':[
            'multiplication = myapp.multiplication:main', # make command
        ],
    },
 )
