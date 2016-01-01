#!/usr/bin/python3
"""
Demonstrate the use of callback functions

Copyright (c) 2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""


import sys
import re

def loopthrough(callback, stop_by):
    """
    Create and print a series of numbers until the latest
    number equals or exceeds argument stop_by. Which series
    it creates depends on the callback function argument.
    """
    print('==============')
    numbers = [1, 0]
    callback(numbers, stop_by)
    while numbers[0] < stop_by:
        numbers = callback(numbers, stop_by)



def cb_count_up(numbers, stop_by):
    """
    Callback to make a count-up series.
    """
    numbers[0] += 1
    print('Count at {}'.format(str(numbers[0])))
    return numbers 

def cb_fibbonacci(numbers, stop_by):
    """
    Callback to make the Fibbonacci series.
    """
    newnum = numbers[0] + numbers[1]
    numbers[0] = numbers[1]
    numbers[1] = newnum
    print('Next Fibbonacci is {}'.format(str(newnum)))
    if newnum >= stop_by:
        numbers[0] = newnum
    return numbers 

def cb_factorial(numbers, stop_by):
    """
    Callback to make the factorial series.
    """
    junk = numbers[1]
    if numbers[1] == 0:
        numbers[1] = 1
    else:
        numbers[1] += 1
    numbers[0] *=  (numbers[1])
    print('Next factorial is {}'.format(str(numbers[0])))
    return numbers


def main():
    """
    Call loopthrough() first with a counting callback,
    then with a fibbonacci callback, then with a
    factorial callback. Same called function, different
    callback functions, completely different results.
    """
    loopthrough(cb_count_up, 8)
    loopthrough(cb_fibbonacci, 22)
    loopthrough(cb_factorial, 444)

if __name__ == "__main__":
    main()
