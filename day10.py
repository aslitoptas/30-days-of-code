#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    radix = list()
    while(n != 1):
        if n%2 == 0:
            n = n//2
            radix.append(0)
        elif n%2 == 1 and n>1:
            n = n//2
            radix.append(1)
        if n == 1:
            radix.append(1)
    #Change the order of the elements to view the binary number correctly
    #Just for checking, not necessary
    radix.reverse()
    #Initialize the list with the first element as 0, to avoid list index errors
    count = [0]
    i = 0
    #Count consecutive 1's and put in a list to find the maximum
    for x in radix:
        if x == 1:
            count[i] = count[i] + 1
        else:
            #Extend the list only when the sequence is broken
            #Do not extend multiple times if there are consecutive zeroes
            if 0 not in count:
                count.append(0)
                i += 1
    #Cleaning up the list, not necessary
    if 0 in count:
        count.remove(0)
    print(max(count))
