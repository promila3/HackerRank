#!/bin/python3
# https://www.hackerrank.com/challenges/beautiful-triplets/problem

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    n = len(arr)
    result = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if d == (arr[j] - arr[i]):
                for k in range(j+1, n):
                    if (d  == arr[k] - arr[j]):
                        result +=1 
                    if d < (arr[k] - arr[j]):
                        break
            elif d < (arr[j] - arr[i]):
                break
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
