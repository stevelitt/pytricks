#!/usr/bin/python3
"""
Master simple string slicing by example.

Copyright (c) 2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""

org='0123456789'

eval('print(org)')

def slice_one(slice_string, org):
    """
    The string slice is passed in as a string, and
    using eval(), is executed as a string slice,
    with the slice, the original string, and the
    sliced result being printed.
    """
    cmd = 'org[' + slice_string + ']'
    newstring = eval(cmd)
    pstring='Slice "{}" on {} produces {}'
    pstring=pstring.format(slice_string, org, newstring)
    print(pstring)


def main():
    """
    Demonstrate a wide variety of string slices
    using slice_one()
    """
    slice_one('0', org)
    slice_one('1', org)
    slice_one('0:3', org)
    slice_one('1:', org)
    slice_one(':', org)
    slice_one(':1', org)
    slice_one(':-1', org)
    slice_one('-3:', org)
    slice_one(':-3', org)
    slice_one('3:5', org)
    slice_one('3:-3', org)
    slice_one('::2', org)
    slice_one('1::2', org)
    slice_one('::3', org)

    slice_one(':0:-1', org)
    slice_one('::-1', org)

if __name__ == '__main__':
    main()
