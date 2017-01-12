def is_matched(expression):
    strList = list(expression)
    lenStr = len(strList)
    stack =[]
    checkList = [']','}',')']
    rcheckList = ['[','{','(']
    if lenStr == 0 :
        return True
    if lenStr %2 != 0 :
        return False
    if strList[0] in checkList :
        return False

    for ch in strList :
        #print stack
        if ch in rcheckList :
            stack.append(ch)
        elif len(stack) > 0:
            popChar = stack.pop()
            if (rcheckList.index(popChar) != checkList.index(ch) ) :
                return False
        else :
            return False
        
       
    if len(stack) > 0 :
        return False
    else :
        return True
        
        

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
