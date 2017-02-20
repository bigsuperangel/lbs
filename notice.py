#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

l = list(range(100))[::2]
print(l)
print(list(range(1, 100, 2)))

print([d for d in os.listdir('.')])

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        if len(L)>10:                                                           #仅输出10行
            break

a = triangles()
for i in a:
    print(i)
