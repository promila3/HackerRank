#!/bin/python3
# https://www.hackerrank.com/challenges/repeated-string/submissions/code/122383924
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    nums = s.count('a')
    lenS = len(s)
    q = n // lenS
    rem = n % lenS
    result = q * nums
    remS = s[:rem]
    result += remS.count('a')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
