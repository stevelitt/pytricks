#!/usr/bin/python3

"""
Based on filename, find if it's a directory, a regular
file, symlink, or none of the above. Prints the full
pathname, and for symlinks, prints the full path of the
target file or directory.

Copyright (c) 2015-2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""


def outerfunction(arr):
    """
    outerfunction() calls innerfunction from a loop.
    """
    def innerfunction(num):
        """
        innerfunction() is declared inside of outerfunction()
        and is visible only from within outerfunction()
        """
        if num % 2 == 0:
            print(num)
    ss = 0
    while arr[ss] != -1:
        innerfunction(arr[ss])
        ss += 1

def main():
    outerfunction([1,2,3,4,5,6,7,8,-1])

    ## UNCOMMENT FOLLOWING 2 LINES TO PROVE innerfunction()
    ## is invisible from the outside

    # print('About to call innerfunction() from outside of outerfunction().')
    # innerfunction(4)

if __name__ == "__main__":
    main()

