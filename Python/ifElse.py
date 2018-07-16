#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N % 2 != 0 :
    print "Weird"
elif N in range(2,6):
    print "Not Weird"
elif N in range(6,21):
    print "Weird"
else :
    print "Not Weird"
