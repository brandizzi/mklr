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

import os.path

def repo1_dir(filename=__file__, path_components=('resources', 'repo1')):
    """
    Returns the path to the repository used for most tests. This repository
    This repository has three branches (``master``, ``branch1``, ``branch2``)
    with the following commits::

    * b31bc3a Fifth master commit.
    * 4e12c21 Fourth master commit.
    | * 84857c1 Second branch2 commit.
    | * f742527 First branch2 commit.
    | | * 5176b86 Second branch1 commit.
    | | * 2edeac2 First branch1 commit.
    | |/
    |/|
    * | 78aa0d7 Third master commit.
    |/
    * fe766b4 Second master commit.
    * 10572be First master commit.

    >>> path = repo1_dir()
    >>> sorted(os.listdir(os.path.join(path, '.git', 'refs', 'heads')))
    ['branch1', 'branch2', 'master']

    Each commit edits a sole file, called ``file``.

    >>> os.path.isfile(os.path.join(path, 'file'))
    True
    """
    test_dir = os.path.dirname(filename)

    return os.path.join(test_dir, *path_components)

