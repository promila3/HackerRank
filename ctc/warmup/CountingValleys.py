# Counting Valleys
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    InValley = False
    result = 0
    for a in s:
        if a == 'D' and level == 0:
            InValley = True
            level -= 1
            continue
        if a == 'D' and InValley:
            level -=1
            continue
        if a == 'U' and InValley:
            level +=1 
            if level == 0:
                InValley = False
                result += 1
                continue
            continue
        if a == 'U' :
            level +=1
        elif a == 'D':
            level -=1
 #       print(a)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
