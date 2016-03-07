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

import unittest
import os.path
import uuid

import mklr.command

from mklr.tests.util import commands_dir


class TestCommand(unittest.TestCase):
    """
    ``mklr.command.Command`` is a class to call and interact with commands
    sent to the OS.
    """

    def test_call(self):
        """
        ``mklr.command.call()`` should call the command given to it.
        """
        path = commands_dir()
        cmd_path = os.path.join(path, 'cat.py')
        file_path = os.path.join(path, 'test')

        result = mklr.command.call('python', cmd_path, file_path)

        self.assertEquals('example\n', result.output)
        self.assertEquals(0, result.exit_code)

    def test_call_command_failed(self):
        """
        ``mklr.command.call()`` should not raise exception if command returns
        non-zero code. Instead, it gives us an error code and the stderr
        output.
        """
        path = commands_dir()
        cmd_path = os.path.join(path, 'cat.py')
        file_path = uuid.uuid1()

        result = mklr.command.call('python', cmd_path, file_path)

        self.assertEquals('', result.output)
        self.assertEquals(
            'Command failed on '+str(file_path)+'\n', result.errors
        )
        self.assertEquals(1, result.exit_code)

    def test_call_command_not_found(self):
        """
        ``mklr.command.call()`` should raise exception if command is not found.
        """
        cmd_path = uuid.uuid1()
        file_path = uuid.uuid1()

        with self.assertRaises(OSError):
            mklr.command.call(cmd_path, file_path)
