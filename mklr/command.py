# !/usr/bin/env python
#
# Copyright 2015 Adam Victor Brandizzi
#
# This file is part of mklr.
#
# mklr is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# mklr is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with mklr. If not, see <http://www.gnu.org/licenses/>.

import subprocess
from subprocess import PIPE


def call(*args):
    command = (str(a) for a in args)

    popen = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = popen.communicate()

    return Result(popen.returncode, out, err)


class Result(object):

    def __init__(self, exit_code, output, errors):
        self.exit_code = exit_code
        self.output = output
        self.errors = errors
