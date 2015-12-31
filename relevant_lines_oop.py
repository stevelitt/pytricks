#!/usr/bin/python3
import sys
import types
import re
import subprocess

class Relevant_lines():
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


def main():

    class Rl_inotify(Relevant_lines):
        def is_relevant(self):
            return True  ### Move down to restrict passed lines
            if re.match('/dev/pts/', self.this_line_text):
                return False
            if re.match('/dev/snd/', self.this_line_text):
                return False
            if re.match('/dev/input/', self.this_line_text) and re.search('ACCESS', self.this_line_text):
                    return False
            if re.match('/dev/\s', self.this_line_text):
                return False
            return True

    procout = subprocess.Popen(['/usr/bin/inotifywait', '-m', '-r', '/dev'], stdout=subprocess.PIPE, bufsize=1)
    rl = Rl_inotify(procout.stdout)
    #rl = Rl_inotify(sys.stdin)

    (lineno, txt) = rl.nextt()
    while lineno != -99:
        print(txt)
        (lineno, txt) = rl.nextt()

main()
