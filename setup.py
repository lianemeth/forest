from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='forest',
    version='0.0.5',
    description='A bunch of trees',
    long_description=long_description,
    url='https://github.com/lianemeth/forest',
    author='Lia  Nemeth',
    license='MIT',
    packages=find_packages(exclude=['tests*'])
)
