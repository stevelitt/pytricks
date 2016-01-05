#!/usr/bin/python3
"""
Hello World for Python's tkinter

Simplest possible Python GUI program, with the
addition of font and padding to make it visible 
on a projector. Note the fancy footwork importing
"tkinter" for Python3 but "Tkinter" for
Python 2.

Copyright (c) 2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""

import sys

### DON'T BLAME ME FOR THE FOLLOWING 4 LINES
if sys.version_info[0] == 2:
    from Tkinter import *
elif sys.version_info[0] == 3:
    from tkinter import *


def main():
    """
    Make trivial window with bigger font and more
    padding.
    """
    root = Tk()
    root.wm_title('Hello App')

    w = Label(root, text='Hello world', font=('Sans', 48))
    w.pack(padx=200, pady=300)

    root.mainloop()

if __name__ == '__main__':
    main()
