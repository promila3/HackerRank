string = raw_input()


found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
lenS = len(string)
dictS = {}
for s in string:
    if s in dictS :
        dictS[s] +=1
    else :
        dictS[s] = 1

isOdd = 0

for item in dictS :
    if dictS[item] %2 != 0 :
        isOdd +=1
if  (lenS %2 == 1 ) and (isOdd == 1) :
    found = True
elif (lenS % 2 == 0 )and (isOdd == 0) :
    found = True

if not found:
    print("NO")
else:
    print("YES")
