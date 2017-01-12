def number_needed2(a, b):
    listA = list(a)
    listB = list(b)
    setA = set(listA)
    setB = set(listB)
    common = setA.intersection(setB)
    comList = []
    for ch in common:
        if (listA.count(ch) == listB.count(ch)):
            comList.append(ch)
    return (len(setA) - 2*len(comList) + len(setB))
a = raw_input().strip()
b = raw_input().strip()

def number_needed(a,b):
    count = 0
    freq = [  0 for _ in range(26)]
    listA = list(a)
    listB = list(b)
    
    for a in listA:
        #print a
        #print ord(a)-ord('a')
        freq[ord(a)-ord('a')] +=1
    for a in listB:
        freq[ord(a)-ord('a')] -=1
    for val in freq:
        #print val
        count+= abs(val)
    #print val
    return count

print number_needed(a, b)
