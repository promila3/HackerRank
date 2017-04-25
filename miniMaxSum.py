#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
#a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
numA= [int(a),int(b),int(c),int(d),int(e)]
#totsum = a + b + c + d +  e
totsum = sum(numA)
maxSum = 0
minSum = totsum
for num in numA:
    temp = totsum - num
    if temp > maxSum:
        maxSum = temp
    if temp < minSum :
        minSum = temp
print minSum, maxSum
