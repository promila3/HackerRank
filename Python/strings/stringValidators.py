# https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen
def checkIsAlphanum(s):
    for a in s:
        if a.isalnum():
            print("True")
            return
    print("False")
    return

def checkIsAlpha(s):
    for a in s:
        if a.isalpha():
            print("True")
            return
    print("False")
    return  
def checkIsDigit(s):
    for a in s:
        if a.isdigit():
            print("True")
            return
    print("False")
    return 
def checkIsLower(s):
    for a in s:
        if a.islower():
            print("True")
            return
    print("False")
    return 

def checkIsUpper(s):
    for a in s:
        if a.isupper():
            print("True")
            return
    print("False")
    return 
           
if __name__ == '__main__':
    s = input()
    checkIsAlphanum(s)
    checkIsAlpha(s)
    checkIsDigit(s)
    checkIsLower(s)
    checkIsUpper(s)
