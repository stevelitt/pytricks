#!/usr/bin/python3

"""
Based on filename, find if it's a directory, a regular
file, symlink, or none of the above. Prints the full
pathname, and for symlinks, prints the full path of the
target file or directory.

Copyright (c) 2015-2016 by Steve Litt
License Expat: http://directory.fsf.org/wiki/License:Expat 
"""


import os

def investigate_filename(fname):
    """
    Check whether file is a symlink, file, dir, 
    combination, or none.
    """
    isfile = os.path.isfile(fname)
    isdir = os.path.isdir(fname)
    islink = os.path.islink(fname)
    pline = '\n{}->{} \n   islink={}, isfile={}, isdir={}'
    pline = pline.format(fname, os.path.realpath(fname), islink, isfile, isdir);
    exists = islink or isfile or isdir
    if exists:
        print(pline)
    else:
        print('\n{} does not exist.'.format(fname))


def main():
    """
    main() calls investigate_filename() four
    times for five different situations.
    """
    investigate_filename('nickname.symlink')
    investigate_filename('randir.symlink')
    investigate_filename('real.file')
    investigate_filename('/home')
    investigate_filename('nonexistant.hoax')
    print('\n')



if __name__ == "__main__":
    main()
