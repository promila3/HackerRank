#!/bin/python

import math
import os
import random
import re
import sys
from bisect import insort

def find_median(a,n):
    middle = math.ceil(n/2)
    middle = int(middle)
    #print middle
    if (n % 2 != 0): # even
        print a[middle] * 1.0
    else :
        print (a[middle-1]+ a[middle])/2.0
        
    return

def median(a):
    if len(a)%2==0:
        l=a[len(a)//2];r=a[(len(a)//2)-1]
        med=(l+r)/2.0
        
    elif len(a)%2 !=0:
        med=a[len(a)//2]
    return med


if __name__ == '__main__':
    n = int(raw_input())

    a = []
    ctr = 0
    for _ in xrange(n):
        a_item = int(raw_input())
        #a.append(a_item)
        insort(a, a_item)
        ctr +=1
        #result = median(a)
        result = find_median(a,ctr)
