# !/usr/bin/env python
#
# Copyright 2015 Adam Victor Brandizzi
#
# This file is part of mklr.
#
# mklr is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# mklr is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with mklr. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name="mklr",
    version="0.0.1.dev1",
    author='Adam Victor Brandizzi',
    author_email='adam@brandizzi.com.br',
    description='mklr',
    license='LGPLv3',
    url='http://bitbucket.com/brandizzi/mklr',

    packages=find_packages(),
    test_suite='mklr.tests',
    test_loader='unittest:TestLoader',
)
