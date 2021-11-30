#!/bin/python3

import math
import os
import random
import re
import sys
import string

if __name__ == '__main__':
    try:
        n = int(input().strip())
    except:
        print('Invalid input.')
    
    if n>=1 and n<=1000:
        arr = list(map(int, input().rstrip().split()))
        #Clear extra elements to keep the array size N
        del arr[n:]
        #Re-arranging them in reverse order
        arr.reverse()
        #Make the list a string and remove brackets and commas
        str_rev=str(arr).lstrip('[').rstrip(']').replace(',','')
        print(str_rev)
    else:
        print('Constraint error.')
