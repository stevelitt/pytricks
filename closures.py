#!/usr/bin/python3
def counter_factory():
  count = 0
  def counter():
     nonlocal count
     count = count + 1
     return count
  return counter

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


