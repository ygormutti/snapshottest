# -*- coding: utf-8 -*-
# pysnap: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import GenericRepr, Snapshot
from pysnap.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_me_endpoint 1'] = {
    'url': '/me'
}

snapshots['test_unicode 1'] = 'pépère'

snapshots['test_object 1'] = GenericRepr('SomeObject(3)')

snapshots['test_file 1'] = FileSnapshot('snap_test_demo/test_file 1.txt')

snapshots['test_multiple_files 1'] = FileSnapshot('snap_test_demo/test_multiple_files 1.txt')

snapshots['test_multiple_files 2'] = FileSnapshot('snap_test_demo/test_multiple_files 2.txt')
