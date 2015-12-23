#!/usr/bin/python3

# Copyright (C) 2014 Steve Litt, Expat license, http://directory.fsf.org/wiki/License:Expat

import sys
import re

def loopthrough(callback, stop_by):
    print('==============')
    numbers = [1, 0]
    callback(numbers, stop_by)
    while numbers[0] < stop_by:
        numbers = callback(numbers, stop_by)



def cb_count_up(numbers, stop_by):
    numbers[0] += 1
    print('Count at {}'.format(str(numbers[0])))
    return numbers 

def cb_fibbonacci(numbers, stop_by):
    newnum = numbers[0] + numbers[1]
    numbers[0] = numbers[1]
    numbers[1] = newnum
    print('Next Fibbonacci is {}'.format(str(newnum)))
    if newnum >= stop_by:
        numbers[0] = newnum
    return numbers 

def cb_factorial(numbers, stop_by):
    junk = numbers[1]
    if numbers[1] == 0:
        numbers[1] = 1
    else:
        numbers[1] += 1
    numbers[0] *=  (numbers[1])
    print('Next factorial is {}'.format(str(numbers[0])))
    return numbers



loopthrough(cb_count_up, 8)
loopthrough(cb_fibbonacci, 22)
loopthrough(cb_factorial, 444)
