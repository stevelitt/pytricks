#!/usr/bin/python3
"""
Simple contrived data entry form attached to data files

This illustrates a data entry form that reads and
writes from data files in the ./data directory.
This isn't CRUD because it can't create or delete,
only update.

Copyright (c) 2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""

import sys

### DON'T BLAME ME FOR THE FOLLOWING 4 LINES
if sys.version_info[0] == 2:
    from Tkinter import *
elif sys.version_info[0] == 3:
    from tkinter import *

normfont=('Sans', 18)

def readData(key):
    """
    Read data from file named data/<key>
    """
    try:
        f = open('data/' + key, 'r')
    except:
        return('')
    return f.readline().strip()

def writeData(key, data):
    """
    Write data to file named data/<key>
    """
    fname = 'data/' + key
    try:
        f = open(fname, 'w')
    except:
        pline='writeData failed to open file {} for write.'
        pline=pline.format(fname)
        print(pline)
        pline='Error reported as {}:{}.'.format(sys.exc_info()[0],sys.exc_info()[1])
        print(pline)
        sys.exit(1)
    f.write(data)
    f.write('\n')
    f.close()

class Application(Frame): 
    """
    class Application is this application, subclassed
    from Tk.Frame. It provides almost everything for
    running an intelligent data entry form.
    """
    def __init__(self, master=None):
        """
        Set up the data entry form
        """
        Frame.__init__(self, master) 
        self.grid()                 
        self.defineWidgets()
        self.defineHotkeys()
        self.layoutWidgets()
        self.initEntryFields()
        self.master.title('Person Form')

    def defineWidgets(self):
        """
        Define form elements (widgets)
        """
        self.labelf = Label(self, text='First name:', font=normfont)
        self.entryf = Entry(self, font=normfont)
        self.labell = Label(self, text='Last name:', font=normfont)
        self.entryl = Entry(self, font=normfont)
        self.labelj = Label(self, text='Job:', font=normfont)
        self.entryj = Entry(self, font=normfont)
        self.quitButton = Button(self, text='Cancel', font=normfont, 
            command=self.cancel)     
        self.saveButton = Button(self, text='Save', font=normfont, 
            command=self.save)     
        self.labeli1 = Label(self, text='F10 to save', font=normfont)
        self.labeli2 = Label(self, text='Alt+Q to cancel', font=normfont)

    def defineHotkeys(self):
        """
        Define hotkeys for form and elements with focus
        """
        self.master.bind('<Alt-q>', self.cancel)
        self.master.bind('<F10>', self.save)
        self.quitButton.bind('<Return>', self.cancel)
        self.saveButton.bind('<Return>', self.save)

    def layoutWidgets(self):
        """
        Lay out form elements
        """
        self.labelf.grid(row=0)    
        self.entryf.grid(row=0, column=1)    
        self.labell.grid(row=1)    
        self.entryl.grid(row=1, column=1)    
        self.labelj.grid(row=2)    
        self.entryj.grid(row=2, column=1)    
        self.quitButton.grid(row=3)    
        self.saveButton.grid(row=3, column=1)    
        self.labeli1.grid(row=5)    
        self.labeli2.grid(row=5, column=1)

    def initEntryFields(self):
        """
        Prepopulate entry fields with data from hard disk.
        """
        self.entryf.delete(0, END)
        self.entryf.insert(0, readData('fname'))
        self.entryl.delete(0, END)
        self.entryl.insert(0, readData('lname'))
        self.entryj.delete(0, END)
        self.entryj.insert(0, readData('job'))

    def cancel(self, event=None):
        """
        Quit without saving
        """
        quit()

    def save(self, event=None):
        """
        Save then exit
        """
        fname = self.entryf.get()
        lname = self.entryl.get()
        job = self.entryj.get()
        writeData('fname', fname)
        writeData('lname', lname)
        writeData('job', job)
        quit()

def main():
    """
    Run the application
    """
    app = Application()              
    app.mainloop()    

if __name__ == '__main__':
    main()
