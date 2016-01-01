#!/usr/bin/python3

"""
Demonstrate use of Relevent_lines() class to provide an
intelligent continue statement, and how to subclass it 
for your unique use case.
Copyright (c) 2015-2016 by Steve Litt
License Expat: http://directory.fsf.org/wiki/License:Expat 
"""


import sys
import types
import re
import subprocess

class Relevant_lines():
    """
    Base class for intelligent continue statement.
    Subclass it to screen out the right lines, by
    overriding the is_relevant() method. Although
    not demonstrated in this program, break logic
    can be implemented by overriding tweak() and
    using one or more added properties (such as
    counters or "last iteration save variables).
    Methods nextt() is not meant to be overridden.
    """
    def __init__(self, streem):
        self.streem = streem
    EOF = False
    this_line_number = 0
    this_line_text = 'init'
    def is_relevant(self):
        return self.this_line_text.strip() != ''
    def tweak(self):
        return 0
    def nextt(self):
        self.this_line_text = self.streem.readline().decode('utf-8')
        if self.this_line_text == '':
            self.EOF = True
        self.this_line_number += 1
        while not self.EOF and not self.is_relevant():
            self.this_line_text = self.streem.readline().decode('utf-8')
            if self.this_line_text == '':
                self.EOF = True
            self.this_line_number += 1
        self.this_line_text = self.this_line_text.strip()
        if self.EOF:
            return -99, 'basura'
        else:
            self.tweak()
            return self.this_line_number, self.this_line_text


class Rl_inotify(Relevant_lines):
    """
    The Rl_inotify class overrides the base is_relevant()
    method to screen out the desired lines.
    """

    def is_relevant(self):
        """
        The is_relevant() method is what screens out the
        desired lines. In this example program, it is
        created for ease of experimentation.
        """

        #if re.match('/dev/pts/', self.this_line_text):
        #    return False
        #if re.match('/dev/snd/', self.this_line_text):
        #    return False
        #if re.match('/dev/input/', self.this_line_text) and re.search('ACCESS', self.this_line_text):
        #        return False
        #if re.match('/dev/\s', self.this_line_text):
        #    return False
        return True




def main():
    """
    main() runs the logic of this program.
    It instantiates an instance of the
    Rl_inotify subclass of the Relevant_lines
    superclass. Then it uses subprocess.Popen
    to run inotifywait and receive its output
    as input. Finally, it runs a loop that gets
    the next relevant line from Rl_notify.nextt().
    """


    procout = subprocess.Popen(['/usr/bin/inotifywait', '-m', '-r', '/dev'], stdout=subprocess.PIPE, bufsize=1)
    rl = Rl_inotify(procout.stdout)
    #rl = Rl_inotify(sys.stdin)

    (lineno, txt) = rl.nextt()
    while lineno != -99:
        print(txt)
        (lineno, txt) = rl.nextt()


if __name__ == "__main__":
    main()
