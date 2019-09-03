# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# jumping on clouds
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    minJumps = 0
    ctr = 0
    while ctr+1 < len(c):
        if (ctr+2 < len(c)) and (c[ctr+2] == 0):
            minJumps +=1 
            ctr +=2
        elif c[ctr+1] == 0:
            minJumps +=1 
            ctr +=1
    return minJumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
