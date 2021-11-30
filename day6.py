#!/bin/python3

import math
import os
import random
import re
import sys
import string

if __name__ == '__main__':
    try:
        t = int(input().strip())
    except:
        print('Invalid input.')
    
    if t>=1 and t<=10:
        for a0 in range(t):
            s = input().strip()
            index = 0
            if len(s)>=2 and len(s)<=10000:
                while index<len(s):
                #Loop should quit when it reaches the last character, which has an index of (length-1)
                    if index<2:
                        odd = s[index]
                        even = s[index + 1]
                    elif index>=2:
                        odd = odd + s[index]
                        #If string length is an odd number loop should stop at the even index
                        #Trying to add another character will give an IndexError 
                        if index<len(s)-1:
                            even = even + s[index + 1]
                    index = index + 2
                print(odd + ' ' + even)
            else:
                print('Constraint error. String is either too long or too short.')
            a0 = a0 + 1
    else:
        print('Constraint error.')
