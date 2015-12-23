#!/usr/bin/python3

def outerfunction(arr):
    def innerfunction(num):
        if num % 2 == 0:
            print(num)
    ss = 0
    while arr[ss] != -1:
        innerfunction(arr[ss])
        ss += 1

outerfunction([1,2,3,4,5,6,7,8,-1])
print('About to call innerfunction() from outside of outerfunction().')
innerfunction(4)
