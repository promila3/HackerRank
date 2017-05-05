#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
neg = 0.0
pos = 0.0
zer = 0.0

for i in range(n):
    if arr[i] > 0 :
        pos +=1 
    elif arr[i] == 0 :
        zer +=1
    else :
        neg +=1
print pos/n
print neg/n
print zer/n
