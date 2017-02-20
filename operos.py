#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
print(os.name)
print(os.environ)
print(os.path.abspath('.'))
print(os.path.join('/Users/michael', 'testdir'))
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
