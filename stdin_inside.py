#!/usr/bin/python3
"""
Demonstrate use of subprocess.Popen() to grab a processes
output for use as the program's input. This is the new,
Pythonic way, superceding os.Popen().
Copyright (c) 2015 by Steve Litt
License Expat: http://directory.fsf.org/wiki/License:Expat 
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
