#!/usr/bin/env python3

import pycodestyle
from os import path

print('Running code style check...')
files_to_check = path.abspath(path.join(path.dirname(__file__), '..'))
style = pycodestyle.StyleGuide(paths=[files_to_check, ])
result = style.check_files()
if result.total_errors == 0:
    print('Code style check succeeded.')
    exit(0)
else:
    print('Code style check failed.')
    exit(1)
