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

import git

class Repository(object):
    """
    ``mklr.repository.Repository`` is a class representing, well, Git repos. It
    provides basic utilities we need when dealing with them, e. g. the ability
    to clone a branch from a repository into a new one.
    """

    def __init__(self, location):
        self.location = location
        self.repo = git.Repo(location)

    def checkout(self, branch):
        self.repo.head.reference = branch

    def get_head(self):
        commit = self.repo.head.commit
        return Commit(commit.hexsha, commit.message)

    def clone(self, to, branch=None):
        self.repo.clone(to, branch=branch)

        return Repository(to)

class Commit(object):

    def __init__(self, id, message):
        self.id = id
        self.message = message
