#!/usr/bin/python3
"""
Simulate an incoming pipe with subprocess.Popen().

Demonstrate use of subprocess.Popen() to grab a processes
output for use as the program's input. This is the new,
Pythonic way, superceding os.Popen(). It's also an
excellent way to assure that if either the called process
or this python program is killed, the other terminates.
Great for using as a daemon.

Copyright (c) 2015-2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""

import re
import subprocess



def main():
    args=['/usr/bin/inotifywait', '-m', '-r', '/dev']
    process = subprocess.Popen(args, stdout=subprocess.PIPE, bufsize=1)
    line = process.stdout.readline().decode('utf-8')
    while line != '':
        line = line.strip()
        if not re.match('/dev/pts', line) and \
           not re.match('/dev/snd', line):
                print(line)
        line = process.stdout.readline().decode('utf-8')


if __name__ == "__main__":
    main()
