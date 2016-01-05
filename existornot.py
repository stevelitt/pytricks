#!/usr/bin/python3
"""
Checking existance in dicts and lists.

Demonstrates how to check existence of
keys and values in dictionaries and lists.

Copyright (c) 2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""

def yorn_dict(key, dictt):
    """
    Tells whether the key is in the dict,
    and if it is, whether it's value is null
    or has a value and reports the value.
    """
    if key in dictt:
        print('{} IS in dictionary.'.format(key))
        if dictt[key]:
            print('Dict\'s {} element has value {}.'.format(key, dictt[key]))
        else:
            print('Dict\'s {} element is null.'.format(key))
    else:
        print('{} is NOT in dictionary.'.format(key))


def yorn_list(ss, listt):
    """
    Tells whether the subscript is in the list,
    and if it is, whether it's value is null or has
    a value and reports the value.
    """
    if ss >= 0 and ss < len(listt):
        print('{} IS in list.'.format(ss))
        if listt[ss]:
            print('List\'s {} element has value {}.'.format(ss, listt[ss]))
        else:
            print('List\'s {} element is null.'.format(ss))
    else:
        print('{} is NOT in list.'.format(ss))



def test_dict():
    """
    Excercises a dictionary to include various cases,
    and calls yorn_dict() repeatedly to report.
    """
    d = {'zero': 0, 'one': 1, 'nine': 9, 'two': 2}
    del(d['nine'])
    d['zero'] = None
    yorn_dict('zero', d)
    yorn_dict('one', d)
    yorn_dict('nine', d)
    yorn_dict('rock', d)


def test_list():
    """
    Excercises a list to include various cases,
    and calls yorn_list() repeatedly to report.
    At the bottom it shows how to loop through
    a list using exceptions instead of len(list).
    """
    l = [None, 'one', 'two', 'three', 'four']
    print('List currently has {} elements.'.format(len(l)))
    del(l[2])
    print('List currently has {} elements.'.format(len(l)))
    yorn_list(0, l)
    yorn_list(1, l)
    yorn_list(2, l)
    yorn_list(3, l)
    yorn_list(4, l)
    yorn_list(5, l)
    yorn_list(6, l)
    ss = 0
    while True:
        try:
            elm = l[ss]
        except IndexError:
            #raise
            break;
        print('Element {} is {}.'.format(ss, l[ss]))
        ss += 1


def main():
    """
    Calls test_list and test_dict
    """
    print()
    test_dict()
    print()
    test_list()
    print()



if __name__ == '__main__':
    main()
