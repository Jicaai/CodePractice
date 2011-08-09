#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename:  directory_traverse.py
# Author: Tiny
# Date:2011-08-09

import os
import fnmatch
def all_files(root, patterns='*', single_level=False, yield_folders=False):
    """
    list all the file in the directory
    """
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
	    files.sort()
	    for name in files:
                for pattern in patterns:
                    if fnmatch.fnmatch(name, pattern.strip()):
                        yield os.path.join(path, name)
                        break
    if single_level:
        break

if __name__=='__main__':
    pass

