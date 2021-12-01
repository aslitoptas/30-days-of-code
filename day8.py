#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    try:
        n=int(input().strip())
        if n>=0 and n<=100000:
            phoneBook=dict()  
            for entry in range(n):
                (name, phoneNumber)=input().rstrip().split()
                phoneBook[name]=phoneNumber    
            while(True):
                try:
                    query=input().strip()
                    if query in phoneBook:
                        print('{0}={1}'.format(query,phoneBook[query]))
                    else:
                        print('Not found')
                except:
                    break
        else:
            print('Constraint error.')
    except:
        print('Invalid input.')
