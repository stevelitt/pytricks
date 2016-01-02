#!/usr/bin/python3
"""
Closure creates 2 independent counters.

Demonstrate a closure, where a function is declared
within a function, and the inner function uses the
local variables declared in the outer function.
Every time the outer function is called, it returns
an inner function with the outer function's local
variable reinitialized.

Copyright (c) 2015-2016 by Steve Litt
License: Expat: http://directory.fsf.org/wiki/License:Expat 
"""

def counter_factory():
  """
  This is a closure, where the outer function returns a
  reference to the inner function. Note that the inner
  function uses the count variable from the outer one,
  because of the word nonlocal.
  """
  count = 0
  def counter():
     nonlocal count
     count = count + 1
     return count
  return counter

def main():
    """
    Use counter_factory() to create two independent
    counter functions, and then run the counters to
    show they count up independent of each other.
    """
    counter1 = counter_factory()
    counter2 = counter_factory()

    print(counter1())    # 1
    print(counter1())    # 2
    print(counter1())    # 3
    print(counter2())    # 1
    print(counter1())    # 4
    print(counter2())    # 2
    print(counter2())    # 3
    print(counter1())    # 5

if __name__ == "__main__":
    main()
