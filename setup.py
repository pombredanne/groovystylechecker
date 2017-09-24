#!/usr/bin/env python3

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='groovystylechecker',
    version='0.0.4',
    description='Groovy code style checker',
    long_description=long_description,
    url='https://github.com/sT331h0rs3/groovystylechecker',
    author='sT331h0rs3',
    author_email='sT331h0rs3@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='groovy codestyle checker',
    packages=['groovystylechecker'],
    python_requires='>=3',
    tests_require=['pycodestyle'],
    entry_points={
        'console_scripts': [
            'groovystylechecker=groovystylechecker.__main__:main',
        ],
    },
)
