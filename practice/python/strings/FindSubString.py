# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    result = 0
    lenS = len(string)
    lenSub = len(sub_string)
    for i in range(lenS-lenSub+1):

        toC = string[i:i+lenSub]
        #print(i, toC)
        result += toC.count(sub_string)
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
