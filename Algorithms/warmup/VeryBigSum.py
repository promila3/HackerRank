#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

sumarr = 0

for i in range(0,n):
    sumarr += arr[i]
    
    

print sumarr
