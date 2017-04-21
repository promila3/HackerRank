#!/bin/python

import sys

def calcPoints(a,b,pts):
    if a!= b :
        if a > b :
            pts[0] +=1 
        else :
            pts[1] +=1
def solve(a0, a1, a2, b0, b1, b):
    # Complete this function
    pts = [0,0]
    calcPoints(a0,b0,pts)
    calcPoints(a1,b1,pts)
    calcPoints(a2,b2,pts)
    return pts
        

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
