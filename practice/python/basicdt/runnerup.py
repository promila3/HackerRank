# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/submissions/code/122388216

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr = [int(x) for x in arr]
    arr.sort()
    #print(arr)
    print(arr[len(arr)-2])
