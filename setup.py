# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='uri2markdown',
    version='0.0.1',
    description='uri parse to markdown',
    long_description=readme,
    author='Cong Quan',
    author_email='cqshinn92@gmail.com'',
    url='https://github.com/enixdark/parse_link_to_markdown',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

