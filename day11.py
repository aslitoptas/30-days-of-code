#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourglassSum = list()
    for i in range(4):
        for j in range(4):
            #Cleaner version
            #hourglass=sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
            #Submitted version
            hourglass=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            hourglassSum.append(hourglass)
    print(max(hourglassSum))
