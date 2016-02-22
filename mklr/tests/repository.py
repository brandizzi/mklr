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

import unittest

import os.path
import tempfile
import shutil

from mklr.repository import Repository

class TestRepository(unittest.TestCase):
    """
    ``mklr.repository.Repository`` is a class representing, well, Git repos. It
    provides basic utilities we need when dealing with them, e. g. the ability
    to clone a branch from a repository into a new one.

    For this test, we are going to use a Git repository under the directory
    ``mklr.tsts.resources.repo1``. It has three branches (``master``,
    ``branch1``, ``branch2``) with the following commits::

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
    """

    def test_checkout(self):
        """
        ``mklr.repository.Repository`` should be able to change the branch from
        its repository.
        """
        repo = Repository(repo1_dir())

        repo.checkout('master')
        head = repo.get_head()

        self.assertEquals('b31bc3aec13846e15f88ef31fd8639e03a1df39a', head.id)
        self.assertEquals('Fifth master commit.\n', head.message)


        repo.checkout('branch1')
        head = repo.get_head()

        self.assertEquals('5176b86e0ce9f4d82f4f59de7f4a8b692e2ae992', head.id)
        self.assertEquals('Second branch1 commit.\n', head.message)

        repo.checkout('branch2')
        head = repo.get_head()

        self.assertEquals('84857c12b84237c30579a5e852e6ecbd5fbbfa2f', head.id)
        self.assertEquals('Second branch2 commit.\n', head.message)

    def test_clone_branch(self):
        """
        ``mklr.repository.Repository`` should be able to clone itself in another
        directory.
        """
        repo = Repository(repo1_dir())

        temp_dir = tempfile.mkdtemp()
        clone = repo.clone(to=temp_dir, branch='branch1')

        head = clone.get_head()

        self.assertEquals('5176b86e0ce9f4d82f4f59de7f4a8b692e2ae992', head.id)
        self.assertEquals('Second branch1 commit.\n', head.message)

        with open(os.path.join(temp_dir, 'file')) as f:
            self.assertEquals('branch1 2\n', f.read())

        shutil.rmtree(temp_dir)

def repo1_dir(filename=__file__, path_components=('resources', 'repo1')):
    test_dir = os.path.dirname(filename)

    return os.path.join(test_dir, *path_components)

