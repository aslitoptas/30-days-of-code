#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    try:
        n = int(input().strip())
        if 2<=n<=20:                            #Constraints
            for i in range(1,11):
                print(n, 'x', i, '=', n*i)
    except:
        print('Invalid input.')