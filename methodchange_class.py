#!/usr/bin/python
"""
Demonstrate monkey patching: Another word for changing
a method class-wide, so that from the moment of the
change, all instances of the class now use the new
method.
Copyright (c) 2015-2016 by Steve Litt
License Expat: http://directory.fsf.org/wiki/License:Expat 
"""

import types

class Person:
    """
    The original class
    """
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def articulate(self):
        print('{} {}'.format(self.fname, self.lname))

def pretty_articulate(self):
    """
    The new class method to replace the original
    Person.articulate()
    """
    st = 'The great and honorable {} {} is presented!'
    st = st.format(self.fname, self.lname)
    print(st)

jim = Person('Jim', 'Johnson')

jim.articulate()

Person.articulate = pretty_articulate
del pretty_articulate  # Not necessary, but cleans up namespace

jim.articulate()

dave = Person('Dave', 'Davidson')

dave.articulate()
