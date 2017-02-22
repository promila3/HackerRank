# Enter your code here. Read input from STDIN. Print output to STDOUT
#Promila Agarwal

def getMedian(numbers,N):
    if (N % 2 == 0 ):
        mid = N/2
        median = (numbers[mid-1] + numbers[mid]) * 1.0 /2
    else :
        mid = N/2
        median = numbers[mid] * 1.0
    return median

N = int(raw_input())
numbers = map(int,raw_input().strip().split())
numbers.sort()
#print numbers
median = getMedian(numbers,N)

if (N % 2 == 0) :
    firstL = numbers[:(N/2)]
    secondL = numbers[(N/2):]
    
else :
    #print N/2
    firstL = numbers[:(N/2)]
    secondL = numbers[(N/2)+1:]
#print firstL
#print secondL
q1 = getMedian(firstL,N/2)
q3 = getMedian(secondL,N/2)


print "%.0f" % q1
print "%.0f" % median
print "%.0f" % q3
