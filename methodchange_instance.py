#!/usr/bin/python
"""
Change a method in an instance of a class (an object).

Demonstrate how to change a method in one specific 
instance of a class, without affecting the class or
any other instances.

Copyright (c) 2015-2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""
import types

class Person:
    """
    Demonstration class. Method articulate() will be
    replaced in an instance.
    """
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def articulate(self):
        print('{} {}'.format(self.fname, self.lname))


def main():
    """
    Uses the types.MethodType() call to replace this
    instance's version of the articulate() method.

    Note that usually it's easier and more pythonic
    to simply subclass the original class.
    """

    def pretty_articulate(self):
        """
        The replacement method
        """
        st = 'The great and honorable {} {} is presented!'
        st = st.format(self.fname, self.lname)
        print(st)

    jim = Person('Jim', 'Johnson')
    jim.articulate()
    jim.articulate = types.MethodType(pretty_articulate, jim, Person)
    del pretty_articulate  # Not necessary, but cleans up namespace
    jim.articulate()
    dave = Person('Dave', 'Davidson')
    dave.articulate()


if __name__ == "__main__":
    main()
