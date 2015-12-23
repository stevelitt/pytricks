#!/usr/bin/python
import types

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def articulate(self):
        print('{} {}'.format(self.fname, self.lname))

def pretty_articulate(self):
    st = 'The great and honorable {} {} is presented!'
    st = st.format(self.fname, self.lname)
    print(st)

jim = Person('Jim', 'Johnson')

jim.articulate()

Person.articulate = pretty_articulate

jim.articulate()

dave = Person('Dave', 'Davidson')

dave.articulate()
