# Enter your code here. Read input from STDIN. Print output to STDOUT
#Promila Agarwal : Jan 31, 2017
import math
import operator

def getMean(sumN, N):
    sumN = sumN * 1.0
    return sumN/N
    
def getMedian(numbers,N):
    if (N % 2 == 0 ):
        mid = N/2
        median = (numbers[mid-1] + numbers[mid]) * 1.0 /2
    else :
        mid = N/2
        median = numbers[mid] * 1.0
    return median

def getMode(numbers):
    c = {}
    for item in numbers:
        if item in c :
            c[item] += 1
        else :
            c[item] = 1
            
    maxItem = max(c.iteritems(), key=operator.itemgetter(1))[0]
    maxVal = c[maxItem]
    nList = []
    for item in c:
        if (c[item] == maxVal ) :
            nList.append(item)
    nList.sort()
    return nList[0]

N = int(raw_input())
numbers=[]
numbers=map(int,raw_input().strip().split(' '))
sumN = sum(numbers)


mean = getMean(sumN, N)

mode= getMode(numbers)
numbers.sort()
#print numbers
median = getMedian(numbers,N)
#print some
print mean
print median
print mode
