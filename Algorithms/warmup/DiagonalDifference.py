#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
    
sumdl = 0
countl = 0
sumdr = 0
countr = n-1
for a_i in xrange(n):
    a_temp = a[a_i]
    sumdl += a_temp[countl]
    sumdr += a_temp[countr]
    
    countl += 1
    countr -= 1

diffd = abs(sumdl - sumdr)
print diffd

