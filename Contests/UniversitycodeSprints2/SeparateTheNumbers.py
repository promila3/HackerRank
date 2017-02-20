'''
https://www.hackerrank.com/contests/university-codesprint-2/challenges/separate-the-numbers
A numeric string, , is beautiful if it can be split into a sequence of two or more positive integers, , satisfying the following conditions:

 for any  (i.e., each element in the sequence is  more than the previous element).
No  contains a leading zero. For example, we can split  into the sequence , but it is not beautiful because  and  have leading zeroes.
The contents of the sequence cannot be rearranged. For example, we can split  into the sequence , but it is not beautiful because it breaks our first constraint (i.e., ).
The diagram below depicts some beautiful strings:

image

You must perform  queries, where each query consists of some string . For each query, print whether or not the string is beautiful on a new line. If it's beautiful, print YES x, where  is the first number of the increasing sequence (if there are multiple such values of , choose the smallest); otherwise, print NO instead.

Input Format

The first line contains an integer denoting  (the number of strings to evaluate). 
Each of the  subsequent lines contains some string  for a query.

Constraints

Each character in  is a decimal digit from  to  (inclusive).
Output Format

For each query, print its answer on a new line (i.e., either YES x where  is the smallest first number of the increasing sequence, or NO).

Sample Input 0
'''
#!/bin/python

import sys

def checkseq(first, s, call):
    lenS = len(s)
    if ((lenS) == 0 ) and (call == 1):
        return False
    elif lenS == 0 :
        return True
    else :
        pass
    secondS = s[0]
    if lenS ==  1 :
        return (int(secondS) - first) == 1
    for i in range(1,lenS):        
        secondNum = int(secondS)
        #print secondNum, first
        if (secondNum-first ) == 1 :
            #print secondNum, first
            return (checkseq(secondNum,s[i:],0) and True) 
        elif (secondNum-first) > 1:
            return False
        else :
            secondS = ''.join(s[:i+1])
            #print secondS, "secondS"
    secondNum = int(secondS)
    #print secondNum
    if (secondNum-first ) == 1 :
        return True
    else :
        return False

def canStringBeSplit(s):
    # there have to be at least two numbers
    
    s = list(s)
    n = len(s)
    for i in range(n-1):
        first = int(''.join(s[:i+1]))
        #print first
        #print s[i+1:]
        result = checkseq(first,s[i+1:],1)
        if result :
            #print result, first
            return result, first
        
        else :
            #print result
            #print result
            pass
            #return result, -1
    return False, -1
    
            
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    if s.startswith('0') :
        result = False
    else :
        result, firstNumber = canStringBeSplit(s)
    
    if result :
        print "YES", firstNumber
    else :
        print "NO"
