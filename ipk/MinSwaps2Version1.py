#!/bin/python3
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    lenArr = len(arr)
    swaps = 0
    
    for i in range(lenArr-1):
        minVal = float('inf')
        indexVal = None
        for j in range(i+1,lenArr):
            if arr[i] > arr[j] and arr[j] < minVal:
                minVal = arr[j]
                indexVal = j
        if indexVal != None:
            arr[i], arr[indexVal] = arr[indexVal],arr[i]
            swaps +=1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
