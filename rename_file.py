#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename:  del_pyc.py
# Author: iLazy
# Date:2011-03-26

import os
import fnmatch
def all_files(root, patterns='*'):
    """
        
     """
    patterns = patterns.split(';')
    for path, subdir, files in os.walk(root):
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern.strip()):
                    yield os.path.join(path, name)

if __name__=='__main__':
    for path in all_files(os.getcwd(),'*.py'):
        dirname = os.path.dirname(path)
        basename = os.path.basename(path)
        root, extention = os.path.splitext(basename)
        rename = os.path.basename(os.path.splitext(path)[0] +'.txt')
        os.rename(path,dirname + os.sep + rename)
