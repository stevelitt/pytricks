#!/usr/bin/python3
"""
Demonstrate string slicing to add commas every
three digits, starting from the right.

Copyright (c) 2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""

def insert_commas(numstr):
    """
    Blows off leading zeros, then inserts commas
    after every three digits starting from the right.
    """
    def blow_off_leading_zeros(numstr):
        done = len(numstr) <= 1
        while True:
            if len(numstr) < 2:
                return numstr
            elif numstr[0] == '0':
                numstr = numstr[1:]
            else:
                return numstr

    numstr = blow_off_leading_zeros(numstr)
    newstr = ''
    sep = ''

    while True:
        strlen = len(numstr)
        if strlen < 1:
            return newstr
        elif strlen < 4:
            return numstr + sep + newstr
        else:
            newstr = numstr[-3:] + sep + newstr
            numstr = numstr[:-3]
            sep = ','


def makestring(num):
    rtrn = ''
    num = int(num)
    for ss in range(num):
        rtrn = rtrn  + str(ss % 10) 
    return rtrn


def main():
    for ss in range(13):
        sanscommas = makestring(ss)
        withcommas = insert_commas(sanscommas)
        pline = '{} produces {}'
        pline = pline.format(sanscommas, withcommas)
        print(pline)

if __name__ == "__main__":
    main()

