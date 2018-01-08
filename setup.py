# -*- coding: utf-8 -*-
from distutils.core import setup

try:
    with open('README.md', 'r') as f:
        readme = f.read()

    with open('LICENSE.txt', 'r') as f:
        license_ = f.read()
except:
    readme = ''
    license_ = ''

setup(
    name='unique-id',
    version='1.0.1',
    packages=['unique_id'],
    url='',
    download_url='https://github.com/slawek87/unique-id',
    license=license_,
    author=u'Sławomir Kabik',
    author_email='slawek@redsoftware.pl',
    description='Unique-ID is a small lib to generate unique ids - string values.',
    long_description=readme,
    keywords=['Python Unique ID', 'Python ID', 'Python Unique string'],
    install_requires=['setuptools'],
)
