#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    while(True):
        try:
            N = int(input('Please enter an integer to see if it is a weird number: ').strip())
            if (N>100 or N<1):
                print('The number should be between 1 and 100.')
                continue
        except:
            print('Invalid input.')
            continue
        break
    if (N%2>0):
        print('Weird')
    elif(N<=20):
        if(N>=2 and N<=5):
            print('Not Weird')
        else:
            print('Weird')
    else:
        print('Not Weird')